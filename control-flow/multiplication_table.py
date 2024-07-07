def main():
    try:
        # Prompt the user to input a number
        number = int(input("Enter a number to see its multiplication table: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    # Generate and print the multiplication table for the given number from 1 to 10
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    main()