# 07_safe_float.py

while True:
    user_input = input("Please enter a decimal number: ")
    try:
        # Try to convert the input to a float
        valid_float = float(user_input)
        print(f"Success! You entered a valid float: {valid_float}")
        break  # Exit the loop since input is valid
    except ValueError:
        # Handle the error if the conversion fails
        print("Invalid input. That is not a decimal number. Please try again.\n")
