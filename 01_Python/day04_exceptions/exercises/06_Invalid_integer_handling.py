def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2 

def multiply(number_1, number_2):
    return number_1 * number_2

def remainder(number_1, number_2):
    return number_1 % number_2 

def get_valid_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer.")

def main():
    while True:
        # 1. Display the menu options
        print("\n===== OPTIONS =====")
        print("1. Add")
        print("2. Difference")
        print("3. Product")
        print("4. Remainder")
        print("5. Exit")
        
        # 2. Get the option input FIRST
        option = get_valid_integer("Choose an option (1-5): ")
        
        # 3. Check for exit condition
        if option == 5:
            print("Goodbye!")
            break
            
        # 4. Check for an invalid range choice
        if option < 1 or option > 5:
            print("Invalid choice. Please choose a number between 1 and 5.")
            continue
            
        # 5. Get the numbers for calculations
        number_1 = get_valid_integer("Enter a 1st integer: ")
        number_2 = get_valid_integer("Enter a 2nd integer: ")
        
        # 6. Perform calculation based on choice
        if option == 1:
            result = add(number_1, number_2)
            operation = "Sum"
        elif option == 2:
            result = subtract(number_1, number_2)
            operation = "Difference"
        elif option == 3:
            result = multiply(number_1, number_2)
            operation = "Product"
        elif option == 4:
            result = remainder(number_1, number_2)
            operation = "Remainder"
            
        # 7. Print the final result!
        print(f"{operation}: {result}")

if __name__ == "__main__":
    main()
