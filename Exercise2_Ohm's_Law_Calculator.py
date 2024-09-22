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

