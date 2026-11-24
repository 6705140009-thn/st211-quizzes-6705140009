# Reusable Account Fixtures

Student: **Thet Htoo Naing**

Student ID: **6705140009**

The `account` fixture supplies a new account with balance 100 for each test. Compare the fixture-based tests in `test_after.py` with direct setup in `test_bank.py`. Validation tests check invalid operations preserve the balance.

## Files

- [bank.py](bank.py)
- [test_after.py](test_after.py)
- [test_bank.py](test_bank.py)
- [test_bank_validation.py](test_bank_validation.py)

## Run

From the repository root:

```powershell
cd Lab04-FixturesAndTestDataManagement/fixtures
python -m pytest -q
```
