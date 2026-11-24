import assert from "node:assert/strict";
import { resolve } from "node:path";
import { connect, pace, readJson, root, saveJson, shortError } from "./studionet.mjs";

const scenarios = readJson(resolve(root, "examples/scenarios.json"));
const deployments = readJson(resolve(root, "deployment_info.json"));
const report = { mode: "rpc_simulation", network: "studionet", cases: {} };

async function main() {
  const { client } = await connect();
  for (const [name, scenario] of Object.entries(scenarios)) {
    const deployment = deployments.deployments[name];
    const result = { address: deployment.address, method: "open" };
    try {
      assert.equal(deployment.status, "FINALIZED");
      await pace();
      const countBefore = await client.readContract({ address: result.address, functionName: "count" });
      await pace();
      const simulated = await client.simulateWriteContract({
        address: result.address, functionName: "open", args: scenario.open,
      });
      await pace();
      const countAfter = await client.readContract({ address: result.address, functionName: "count" });
      assert.equal(Number(simulated), countBefore);
      assert.equal(countAfter, countBefore);
      result.return_value = Number(simulated);
      result.count_before = countBefore;
      result.count_after = countAfter;
      result.status = "PASS";
    } catch (error) {
      result.status = "UNVERIFIED";
      result.error = shortError(error);
    }
    report.cases[name] = result;
    console.log(name, result.status, result.error ?? "");
  }
  report.checked_at = new Date().toISOString();
  report.passed = Object.values(report.cases).filter(result => result.status === "PASS").length;
  report.total = Object.keys(report.cases).length;
  if (process.argv[2]) saveJson(resolve(process.argv[2]), report);
  if (report.passed !== report.total) process.exitCode = 1;
}

main().catch(error => {
  console.error(shortError(error));
  process.exitCode = 1;
});
