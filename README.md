# ReleaseWeave

ReleaseWeave is a catalog of ten standalone GenLayer Intelligent Contracts for software teams and data curators. The contracts turn judgments about migrations, compatibility, test quality and release evidence into explicit workflow states.

| Contract | Use | Enforced rule |
| --- | --- | --- |
| MigrationFence | Review a dataset migration before changing its recorded schema | A proposal is pinned to the current revision. Loss needs explicit acknowledgment and a blocked safeguard prevents commitment. |
| DependencyExit | Replace a software dependency | A candidate that needs an adapter requires a second review of that adapter before selection. |
| SplitLeakLedger | Review a small benchmark for training/test overlap | Every cross-partition sample pair must be reviewed as distinct before freezing the batch. |
| LocaleParity | Publish translated release notices | A source revision invalidates old translation approvals. Published snapshots retain their original text. |
| ReproQuorum | Confirm a reported software defect | Two distinct reporter wallets must reproduce the same version before the maintainer can confirm it. |
| RegressionWitness | Archive a test that catches a repaired defect | The reviewed evidence must show an assertion failing before the fix and passing afterward. |
| DeprecationPact | Coordinate an API retirement with known consumers | Enrolled consumers acknowledge a fixed migration guide before retirement. |
| BuildOrigin | Compare build attestations | Two qualifying builder wallets are required. Conflicting artifact hashes produce a contested result. |
| BatchException | Resolve failed rows from a data import | Only declared failed rows can restore accepted counts. A separate assigned reviewer evaluates repairs. |
| SchemaHandshake | Negotiate a producer/consumer interface | The provider accepts a reviewed consumer offer against a specific schema revision. |

Every source in `contracts/` can be loaded directly into GenLayer Studio. Each contract exposes `count()` and `get(index)`. A call to `open(...)` creates an independent record whose creator controls the relevant maintainer actions.

[Contract APIs](CONTRACTS.md) list the public entry points and their input types. [Example scenarios](examples/scenarios.json) contain constructor arguments, opening calls and follow-up operations. [Design decisions](DECISIONS.md) explain the consensus boundary and the evidence behind each judgment.

## Local tests

Use Python 3.12 or later.

```sh
python3.12 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest -q
```

The direct suite contains 30 tests and runs the contract source with the GenLayer SDK, mocked model responses and serializable closure checks. It exercises unauthorized callers, stale proposals, conflicting results and repeated actions.

## StudioNet

[Deployment records](deployment_info.json) and [explorer links](DEPLOYMENTS.md) accompany the released bundle. Run the verifier to check finalized receipts, source hashes and public views again.

```sh
npm ci
npm run verify:live
```

[Setup](docs/SETUP.md) covers importing an address, using the examples and deploying a fresh batch. [Verification evidence](verification/README.md) describes exactly which checks ran.

The archive includes `MANIFEST.sha256`. From its root, use `sha256sum -c MANIFEST.sha256` to verify the distributed file bytes.
