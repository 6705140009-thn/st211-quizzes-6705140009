# Lab 06 Mocking and Test Doubles

Student: **Thet Htoo Naing**

Student ID: **6705140009**

Use unittest.mock to isolate weather, payment, notification, database, and year dependencies. Cover fixed return values, sequential and function-based side effects, exceptions, and interaction assertions. The local pytest.ini also collects exe1.py through exe4.py.

## Topics

- [Mock Lab Submission Documents](documents/README.md)

## Files

- [date_utils.py](date_utils.py)
- [exe1.py](exe1.py)
- [exe2.py](exe2.py)
- [exe3.py](exe3.py)
- [exe4.py](exe4.py)
- [notifications.py](notifications.py)
- [payment.py](payment.py)
- [pytest.ini](pytest.ini)
- [test_date_utils.py](test_date_utils.py)
- [test_function_side_effect.py](test_function_side_effect.py)
- [test_mock_basics.py](test_mock_basics.py)
- [test_notifications.py](test_notifications.py)
- [test_payment.py](test_payment.py)
- [test_problem.py](test_problem.py)
- [test_return_values.py](test_return_values.py)
- [test_solution_preview.py](test_solution_preview.py)
- [test_user_service.py](test_user_service.py)
- [test_verify_calls.py](test_verify_calls.py)
- [test_weather_new.py](test_weather_new.py)
- [user_service.py](user_service.py)
- [weather.py](weather.py)
- [weather_new.py](weather_new.py)

## Run

From the repository root:

```powershell
cd Lab06-MockingAndTestDoubles
python -m pytest -q
```

This command also discovers child tests. The root runner runs each test directory separately to prevent duplicate execution.
