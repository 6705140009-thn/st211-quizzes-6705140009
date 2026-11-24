# Sharing Fixtures with conftest.py

Student: **Thet Htoo Naing**

Student ID: **6705140009**

Define the account fixture once in `conftest.py`. Pytest injects it into both tests without an explicit fixture import; each test still receives its own account.

## Files

- [bank.py](bank.py)
- [conftest.py](conftest.py)
- [test_shared_fixture.py](test_shared_fixture.py)

## Run

From the repository root:

```powershell
cd Lab04-FixturesAndTestDataManagement/sharing-fixtures
python -m pytest -q
```
