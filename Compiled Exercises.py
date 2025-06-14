# ------------------------------------------- #
#   Name: Sophia Queen Lim                    #
#   Subject: Data Structure and Algorithm     #
#   Lab Activity 1: Python review             #
#   Compiled Exercises 1, 2, and 3            #
# ------------------------------------------- #


# Picking an Exercise:
class Pick:
    def __init__(self):
        self.run()

    def run(self):
        # Loop exercise selection
        while True:
            try:
                # Choosing an exercise 
                choice = int(input("\nPlease pick an exercise to run\n"
                                   "Exercise 1: Temperature Converter\n"
                                   "Exercise 2: Ohm's Law Calculator\n"
                                   "Exercise 3: Diamond Shape\n"
                                   "(1, 2, or 3): "))
                # Select an exercise and run its class
                if choice == 1:
                    if not self.run_exercise(TemptConvo):
                        break
                elif choice == 2:
                    if not self.run_exercise(VolCurRes):
                        break
                elif choice == 3:
                    if not self.run_exercise(DiamondSM):
                        break
                else:
                    print("Invalid choice. Please choose again.\n")
            except ValueError:
                print("Please enter a valid integer.\n")

    # Run an exercise and handle the repeat/new exercise logic
    def run_exercise(self, exercise_class):
        while True:
            # Create an instance of the exercise and run it
            exercise_instance = exercise_class()
            exercise_instance.run()
            # Asking for the repition of the exercise
            if not self.ask_repeat_exercise():
                # If preferred not to repeat the exercise. It will ask if they want to pick another exercise instead.
                return self.ask_new_exercise()

    # Ask if the user wants to repeat the current exercise
    def ask_repeat_exercise(self):
        while True:
            repeat = input("\nWould you like to repeat this exercise? (Yes/No): ").strip().lower()
            # If yes, repeat the exercise
            if repeat == "yes":
                return True
            # If no, proceed to ask about picking another exercise
            elif repeat == "no":
                return False
            # If input is not Yes or No, raise an Invalid input
            else:
                print("Invalid input. Please try again. Please enter either 'Yes' or 'No'.")

    # Ask if the user wants to pick a new exercise
    def ask_new_exercise(self):
        while True:
            new_exercise = input("\nWould you like to pick another exercise? (Yes/No): ").strip().lower()
            # If user selects yes, pick a new exercise
            if new_exercise == "yes":
                return True
            # If user selects no, end the program
            elif new_exercise == "no":
                print("Thank You! Goodbye!")
                return False
            # If input is not Yes or No, raise an Invalid input
            else:
                print("Invalid input. Please try again. Please enter either 'Yes' or 'No'.")


