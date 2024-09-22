
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
        while True:
            self.main()
            if not self.ask_repeat_exercise():
                break  # Exit the loop if user doesn't want to repeat

    # The main program
    def main(self):
        while True:
            # Loop until a valid odd integer is inputted
            while True:
                try:
                    n = int(input("Please input an odd integer: "))
                    # Check if the inputted number is either an even number or an odd number
                    if n % 2 == 0:
                        print("You have entered an even number. Please enter an odd number.")
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

# Run the Program
diamond_shape = DiamondSM()
diamond_shape.run()
