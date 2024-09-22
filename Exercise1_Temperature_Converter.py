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
        while True:
            self.main()
            if not self.ask_repeat_exercise():
                break  # Exit the loop if user doesn't want to repeat

    # The main program
    def main(self):
        # Loop until a valid temperature is inputted
        while True:
            try:
                # Input of temperature.
                temp = float(input("Please input a temperature: "))
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Input is not a valid number. Please enter a numbered temperature.\n")

        # Showing the inputted temperature
        print(f"The temperature is {temp} degrees")
        # Selecting the conversion type
        self.vert(temp)

    # Selection of conversion
    def vert(self, temp):
        # Prompt for conversion type
        convert = input("\nPlease select conversion type\n  1. Celsius to Fahrenheit | 2. Fahrenheit to Celsius\n  Please select option 1 or 2: ")
        if convert == "1":
            self.c_f(temp)
        elif convert == "2":
            self.f_c(temp)
        else:
            print("Invalid selection.\n")
            self.vert(temp)

    # Ask if the user wants to repeat the current exercise
    def ask_repeat_exercise(self):
        while True:
            repeat = input("\nWould you like to repeat this exercise? (Yes/No): ").strip().lower()
            if repeat == "yes":
                return True
            elif repeat == "no":
                return False
            else:
                print("Invalid input. Please try again. Please enter either 'Yes' or 'No'.")

    # Converting Celsius to Fahrenheit
    def c_f(self, temp):
        c_f_value = (temp * 1.8) + 32
        r_c_f = round(c_f_value, 4)
        print(f"\n   {temp} degrees Celsius is equal to\n   {r_c_f} degrees Fahrenheit")

    # Converting Fahrenheit to Celsius
    def f_c(self, temp):
        f_c_value = (temp - 32) / 1.8
        r_f_c = round(f_c_value, 4)
        print(f"\n   {temp} degrees Fahrenheit is equal to\n   {r_f_c} degrees Celsius")

# Then, you can keep your other classes as they are

temp_converter = TemptConvo()
temp_converter.run()

