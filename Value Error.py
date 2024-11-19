def convert_to_int(user_input):
    try:

        number = int(user_input)
        return number
    except ValueError:
        print(f"ValueError: '{user_input}' is not a valid integer.")
        return None

def main():
    while True:
        user_input = input("Please enter an integer (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        result = convert_to_int(user_input)
        if result is not None:
            print(f"You have entered the integer: {result}")

if __name__ == "__main__":
    main()
