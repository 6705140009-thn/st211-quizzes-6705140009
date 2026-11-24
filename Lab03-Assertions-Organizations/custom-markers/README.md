# Custom Markers and Strict Validation

Student: **Thet Htoo Naing**

Student ID: **6705140009**

The local `pytest.ini` registers smoke, slow, and regression markers and enables strict marker validation. `test_strict.py` uses a registered smoke marker. Changing it to an unregistered name intentionally demonstrates a collection error.

## Files

- [pytest.ini](pytest.ini)
- [test_markers.py](test_markers.py)
- [test_strict.py](test_strict.py)

## Run

From the repository root:

```powershell
cd Lab03-Assertions-Organizations/custom-markers
python -m pytest -q
```

Filter smoke tests with `python -m pytest -m smoke -q`.
