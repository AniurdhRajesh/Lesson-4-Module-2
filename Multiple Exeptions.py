def divide_numbers(num1, num2):
    try:
      
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
    except ZeroDivisionError:
    
        print("Error: You cannot divide by zero.")
    except Exception as e:

        print(f"An unexpected error occurred: {e}")
    finally:
     
        print("Execution of the divide_numbers function is complete.")

def main():
 
    test_cases = [(10, 2), (20, 0), (30, 'a')]
    
    for num1, num2 in test_cases:
        print(f"Attempting to divide {num1} by {num2}:")
        divide_numbers(num1, num2)
        print("-" * 40) 
    
if __name__ == "__main__":
    main()
