# The Quiz and Question classes define a particular quiz
import datetime
import sys
import random


class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions: [Question] = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0

    def print_header(self):
        print("\n\n*******************************************")
        # Print the quiz header
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("*******************************************\n")

    def print_results(self, quiz_taker, file=sys.stdout):
        print("*******************************************", file=file, flush=True)
        print(f"RESULTS FOR {quiz_taker}", file=file, flush=True)
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", file=file, flush=True)
        print(f"TIME TO COMPLETE: {str(self.completion_time)}", file=file, flush=True)
        print(f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct.", file=file, flush=True)
        print(f"SCORE: {self.score} points out of possible {self.total_points}", file=file, flush=True)
        print("*******************************************\n", file=file, flush=True)

    def take_quiz(self):
        # Initialize the quiz state
        self.score = 0
        self.correct_count = 0
        self.completion_time = 0

        for q in self.questions:
            q.is_correct = False

        # Print the header
        self.print_header()

        # Randomize the questions
        random.shuffle(self.questions)

        # Record the start time of quiz
        start_time = datetime.datetime.now()

        # Execute each question and record the result
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points
            print("--------------------------------\n")

        # Record the end time of the quiz
        end_time = datetime.datetime.now()

        # Ask the use if they want to review the quiz
        response = input("Would you like to review the quiz? (Y/N) ")
        print("--------------------------------\n")
        if len(response) != 0 and response[0].upper() == "Y":
            for q in self.questions:
                print(f"Question: {q.text}")
                if type(q) == QuestionMC:
                    for answer in q.answers:
                        if answer.name == q.response:
                            print("-> ", end="")
                        else:
                            print("   ", end="")
                        if answer.name == q.correct_answer:
                            print(f"{answer.name}) {answer.text} (Correct)")
                        else:
                            print(f"{answer.name}) {answer.text}")
                else:
                    print(f"Correct Answer: ", end="")
                    if q.correct_answer == 't':
                        print("True")
                    else:
                        print("False")
                    print(f"Your Answer: ", end="")
                    if q.response == 't':
                        print("True")
                    else:
                        print("False")
                print(f"Points: {q.points}")
                if q.is_correct:
                    print("Correct!")
                else:
                    print("Incorrect!")
                print("--------------------------------\n")
                next = input("Press Enter key to continue...")
                print("--------------------------------\n")

        # Calculate the time to complete the quiz
        self.completion_time = end_time - start_time
        self.completion_time = datetime.timedelta(seconds=round(self.completion_time.total_seconds()))

        # Return the results
        return (self.score, self.correct_count, self.total_points)


class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False
        self.response = ""


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            # Check to see if no response was entered
            if len(response) == 0:
                print("Sorry, that's not a valid response. Please try again")
                continue

            # Check to see if either T or F was given
            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("Sorry, that's not a valid response. Please try again")
                continue

            self.response = response[0].lower()

            # Mark this question as correct if answered correctly
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while True:
            # Present the question and possible answers
            print(self.text)
            for a in self.answers:
                print(f"{a.name}) {a.text}")

            response = input("? ")

            # Check to see if no response was entered
            if len(response) == 0:
                print("Sorry, that's not a valid response. Please try again")
                continue

            # Check if the response is in the available answer names
            valid_responses = [a.name for a in self.answers]
            if response not in valid_responses:
                print("Sorry, that's not a valid response. Please try again")
                continue

            self.response = response[0].lower()

            # Mark this question as correct if answered correctly
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class Answer:
    def __init__(self):
        # define the Answer fields
        self.text = ""
        self.name = ""

# Following part is for testing
# if __name__ == "__main__":
#     qz = Quiz()
#     qz.name = "Sample Quiz"
#     qz.description = "This is a sample quiz!"
#
#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     qz.questions.append(q1)
#
#     q2 = QuestionMC()
#     q2.text = "What is 2+2?"
#     q2.points = 10
#     q2.correct_answer = "b"
#     ans = Answer()
#     ans.name = "a"
#     ans.text = "3"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "b"
#     ans.text = "4"
#     q2.answers.append(ans)
#     ans = Answer()
#     ans.name = "c"
#     ans.text = "5"
#     q2.answers.append(ans)
#     qz.questions.append(q2)
#
#     qz.total_points = q1.points + q2.points
#     result = qz.take_quiz()
#     print(result)
