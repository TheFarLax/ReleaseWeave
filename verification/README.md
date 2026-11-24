# Verification evidence

| Check | Result | Evidence |
| --- | --- | --- |
| GenLayer Direct Mode | 30 tests passed across ten contract modules. | [Text output](direct-tests.txt), [JUnit results](direct-tests.xml) |
| StudioNet deployment | Ten separate finalized deployment transactions with successful constructor execution. | [Explorer links](../DEPLOYMENTS.md), [Deployment records](../deployment_info.json) |
| Deployed source | Each source SHA-256 matched the file sent for deployment. | [Verification output](studionet-verification.txt) |
| Public contract APIs | Each deployed schema matched the expected constructor and methods. | [Contract schemas](../contract_schemas.json) |
| Opening-call simulation | Initial record creation was simulated through the StudioNet RPC and persistent counts were checked before and after. | [Simulation results](studionet-simulations.json) |

Direct Mode uses the official GenLayer Python SDK pinned to GenVM v0.2.16 and controlled LLM responses. The tests include independently repeated validator decisions, changed leader outputs, role boundaries, repeated actions and revision changes.

The live simulations cover the initial `open` entry points, which validate inputs and initialize workflow storage. The model-driven follow-up methods are covered by the local suite with mock responses. The recorded live transactions are the ten constructors.
