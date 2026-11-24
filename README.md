# 192-211 Automated Software Testing

[![Python tests](https://github.com/6705140009-thn/st211-quizzes-6705140009/actions/workflows/tests.yml/badge.svg)](https://github.com/6705140009-thn/st211-quizzes-6705140009/actions/workflows/tests.yml)

Student: **Thet Htoo Naing**

Student ID: **6705140009**
Institution: Siam University
Repository: [st211-quizzes-6705140009](https://github.com/6705140009-thn/st211-quizzes-6705140009)

Python coursework covering unit tests, test design, assertions, fixtures,
parametrization, mocking, and code coverage. Each topic keeps its code, tests,
and run instructions together. The original quiz and Roman converter remain
part of the repository.

## Labs and assignments

| Folder | Topics | Guide |
| --- | --- | --- |
| `Lab01-TestingFundamentals` | Basic assertions, Arrange Act Assert, calculator exceptions | [Lab 01](Lab01-TestingFundamentals/README.md) |
| `Lab02-EffectiveTestCases` | Independent tests, bank validation, grade boundaries, positive and negative cases | [Lab 02](Lab02-EffectiveTestCases/README.md) |
| `Lab03-Assertions-Organizations` | Collections, float precision, test classes, markers, skip and xfail | [Lab 03](Lab03-Assertions-Organizations/README.md) |
| `Lab04-FixturesAndTestDataManagement` | Reusable fixtures, conftest, factories, scopes, setup and teardown | [Lab 04](Lab04-FixturesAndTestDataManagement/README.md) |
| `Lab05-Parametrization` | Multiple inputs, custom IDs, fixture parameters, CSV and JSON | [Lab 05](Lab05-Parametrization/README.md) |
| `Lab06-MockingAndTestDoubles` | Return values, side effects, patching, dependency call checks | [Lab 06](Lab06-MockingAndTestDoubles/README.md) |
| `Code-Coverage` | Statement and branch coverage for access and shipping | [Coverage](Code-Coverage/README.md) |
| `RomanConversion` | Roman/integer conversion, validation, round-trip tests | [Roman converter](RomanConversion/README.md) |
| `quiz-01` | Letter grades and boundary tests | [Quiz 01](quiz-01/README.md) |

## Setup

Use Python 3.10 or newer. From the repository root:

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.venv\Scripts\python.exe run_labs.py -q
```

On macOS or Linux, replace `.venv\Scripts\python.exe` with `.venv/bin/python`.
If pytest and coverage are already installed in your active environment:

```powershell
python run_labs.py -q
```

The runner discovers each test directory and starts a separate pytest process.
This isolates repeated teaching module names such as `bank.py` and
`test_bank.py`. Child directories are run separately, so each suite runs once.
Use this runner for the whole repository; running one pytest process at the
root can mix independent teaching modules with identical names.

List suites without running them:

```powershell
python run_labs.py --list
```

For a single topic, change into its directory and run `python -m pytest -q`.
Every topic README provides its exact path and command. The mock lab also
collects the four `exe*.py` exercises through its local `pytest.ini`.

## Verification

Local checks with Python 3.14: **228 passed**, 1 skipped, 2 expected failures,
and 1 intentional XPASS across **22 isolated test suites**.
The coverage lab reaches **100% statement and branch coverage**.

## Expected pytest demonstrations

The skip/xfail topic intentionally contains one skipped future feature, one
expected failure, and one non-strict XPASS. The parameter-ID topic adds one
expected failure to demonstrate marking an individual parameter case. These
are documented teaching examples and do not cause the runner to fail.

The weather example `test_problem.py` demonstrates a weak assertion over a
random dependency. The patched weather tests provide deterministic checks
at the freezing, cold, pleasant, and hot thresholds. Browser/database fixture
examples use labels and do not contact real services. Notification and payment
tests mock external dependencies.

## Coverage

```powershell
cd Code-Coverage
python -m coverage run --branch --source=access,shipping -m pytest -q
python -m coverage report --fail-under=100 -m
python -m coverage html
```

The complete coverage suite reaches 100% statement and branch coverage for
`access.py` and `shipping.py`. Open the generated `htmlcov/index.html` locally.
Virtual environments, Python caches, and generated coverage reports are ignored.

## Continuous integration

[Python tests](https://github.com/6705140009-thn/st211-quizzes-6705140009/actions/workflows/tests.yml)
run on pushes and pull requests with Python 3.10, 3.12, and 3.14. Each job runs
the isolated suites and enforces 100% coverage for the coverage lab modules.

## Submission documents

The completed Word and PDF mock-lab submission is in
[Lab 06 documents](Lab06-MockingAndTestDoubles/documents/README.md), with
Thet Htoo Naing and student ID 6705140009. The blank original worksheet is
kept separately in the same directory as reference.

## Where previous folders moved

| Previous folder | Current location |
| --- | --- |
| `Bank Testing` | `Lab02-EffectiveTestCases/bank-and-boundary-values` |
| `Positive&Negative_Testing` | `Lab02-EffectiveTestCases/positive-negative-testing` |
| `Assertions_Testing` | `Lab03-Assertions-Organizations/assertion-types` |
| `Roman_Testing` | `RomanConversion` |
| `quiz-01` | Retained at the repository root |

The lab numbering and documentation organization use
[the supplied reference repository](https://github.com/AeintKyiPyarSoe/st211-quizzes-6705140003)
as a structural reference. Existing coursework and the reviewed local labs are
organized here with their own matching documentation.
