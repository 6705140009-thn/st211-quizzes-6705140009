# Code Coverage

Student: **Thet Htoo Naing**

Student ID: **6705140009**

Measure statement and branch coverage for role-based access and shipping costs. Compare the weak access tests with the complete suite. Shipping cases cover express service, the heavy-weight threshold, zero and negative weights, and free-shipping eligibility.

## Files

- [access.py](access.py)
- [shipping.py](shipping.py)
- [test_access_complete.py](test_access_complete.py)
- [test_access_weak.py](test_access_weak.py)
- [test_shipping.py](test_shipping.py)
- [test_shipping_complete.py](test_shipping_complete.py)

## Run

From the repository root:

```powershell
cd Code-Coverage
python -m pytest -q
```

## Measure coverage

From this directory:

```powershell
python -m coverage run --branch --source=access,shipping -m pytest -q
python -m coverage report --fail-under=100 -m
python -m coverage html
```

The complete tests achieve 100% statement and branch coverage for the two implementation modules. Generated reports are ignored by Git.
