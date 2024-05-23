from project.calculator import RPNCalculator

def main():
    calculator = RPNCalculator()
    while True:
        try:
            expression = input("Enter RPN expression: ")
            if expression.lower() in ["exit", "quit"]:
                break
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
