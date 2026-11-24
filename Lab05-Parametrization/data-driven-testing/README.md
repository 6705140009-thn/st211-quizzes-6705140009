# Data Driven Testing

Student: **Thet Htoo Naing**

Student ID: **6705140009**

Load uppercase cases from `test_cases.json` and login cases from `logins.csv`. Resolve files relative to the test module so collection works from other directories. CSV boolean fields must be exactly True or False; malformed values raise an error rather than silently becoming False.

## Files

- [logins.csv](logins.csv)
- [test_cases.json](test_cases.json)
- [test_csv_driven.py](test_csv_driven.py)
- [test_data_driven.py](test_data_driven.py)
- [validate.py](validate.py)

## Run

From the repository root:

```powershell
cd Lab05-Parametrization/data-driven-testing
python -m pytest -q
```
