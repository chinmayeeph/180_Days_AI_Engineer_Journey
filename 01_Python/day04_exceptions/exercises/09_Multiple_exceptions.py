# 09_multiple_exceptions.py

def safe_division():
    print("--- Safe Division Program ---")
    
    try:
        # Prompt user for inputs
        num_input = input("Enter the numerator (number to divide): ")
        den_input = input("Enter the denominator (number to divide by): ")
        
        # Convert strings to floats (can trigger ValueError)
        numerator = float(num_input)
        denominator = float(den_input)
        
        # Perform division (can trigger ZeroDivisionError)
        result = numerator / denominator
        print(f"Result: {numerator} / {denominator} = {result}")

    except ValueError:
        # Triggers if the user types letters, symbols, or leaves it blank
        print("Error: You must enter numbers only! Please try running the program again.")
        
    except ZeroDivisionError:
        # Triggers if the denominator entered is 0
        print("Error: You cannot divide by zero! Math rules do not allow this.")

# Run the program
safe_division()
