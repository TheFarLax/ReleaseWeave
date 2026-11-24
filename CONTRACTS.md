# Contract APIs

All constructors take zero arguments. Each contract exposes `count() -> int` and `get(index: int) -> str`. Records are encoded as JSON strings, and indices start at zero.

## MigrationFence

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(dataset: str, current_schema: str, safeguard: str) -> int` | Write |
| `propose(index: int, expected_revision: int, target_schema: str, migration_plan: str) -> int` | Write |
| `commit(index: int, proposal_index: int, acknowledge_loss: bool) -> int` | Write |

## DependencyExit

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(dependency: str, required_behavior: str) -> int` | Write |
| `review(index: int, candidate: str, candidate_documentation: str) -> int` | Write |
| `prove_adapter(index: int, candidate_index: int, adapter_design: str) -> str` | Write |
| `select(index: int, candidate_index: int) -> None` | Write |

## SplitLeakLedger

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(benchmark: str) -> int` | Write |
| `add(index: int, partition: str, sample: str) -> int` | Write |
| `compare(index: int, first: int, second: int) -> str` | Write |
| `freeze(index: int) -> None` | Write |

## LocaleParity

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(notice: str) -> int` | Write |
| `revise(index: int, expected_revision: int, notice: str) -> int` | Write |
| `review(index: int, expected_revision: int, locale: str, translation: str) -> str` | Write |
| `publish(index: int, expected_revision: int, locales_json: str) -> int` | Write |

## ReproQuorum

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(version: str, environment: str, steps_and_expected: str) -> int` | Write |
| `report(index: int, tested_version: str, environment: str, actual_trace: str) -> str` | Write |
| `confirm(index: int) -> None` | Write |

## RegressionWitness

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(defect: str, broken_commit: str, fixed_commit: str) -> int` | Write |
| `evaluate(index: int, test_source: str, before_trace: str, after_trace: str) -> int` | Write |
| `seal(index: int, test_index: int) -> None` | Write |

## DeprecationPact

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(old_api: str, replacement: str, announced_minute: int, cutoff_minute: int, minimum_window: int) -> int` | Write |
| `enroll(index: int) -> None` | Write |
| `lock_guide(index: int, migration_guide: str) -> str` | Write |
| `acknowledge(index: int) -> None` | Write |
| `retire(index: int, observed_minute: int) -> None` | Write |

## BuildOrigin

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(source_commit: str, recipe: str, environment: str) -> int` | Write |
| `attest(index: int, artifact_sha256: str, run_evidence: str) -> str` | Write |
| `seal(index: int) -> str` | Write |

## BatchException

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(batch_ref: str, total_rows: int, failed_rows_json: str, reviewer: str) -> int` | Write |
| `submit(index: int, row_number: int, failed_constraint: str, repaired_row: str) -> None` | Write |
| `adjudicate(index: int, row_number: int) -> str` | Write |
| `retry(index: int, row_number: int, repaired_row: str) -> None` | Write |
| `close(index: int) -> None` | Write |

## SchemaHandshake

| Method | Access |
| --- | --- |
| `count() -> int` | View |
| `get(index: int) -> str` | View |
| `open(provider_schema: str) -> int` | Write |
| `revise(index: int, expected_revision: int, provider_schema: str) -> int` | Write |
| `propose(index: int, expected_revision: int, consumer_expectations: str) -> int` | Write |
| `accept(index: int, offer_index: int) -> int` | Write |
| `agreement_current(index: int, agreement_index: int) -> bool` | View |
