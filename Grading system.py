def grade(marks):
    if marks >= 80:
        print("You had an 'A'")
    elif marks >= 70:
        print("You got a 'B'")
    elif marks >= 60:
        print("You got a 'C'")
    elif marks >= 50:
        print("You got a 'D'")
    elif marks >= 40:
        print("You got an 'E'")
    elif marks <= 39:
        print("You got an 'F'")
    else:
        print("Enter marks")
def feedback(marks):
    if marks >= 80:
        print("You did Excellent. Keep it up")
    elif marks >= 70:
        print("Very good effort. Keep aiming higher")
    elif marks >= 60:
        print("You're almost there. Try harder")
    elif marks >= 50:
        print("You can do far better. Study more")
    elif marks >= 40:
        print("Not a very good attempt. There is more room for improvement")
    elif marks <= 39:
        print("Don't feel bad about it. See me let's discuss study plans for your development")
    else:
        print("Enter marks")

print("****************************************************************************************************************")
print("1. TEACHER")
print("2. STUDENT")
print("****************************************************************************************************************")
pos = int(input("Kindly select your position in the school?\n"))
print("****************************************************************************************************************")
if pos == 1:
    print("Welcome Sir/Madam. Let's get straight to work.")
    print("****************************************************************************************************************")
    print("1. Level 100")
    print("2. Level 200")
    print("3. Level 300")
    print("4. Level 400")
    print("Which level is the student in?")
    print("****************************************************************************************************************")
    lev = int(input("Kindly enter the number option.\n"))
    if lev == 1:
        def grade100(marks):
            if marks >= 90:
                print("You had an 'A'")
            elif marks >= 75:
                print("You got a 'B'")
            elif marks >= 65:
                print("You got a 'C'")
            elif marks >= 55:
                print("You got a 'D'")
            elif marks >= 45:
                print("You got an 'E'")
            elif marks <= 40:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("****************************************************************************************************************")
        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print("****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option\n"))
        print("****************************************************************************************************************")
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?\n"))
            print("****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the mark\n"))
                print("****************************************************************************************************************")
                grade100(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")
        else:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?\n"))
            print("****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks\n"))
                grade100(mark)
                feedback(mark)
                sum += mark
        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of your marks is {avg}")
        average_of_assignment()
        print("****************************************************************************************************************")

    elif lev == 2:
        def grade200(marks):
            if marks >= 80:
                print("You had an 'A'")
            elif marks >= 70:
                print("You got a 'B'")
            elif marks >= 60:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 39:
                print("You got an 'F'")
            else:
                print("Enter marks")

        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print("****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade200(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade200(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")

        else:
            print("Enter a number option!")


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()

    elif lev == 3:
        def grade300(marks):
            if marks >= 75:
                print("You had an 'A'")
            elif marks >= 65:
                print("You got a 'B'")
            elif marks >= 60:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 39:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print("****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade300(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade300(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")

        else:
            print("Enter a number option!")


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()

    elif lev == 4:
        def grade400(marks):
            if marks >= 70:
                print("You had an 'A'")
            elif marks >= 60:
                print("You got a 'B'")
            elif marks >= 55:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 35:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print("****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            print("****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade400(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            print("****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print("****************************************************************************************************************")
                grade400(mark)
                feedback(mark)
                sum += mark
                print("****************************************************************************************************************")

        else:
            print("Enter a number option!")

        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()


elif pos == 2:
    print("Welcome! Let's get straight to work.")
    print("1. Level 100")
    print("2. Level 200")
    print("3. Level 300")
    print("4. Level 400")
    print("Which level are you in?")
    lev = int(input("Enter the number option.\n"))

    if lev == 1:
        def grade100(marks):
            if marks >= 90:
                print("You had an 'A'")
            elif marks >= 75:
                print("You got a 'B'")
            elif marks >= 65:
                print("You got a 'C'")
            elif marks >= 55:
                print("You got a 'D'")
            elif marks >= 45:
                print("You got an 'E'")
            elif marks <= 40:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print(
            "****************************************************************************************************************")
        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print(
            "****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option\n"))
        print(
            "****************************************************************************************************************")
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?\n"))
            print(
                "****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the mark\n"))
                print(
                    "****************************************************************************************************************")
                grade100(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")
        else:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?\n"))
            print(
                "****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks\n"))
                grade100(mark)
                feedback(mark)
                sum += mark


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of your marks is {avg}")


        average_of_assignment()
        print(
            "****************************************************************************************************************")

    elif lev == 2:
        def grade200(marks):
            if marks >= 80:
                print("You had an 'A'")
            elif marks >= 70:
                print("You got a 'B'")
            elif marks >= 60:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 39:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print(
            "****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade200(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade200(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")

        else:
            print("Enter a number option!")


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()

    elif lev == 3:
        def grade300(marks):
            if marks >= 75:
                print("You had an 'A'")
            elif marks >= 65:
                print("You got a 'B'")
            elif marks >= 60:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 39:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print(
            "****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade300(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade300(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")

        else:
            print("Enter a number option!")


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()

    elif lev == 4:
        def grade400(marks):
            if marks >= 70:
                print("You had an 'A'")
            elif marks >= 60:
                print("You got a 'B'")
            elif marks >= 55:
                print("You got a 'C'")
            elif marks >= 50:
                print("You got a 'D'")
            elif marks >= 40:
                print("You got an 'E'")
            elif marks <= 35:
                print("You got an 'F'")
            else:
                print("Enter marks")


        print("What are you entering marks for?")
        print("1. ASSIGNMENT")
        print("2. EXAMINATION")
        print(
            "****************************************************************************************************************")
        ex_or_ass = int(input("Enter a number option"))
        sum = 0
        if ex_or_ass == 1:
            print("OK. Let's enter marks for assignment")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            print(
                "****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade400(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")
        elif ex_or_ass == 2:
            print("OK. Let's enter marks for examination")
            nu_of_subs = int(input("How many subjects would you like to input?"))
            print(
                "****************************************************************************************************************")
            for i in range(nu_of_subs):
                mark = float(input("Enter the marks"))
                print(
                    "****************************************************************************************************************")
                grade400(mark)
                feedback(mark)
                sum += mark
                print(
                    "****************************************************************************************************************")

        else:
            print("Enter a number option!")


        def average_of_assignment():
            avg = sum / nu_of_subs
            print(f"The average of marks is {avg}")


        average_of_assignment()


else:
    print("Please state whether you're a teacher or student")
