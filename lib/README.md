# Consensus helper

Each source includes a `judge(task, evidence, choices)` function. It serializes the evidence, asks for one token, validates that token and independently reproduces it in the validator. The closure captures plain data. Storage access happens outside the model call.

Reuse the pattern by defining a task with explicit decision boundaries and making all consequential state transitions depend on the validated token.
