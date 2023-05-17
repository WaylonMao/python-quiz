from quizmanager import QuizManager


class QuizApp:
    QUIZ_FOLDER = "Quizzes"

    def __init__(self):
        self.username = ""
        self.qm = QuizManager(self.QUIZ_FOLDER)

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

        # get the user's selection and act on it. This loop will
        # run until the user exits the app
        selection = ""
        while True:
            self.menu_header()
            selection = input("Selection: ")

            if len(selection) == 0:
                self.menu_error()
            elif selection[0].upper() == "E":
                self.goodbye()
                break
            elif selection[0].upper() == "L":
                print("\nAvailable Quizzes Are: ")
                # List quizzes
                self.qm.list_quizzes()
                print("--------------------------------\n")
                continue
            elif selection[0].upper() == "T":
                try:
                    self.qm.list_quizzes()
                    quiznum = int(input("Enter the quiz number: "))
                    print(f"\nYou have selected quiz number {quiznum}")
                    # Take quiz
                    self.qm.take_quiz(quiznum, self.username)
                    self.qm.print_results()
                    print("--------------------------------\n")
                    do_save = input("Would you like to save your results? (Y/N) ")
                    do_save = do_save.capitalize()
                    if len(do_save) > 0 and do_save[0] == "Y":
                        self.qm.save_results()
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
