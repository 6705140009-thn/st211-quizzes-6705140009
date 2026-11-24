# Bank Operations and Grade Boundaries

Student: **Thet Htoo Naing**

Student ID: **6705140009**

The original bank and grade examples are retained here. Deposits and withdrawals must be positive; starting balances cannot be negative; overdrafts are rejected without changing the balance. `grade.py` maps 80–100 to A, 70–79 to B, 60–69 to C, and 0–59 to F. Scores outside 0–100 raise ValueError. Despite its historical filename, `test_dependent.py` creates fresh accounts and has no order dependency.

## Files

- [bank.py](bank.py)
- [grade.py](grade.py)
- [test_bank.py](test_bank.py)
- [test_bank_validation.py](test_bank_validation.py)
- [test_dependent.py](test_dependent.py)
- [test_grades.py](test_grades.py)
- [test_independent.py](test_independent.py)

## Run

From the repository root:

```powershell
cd Lab02-EffectiveTestCases/bank-and-boundary-values
python -m pytest -q
```
