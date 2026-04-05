# Week 5: Midnight Mail Train

## GitHub Classroom Assignment Brief

- **Repo name:** `ds26-wk05-midnight-mail-train-<student>`
- **Due:** Friday, 23:59 KST
- **Python version:** 3.11+
- **Allowed libraries:** stdlib only

### Graded Files

- `src/challenges.py`
- `tests/test_challenges.py`
- `README.md`

## Story

A late-night rail company is trying to keep its deliveries moving across the city. Your job is to help the control team build and test small tools for train cars, ticket checks, and message handling.

Each problem is short, but each one checks an important idea from class.

## Standards Targeted

- **Primary:** S8 — Recursion + Call Stack Thinking
- **Supporting:** S1 — Python + Testing Fundamentals
- **Supporting:** S9 — Linked Lists
- **Cross-cutting:** S3 — Big-O Reasoning

## Instructions

### What to Do

1. Open the starter repo.
2. Complete the required work in `src/challenges.py`.
3. Run tests with `pytest -q`.
4. Add any required missing tests in `tests/test_challenges.py`.
5. Update `README.md`.
6. Push your work and open a PR.

### Requirements

- Use Python classes where the problem asks for classes.
- Use recursion where the problem says to use recursion.
- Do not use loops in the recursion problems.
- Use type hints on public functions.
- Keep code clear and readable.

## README Requirements

Your `README.md` must include:

- Summary
- Approach
- Complexity
- Edge-case checklist
- Assistance & Sources

## Required Problems

### Problem 1 — Train Cars in Reverse (DLL)

The Midnight Mail Train needs to keep track of train cars in order. Workers sometimes need to inspect the train from the back.

#### Build

- `TrainCarNode`
- `MidnightMailDLL`

#### Implement Methods

- `append_car(car_id: str) -> None`
- `detach_last_car() -> str | None`
- `to_reverse_list() -> list[str]`

#### Rules

- This must be a doubly linked list.
- The node class stores one car and its links.
- The list class manages the overall structure.

#### Edge Cases to Handle

- empty train
- one train car
- several train cars

### Problem 2 — Ticket Code Check

Every delivery ticket code must follow the company rule:

- it starts with `"MM-"`
- it ends with exactly 4 digits

#### Implement

- `is_valid_ticket_code(code: str) -> bool`

#### Testing Requirement

In `tests/test_challenges.py`, you must include tests for:

- 1 valid case
- 2 invalid cases
- 1 edge case

#### Example Ideas

- `"MM-1234"` → `True`
- `"MM-12"` → `False`
- `"XX-1234"` → `False`
- `""` → `False`

### Problem 3 — Count Priority Packages (Recursion)

The control room has a list of package labels. It wants to know how many are marked with a target label.

#### Implement

- `count_priority_labels(labels: list[str], target: str) -> int`

#### Rules

- Use recursion.
- Do not use a loop.
- Return how many times `target` appears.

#### Example

- `count_priority_labels(["PRIORITY", "NORMAL", "PRIORITY"], "PRIORITY") == 2`
- `count_priority_labels([], "PRIORITY") == 0`

### Problem 4 — Clean the Radio Message (Recursion)

The radio system sometimes adds spaces to short emergency messages. The control room wants a cleaned version with all spaces removed.

#### Implement

- `clean_radio_message(message: str) -> str`

#### Rules

- Use recursion.
- Do not use a loop.
- Return a new string with all spaces removed.

#### Example

- `clean_radio_message("go now") == "gonow"`
- `clean_radio_message(" a b ") == "ab"`
- `clean_radio_message("") == ""`

## Optional Stretch — Recursive Refactor

Write an iterative version of one recursion problem and add a short note in `README.md` comparing the two approaches.

### Suggested Options

- `count_priority_labels_iterative(labels: list[str], target: str) -> int`
- `clean_radio_message_iterative(message: str) -> str`

### Stretch Goal

Explain:

- which version feels clearer
- which version uses call stack space

## What Earns Meets vs Exceeds

### Meets

- code works
- tests pass
- recursive problems use a correct base case and recursive step
- DLL methods work for normal cases
- README includes complexity and edge cases

### Exceeds

- strong edge-case handling
- clear, well-named code
- better-than-minimum tests
- good complexity explanations
- thoughtful iterative vs recursive comparison on the stretch
