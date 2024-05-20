# For this example, the while loop will count down by threes starting
# from 18 and ending at 0.
starting_number = 18

# The while loop will continue to loop until it reaches 0.
while starting_number >= 0:
    # To make the sequence of numbers easier to read, include a space
    # between each number in the sequence. You can override the default
    # behavior of the print() function by using the "end=" parameter with
    # the print() function. The syntax for adding a space is: end=" "
    print(starting_number, end=" ")

    # Decrement the "starting_number" variable by -3.
    starting_number -= 3

# Should print 18 15 12 9 6 3 0
