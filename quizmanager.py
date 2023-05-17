# QuizManager manages the quiz content
import os.path
import os
import quizparser
import datetime


class QuizManager:
    def __init__(self, quiz_folder):
        self.quiz_folder = quiz_folder

        # The most recently selected quiz
        self.the_quiz = None

        # Initialize the collection of quizzes
        self.quizzes = dict()

        # Stores the results of the most recent quiz
        self.results = None

        # The name of the person taking the quiz
        self.quiz_taker = ""

        # Make sure that the quiz folder exists
        if not os.path.exists(self.quiz_folder):
            raise FileNotFoundError(f"Quiz folder {self.quiz_folder} does not exist.")

        # Build the list of quizzes
        self._build_quiz_list()

    def _build_quiz_list(self):
        dir_contents = os.scandir(self.quiz_folder)
        # Parse the XML files in the directory
        for i, f in enumerate(dir_contents):
            if f.is_file():
                parser = quizparser.QuizParser()
                self.quizzes[i + 1] = parser.parse_quiz(f)

    # Print a list of the currently installed quizzes
    def list_quizzes(self):
        for key, value in self.quizzes.items():
            print(f"{key}) {value.name}")

    # start the given quiz for the user and return the results
    def take_quiz(self, quizid, username):
        self.quiz_taker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()

    # prints the results of the most recently taken quiz
    def print_results(self):
        self.the_quiz.print_results(self.quiz_taker)

    # save the results of the most recent quiz to a file
    # the file is named using the current date as
    # QuizResults_YYYY_MM_DD_N (N is incremented until unique)
    def save_results(self):
        pass

# Following is for testing.
# if __name__ == "__main__":
#     qm = QuizManager("Quizzes")
#     qm.list_quizzes()
