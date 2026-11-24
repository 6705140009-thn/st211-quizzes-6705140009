# Setup and Teardown

Student: **Thet Htoo Naing**

Student ID: **6705140009**

Create an in-memory SQLite database, yield the connection to each test, and close it in a finally block. Parameterized SQL inserts the student record, and a separate test verifies a fresh database is empty.

## Files

- [test_database.py](test_database.py)

## Run

From the repository root:

```powershell
cd Lab04-FixturesAndTestDataManagement/setup-and-teardown
python -m pytest -q
```
