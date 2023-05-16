class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting at startup
        self.greeting()

        # ask the user's name
        self.username = None
        while not self.username:  # while username is None or empty string
            user_input = input("What is your name? ").strip()
            if user_input:  # if user_input is not empty
                self.username = user_input
            else:
                print("Invalid input. Please enter a valid name.")
        print(f"Hello, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("~~~~~~ Welcome to PyQuiz! ~~~~~~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("--------------------------------")
        print("Please make a selection:")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()

        # get the user's selection and act on it. This loop will
        # run until the user exits the app
        selection = ""
        while True:
            selection = input("Selection: ")

            if len(selection) == 0:
                self.menu_error()
            elif selection[0].upper() == "E":
                self.goodbye()
                break
            elif selection[0].upper() == "M":
                self.menu_header()
                continue
            elif selection[0].upper() == "L":
                print("\nAvailable Quizzes Are: ")
                # TODO: list quizzes
                print("--------------------------------\n")
                continue
            elif selection[0].upper() == "T":
                try:
                    quiznum = int(input("Enter the quiz number: "))
                    print(f"\nYou have selected quiz number {quiznum}")
                    # TODO: take quiz
                    print("--------------------------------\n")
                    continue
                except:
                    self.menu_error()
            else:
                self.menu_error()

    # This is the entry point to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    app = QuizApp()
    app.run()
