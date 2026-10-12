def get_valid_age():
    while True:
        try:
            # 1. Ask the user to enter their age
            age = int(input("Enter your age: "))
            
        except ValueError:
            # 2. Handle non-integer input (like 'abc')
            print("Invalid input. Enter a whole number.")
            continue  # Skips back to the top of the while loop to ask again

        # 3. Reject ages below 0
        if age < 0:
            print("Age cannot be negative.")
            continue  # Ask again

        # 4. Reject an age above 120
        elif age > 120:
            print("Please enter a realistic age.")
            continue  # Ask again
            
        elif age == 0:
            print("Age cannot be zero.")
            continue  # Ask again

        else:
            # 6. If it passes all checks, break the loop and return it
            print(f"Accepted age: {age}")
            return age

# Run the function
get_valid_age()



