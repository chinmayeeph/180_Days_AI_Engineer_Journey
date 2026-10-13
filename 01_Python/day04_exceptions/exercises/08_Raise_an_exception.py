# 08_raise_exception.py

def validate_age(age):
    # Check if the age is negative
    if age < 0:
        # Explicitly raise a ValueError with a custom descriptive message
        raise ValueError("Age cannot be negative.")
    
    print(f"Age {age} is valid.")

# Example usage (Testing the function):
try:
    validate_age(25)   # This works perfectly
    validate_age(-5)   # This will trigger the exception
except ValueError as error:
    print(f"Caught an expected error: {error}")
