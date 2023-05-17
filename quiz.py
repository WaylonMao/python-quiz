# The Quiz and Question classes define a particular quiz

class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


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

            # Mark this question as correct if answered correctly
            if response[0] == self.correct_answer:
                self.is_correct = True
            break


class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while (True):
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
#     q1 = QuestionTF()
#     q1.text = "Broccoli is good for you"
#     q1.points = 5
#     q1.correct_answer = "t"
#     q1.ask()
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
#     q2.ask()
#
#     print(q1.is_correct)
#     print(q2.is_correct)