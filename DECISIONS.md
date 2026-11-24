# Design decisions

## Consequential results are exact

Each model task returns a closed vocabulary result. The validator independently repeats the same task against the same evidence and compares the complete result. A result that enables commitment, selection, confirmation or accounting is therefore also the result checked by the validator.

The short vocabulary is normalized before comparison. Invalid model output raises a contract error. The validator rejects an errored leader result. Direct tests supply an alternative leader result to the actual validator function and check that it is rejected.

## State transitions follow judgment

Roles, counters, revisions, participant limits and stored snapshots are managed deterministically after consensus. A schema change invalidates an outstanding MigrationFence proposal. A provider revision makes old SchemaHandshake offers stale and marks previous agreements as historical. A BuildOrigin record stores a digest only when every qualifying builder agrees on that exact digest.

SplitLeakLedger limits a batch to eight samples. Freezing requires a DISTINCT review for every training/test pair. Exact duplicate text is detected by deterministic comparison. Related dataset batches can be handled as independent records.

BatchException starts from an explicit list of failed row numbers. Only those rows can receive repairs. A repair accepted by the assigned reviewer moves exactly one unit from failed to accepted, and each row can do so once. Rejected repairs can be retried up to four adjudications with the earlier review retained.

## What the evidence represents

RegressionWitness and BuildOrigin evaluate supplied source excerpts, traces and claims. Integrators establish how those records were produced and which wallets represent trusted builders or maintainers. The contracts record what the submitted evidence supports. The model does not execute submitted code.

Distinct wallets are the quorum unit for ReproQuorum and BuildOrigin. They provide address separation. Applications can maintain a verified reporter list when organizational independence matters.

DeprecationPact's announcement, cutoff and observed retirement minute are caller-supplied Unix minutes. Enrollment remains open until a complete guide is locked. The resulting pact applies to those enrolled consumers. Applications establish the consumer roster and time source.

## Reuse and layout

The standalone source/test/catalog structure follows the Penumbra reference supplied for the first bundle. The tested StudioNet deployment journal was reused from CivicWorks, with its contract-specific threshold check removed. The ten workflows and their source code were written for ReleaseWeave.

Every Python file contains the small helpers it calls. This permits direct single-file deployment in Studio without local module imports.
