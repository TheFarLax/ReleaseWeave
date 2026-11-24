# Setup

## Use a published instance

Open [GenLayer Studio](https://studio.genlayer.com), then import a contract address from [DEPLOYMENTS.md](../DEPLOYMENTS.md). The public view `count()` reports how many workflow records exist. Select an account and call `open(...)` using an example to create your own record.

For a new instance, load any single file from `contracts/` in the Studio editor. All ten constructors take zero arguments.

## Run tests

Create a Python 3.12 virtual environment and install `requirements-dev.txt`. Run `python -m pytest -q` from the project root. The GenLayer testing package downloads the pinned GenVM v0.2.16 Python SDK on first use.

## Verify the published batch

Use Node.js 22 or later.

```sh
npm ci
npm run verify:live
```

The verifier checks chain ID 61999, finalized constructor receipts, source digests and each instance's public count. A temporary RPC failure is retried during the verification window.

## Deploy another batch

Create a local `.env` from `.env.example` and set `STUDIONET_PRIVATE_KEY` to a dedicated test wallet key.

```sh
node --env-file=.env deploy/studionet.mjs submit
node deploy/studionet.mjs wait
```

The deployment script submits contracts sequentially and stores each transaction hash in `deployments.local.json`. Repeating `submit` skips entries with a known transaction hash. A submission with an uncertain response is retained for reconciliation against the sender's explorer history before another broadcast.

To verify that new batch, use `node deploy/studionet.mjs verify --state deployments.local.json`.

## Work with examples

Each entry in [scenarios.json](../examples/scenarios.json) supplies a first call and follow-up operations. Use the actual index returned by each opening call. Replace example addresses with the participating wallets. All supplied text and transaction arguments are public.

## Simulate opening calls

Run `node deploy/simulate.mjs` after installing dependencies. The script simulates the initial `open` call for all ten deployed contracts and checks record counts before and after. Each simulation uses the public RPC with a zero-address caller in temporary state.
