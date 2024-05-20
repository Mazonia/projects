# This function accepts a CEO's salary as a variable.
# It counts the number of digits in the salary and
# returns the sentence like:
# "The CEO has a 6-figure salary."
def X_figure(salary):
    # Initializes the counter as an integer.
    tally = 0

    # The if-statement checks if the variable "salary"
    # is equal to 0.
    if salary == 0:
        # If true, then it increments the counter to
        # show there is 1 digit in 0.
        tally += 1

    # The while loop starts to run while the "salary"
    # is greater than or equal to 1 (the loop will
    # not run if the "salary" is 0).
    while salary >= 1:
        # The body of the while loop counts the digits
        # in "salary" by counting the number of times
        # "salary" can be divided by 10 until "salary"
        # is no longer >= 1.
        salary = salary / 10

        # Add 1 to the counter to tally the number of
        # times the loop runs.
        tally += 1

    # Return the results of the "tally" of the number
    # of digits in "salary".
    return tally


# Call the X_figure function with 1 parameter, converted to a string,
# inside a print function with additional strings.
print("The CEO has a " + str(X_figure(2300000)) + "-figure salary.")

# Should print"The CEO has a 7-figure salary."
