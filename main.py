from functions.advanced_operations import power, sqrt, log
from functions.basic_operations import add, subtract, multiply, divide


def main():
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Logarithm")
        print("8. Exit")
        
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")
        
        if choice == '8':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            try:
                num1 = float(input("Enter first number: "))
                if choice in ['1', '2', '3', '4', '5']:
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {power(num1, num2)}")
            elif choice == '6':
                print(f"Result: {sqrt(num1)}")
            elif choice == '7':
                base = input("Enter base (default is 10): ")
                base = float(base) if base else 10
                print(f"Result: {log(num1, base)}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
