# This function will accept two integer variables: the floor
# number that a passenger "enter"s an elevator and the floor
# number the passenger is going to "exit". Then, the function
# counts up or down from the two floor numbers.
def elevator_floor(enter, exit):
    # The "floor" variable will be used as a counter and to
    # print the floor numbers. The "elevator_direction"
    # variable will hold the string "Going up: " or
    # "Going down: " plus the count up or down of the
    # "floor" numbers.
    floor = enter
    elevator_direction = ""

    # If the passenger enters the elevator on a floor that
    # is higher than the destination floor:
    if enter > exit:

        # Then the "elevator_direction" string will be
        # initialized with the string "Going down: ".
        elevator_direction = "Going down: "

        # While the "floor" number is greater than or
        # equal to the exit floor number:
        while floor >= exit:
            # The "floor" number is converted to a string
            # and is appended to the string variable
            # "elevator_direction".
            elevator_direction += str(floor)

            # If the "floor" number is still greater than
            # the exit floor number:
            if floor > exit:
                # A pipe | character is added between each
                # floor number in the string variable
                # "elevator_direction" to provide a visual
                # divider between numbers. The if-statement
                # above (if floor > exit) prevents the pipe
                # character from appearing after the "floor"
                # number is no longer greater than the "exit"
                # variable.
                elevator_direction += " | "

                # Decrement the "floor" number as the elevator
                # goes down.
            floor -= 1

    # Else, it is implied that the passenger is entering the
    # elevator on a floor that is lower than the destination
    # floor.
    else:

        # The "elevator_direction" string will be initialized
        # with the string "Going up: ".
        elevator_direction = "Going up: "

        # While the "floor" number is less than or equal to the
        # "exit" floor number:
        while floor <= exit:

            # Convert the the "floor" number to a string and append
            # it to the string variable "elevator_direction".
            elevator_direction += str(floor)

            # If the entry floor number is still less than the exit
            # floor number:
            if floor < exit:
                # The pipe | character is added between each
                # floor number in the string variable
                # "elevator_direction" to provide a visual
                # divider between numbers. The if-statement
                # above (if floor < exit) prevents the pipe
                # character from appearing after the "floor"
                # number is no longer less than the "exit"
                # variable.
                elevator_direction += " | "

            # Increments the "floor" number as the elevator goes up.
            floor += 1

    # Returns the string holding the elevator direction (Going down or
    # Going up) along with the floor countdown or count up.
    return elevator_direction


# Call the function with 2 integer parameters.
print(elevator_floor(1, 4))  # Should print Going up: 1 | 2 | 3 | 4
print(elevator_floor(6, 2))  # Should print Going down: 6 | 5 | 4 | 3 | 2
