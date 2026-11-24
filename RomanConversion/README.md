# Roman Numeral Conversion

Student: **Thet Htoo Naing**

Student ID: **6705140009**

The existing converter supports canonical Roman numerals from I through MMMCMXCIX (1–3999), including lowercase input. Invalid characters, repetitions, subtraction, ordering, and out-of-range values raise ValueError. Non-string Roman input raises TypeError. The integer API accepts integers from 1 to 3999 and rejects booleans and other types. Tests cover both conversion directions and round trips.

## Files

- [roman.py](roman.py)
- [test_roman.py](test_roman.py)
- [test_round_trip.py](test_round_trip.py)

## Run

From the repository root:

```powershell
cd RomanConversion
python -m pytest -q
```

## Interactive converter

From this directory, run `python roman.py` and enter a Roman numeral when prompted. Enter `no` at the continuation prompt to exit.
