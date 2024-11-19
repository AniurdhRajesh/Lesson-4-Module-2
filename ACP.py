def check_age(age):
    if age % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    while True:
        user_input = input("Please enter your age (0-116) (or type 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        
        try:
            age = int(user_input) 
            if age < 0 or age > 116:
                print("Error: Age must be between 0 and 116. Please enter a valid age.")
            else:
                age_type = check_age(age)
                print(f"Your age is {age} and it is {age_type}.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid integer for age.")

if __name__ == "__main__":
    main()
