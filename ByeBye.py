def main():
    while True:
        user_input = input("Enter a number (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            number = int(user_input)
            if number % 2 == 0:
                print("Number is divisible by 2. Entering infinite loop...")
                while True:
                    print("bye")
        except ValueError:
            print("That's not a valid number! Please enter an integer.")

if __name__ == "__main__":
    main()
