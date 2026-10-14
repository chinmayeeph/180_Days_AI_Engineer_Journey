# Day 4 — Exceptions

## Learning Source

- CS50P Week 3 — Exceptions
- Automate the Boring Stuff with Python

## Topics Covered

- try
- except
- else
- finally
- ValueError
- ZeroDivisionError
- FileNotFoundError
- NameError
- raise
- pass
- Input validation

## Exercises Completed

- Safe division calculator
- Number input validation
- File opening error
- Menu system
- Invalid age handling
- Invalid integer handling
- Safe float input
- Raise an exception
- Multiple exceptions

## Problems Completed

- Fuel Gauge
- Felipe’s Taqueria
- Grocery List
- Outdated

## Challenge

- Student Marks Analyzer

## What I Learned

- Graceful Crash Prevention: Python uses try and except blocks to intercept errors at runtime, preventing programs from abruptly crashing when unexpected events occur.
- Flow Control with Else and Finally: The else block runs only when the try block encounters no errors, while the finally block executes unconditionally, making it ideal for cleanup tasks like closing files.
- Specific Error Handling: Catching targeted exceptions (such as ValueError, ZeroDivisionError, or FileNotFoundError) provides precise control over debugging and helps avoid broad, unsafe catch-all handlers.
- Intentional Error Generation: The raise keyword allows developers to deliberately trigger specific exceptions to enforce data constraints and robust input validation rules.
- Silent Handling Cautiously: The pass statement can bypass non-critical exceptions silently, though it must be used sparingly to keep from hiding actual application logic flaws.

## Difficulties

- Differentiating Blocks: Tracking the precise execution order and distinct use cases of else versus finally blocks during complex error scenarios.
- Handling Multiple Exceptions: Keeping code readable and efficient when nesting or handling multiple different error types simultaneously under a single try statement.
- Robust Input Validation: Designing clean loops that continuously prompt users for input until they provide valid data, especially when dealing with mixed string and numerical data types.

## Testing

Tested valid inputs:
- Yes

Tested invalid inputs:
- Yes

Tested edge cases:
- Yes

## Key Takeaway

I learned how to handle predictable errors using Python exceptions.