Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.
                                                                                                                       
                                                                                                                       
                                                                                                                       # Initialize variables to store the largest and smallest numbers
largest = None
smallest = None

while True:
    # Prompt the user for input
    num = input("Enter a number: ")

    # Check if the user wants to exit
    if num == "done":
        break

    try:
        # Convert the input to an integer
        num = int(num)

        # Update the largest number
        if largest is None or num > largest:
            largest = num

        # Update the smallest number
        if smallest is None or num < smallest:
            smallest = num

    except ValueError:
         #Handle invalid input (non-integer values)
        print("Invalid input")

# Print the results
if largest is not None and smallest is not None:
    print("Maximum is", largest)
    print("Minimum is", smallest)
else:
    print("No valid numbers were entered.")