# Exercise 1: Temperature Converter
class TemptConvo:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen . . .-".center(self.width))
        print("-Exercise 1: Temperature Converter-".center(self.width))
        print("-From Celsius to Fahrenheit and from Fahrenheit to Celsius-\n".center(self.width))

    # The main method that starts the temperature conversion process
    def run(self):
        self.main()

    # The main program
    def main(self):
        # Loop until a valid temperature is inputted
        while True:
            try:
                # Input of temperature.
                temp = float(input("Please input a temperature: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                # If the input is not a number, print an error and loop again
                print("Input is not a valid number. Please enter a numbered temperature.\n")
       
        # Showing the inputted temperature
        print(f"The temperature is {temp} degrees")
        # Selecting the conversion type
        self.vert(temp)

    # Selection of conversion
    def vert(self, temp):
        # Prompt for conversion type
        convert = input("\nPlease select conversion type\n  1. Celsius to Fahrenheit | 2. Fahrenheit to Celsius\n  Please select option 1 or 2: ")
        # Selecting '1' to convert from Celsius to Fahrenheit
        if convert == "1":
            self.c_f(temp)
        # Selecting '2' to convert from Fahrenheit to Celsius
        elif convert == "2":
            self.f_c(temp)
        # If input is not 1 or 2, raise an Invalid selection and call vert() again
        else:
            print("Invalid selection.\n")
            self.vert(temp)

    # Converting Celsius to Fahrenheit
    def c_f(self, temp):
        c_f_value = (temp * 1.8) + 32
        r_c_f = round(c_f_value, 4)
        # Show result
        print(f"\n   {temp} degrees Celsius is equal to\n   {r_c_f} degrees Fahrenheit")

    # Converting Fahrenheit to Celsius
    def f_c(self, temp):
        f_c_value = (temp - 32) / 1.8
        r_f_c = round(f_c_value, 4)
        # Show result
        print(f"\n   {temp} degrees Fahrenheit is equal to\n   {r_f_c} degrees Celsius")


# Exercise 2: Ohm's Law Calculator
class VolCurRes:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen . . .-".center(self.width))
        print("-Exercise 2: Ohm's Law Calculator-".center(self.width))
        print("-Voltage | Current | Resistance-\n".center(self.width))

    # The main method that starts the Ohm's Law calculation
    def run(self):
        self.main()

    # The main program
    def main(self):
        # Loop until the user provides a valid choice for the calculation
        while True:
            try:
                # Asking the user what they want to calculate
                v_c_r = int(input("What do you want to calculate?\n 1. Voltage\n 2. Current\n 3. Resistance\n   : "))
                # Calculate voltage
                if v_c_r == 1:
                    self.voltage()
                # Calculate current
                elif v_c_r == 2:
                    self.current()
                # Calculate resistance
                elif v_c_r == 3:
                    self.resistance()
                else:
                    # If input is not valid, print an error and loop again
                    print("Invalid input. Please enter one of the given number choices (1, 2, or 3).")
                    continue
                break  # Exit the loop if a valid choice was made
            except ValueError:
                # If the input is not a number, raise an Invalid input and loop again
                print("Invalid input. Please enter a valid number (1, 2, or 3).")

    # Calculate voltage
    def voltage(self):
        # Loop until valid values for current and resistance are inputted
        while True:
            try:
                cur = float(input("Please input the current: "))
                res = float(input("Please input the resistance: "))
                # Formula to calculate the voltage
                vol = cur * res
                print("\nThe Voltage is:", vol)
                break
            # If input is not a valid value, raise a Value Error
            except ValueError:
                print("Invalid input. Please enter valid values for the current and resistance.\n")

    # Calculate current
    def current(self):
        # Loop until valid values for voltage and resistance are inputted
        while True:
            try:
                vol = float(input("Please input the voltage: "))
                res = float(input("Please input the resistance: "))
                # Check if resistance is zero to avoid division by zero
                if res == 0:
                    print("\nInvalid input. Resistance cannot be zero.")
                    continue
                # Formula to calculate the current
                cur = vol / res
                print("\nThe Current is:", cur)
                break
            # If input is not a valid value, raise a Value Error
            except ValueError:
                print("Invalid input. Please enter valid values for the voltage and resistance.")

    # Calculate resistance
    def resistance(self):
        # Loop until valid values for voltage and current are inputted
        while True:
            try:
                vol = float(input("Please input the voltage: "))
                cur = float(input("Please input the current: "))
                # Check if current is zero to avoid division by zero
                if cur == 0:
                    print("\nInvalid input. Current cannot be zero.")
                    continue\
                # Formula to calculate the resistance
                res = vol / cur
                print("\nThe Resistance is:", res)
                break
            # If input is not a valid value, raise a Value Error
            except ValueError:
                print("Invalid input. Please enter valid values for the voltage and current.\n")


# Exercise 3: Diamond Shape
class DiamondSM:
    def __init__(self):
        # Introducing the program
        self.width = 80
        print("-You have chosen . . .-".center(self.width))
        print("-Exercise 3: Diamond Shape-".center(self.width))
        print("-**********-\n".center(self.width))

    # The main method that starts the Diamond Shape drawing process
    def run(self):
        self.main()

    # The main program
    def main(self):
        while True:
            # Loop until a valid odd integer is inputted
            while True:
                try:
                    n = int(input("Please input an odd integer: "))
                    # Chack if the inputted number is either an even number or an odd number
                    if n % 2 == 0:
                        print("Please provide an odd integer.")
                    else:
                        self.diamond(n)
                        break
                # If input is not an odd integer, raise a Value Error
                except ValueError:
                    print("Invalid input. Please enter an odd integer.")
            break

    # Printing the diamond shape
    def diamond(self, n):
        # Print first half of the diamond
        for i in range(n // 2 + 1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
        # Print second half of the diamond
        for i in range(n // 2 - 1, -1, -1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))


# Run the Program
Pick()
