# QuizParser builds a quiz from a source file
import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):
    """
    The QuizParser class loads a particular quiz file, parses it, and returns
    a fully-built Quiz object that can then be presented to the user.
    """

    def __init__(self):
        self.new_quiz = Quiz()
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quiz_path):
        # load the file contents
        quiz_text = ""
        with open(quiz_path, "r") as quiz_file:
            if quiz_file.mode == "r":
                quiz_text = quiz_file.read()

        # Parse the file
        xml.sax.parseString(quiz_text, self)

        # return the finished quiz
        return self.new_quiz

    def startElement(self, tag_name, attrs):
        if tag_name == "QuizML":
            self._parse_state = QuizParserState.PARSE_QUIZ
            self.new_quiz.name = attrs["name"]
        elif tag_name == "Description":
            self._parse_state = QuizParserState.PARSE_DESCRIPTION
        elif tag_name == "Question":
            self._parse_state = QuizParserState.PARSE_QUESTION
            if attrs["type"] == "multichoice":
                self._current_question = QuestionMC()
            elif attrs["type"] == "tf":
                self._current_question = QuestionTF()
            self._current_question.points = int(attrs["points"])
            self.new_quiz.total_points += self._current_question.points
        elif tag_name == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUEST_TEXT
            self._current_question.correct_answer = attrs["answer"]
        elif tag_name == "Answer":
            self._current_answer = Answer()
            self._current_answer.name = attrs["name"]
            self._parse_state = QuizParserState.PARSE_ANSWER

    def endElement(self, tag_name):
        if tag_name == "QuizML":
            self._parse_state = QuizParserState.IDLE
        elif tag_name == "Description":
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tag_name == "Question":
            self.new_quiz.questions.append(self._current_question)
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tag_name == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUESTION
        elif tag_name == "Answer":
            self._current_question.answers.append(self._current_answer)
            self._parse_state = QuizParserState.PARSE_QUESTION

    def characters(self, chars):
        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += chars
        elif self._parse_state == QuizParserState.PARSE_QUEST_TEXT:
            self._current_question.text += chars
        elif self._parse_state == QuizParserState.PARSE_ANSWER:
            self._current_answer.text += chars


# Following part is for testing.
if __name__ == "__main__":
    app = QuizParser()
    qz = app.parse_quiz("Quizzes/SampleQuiz.xml")
    print(f"Quiz Name: {qz.name}")
    print(f"Description: {qz.description}")
    print(f"Number of Questions: {len(qz.questions)}")
    print(f"Total Points: {qz.total_points}")
    for q in qz.questions:
        print("-" * 40)
        print(f"Question: {q.text}")
        print(f"Points: {q.points}")
        if type(q) == QuestionMC:
            print("Type: Multiple Choice")
            for answer in q.answers:
                print(f" {answer.name} - {answer.text}")
        elif type(q) == QuestionTF:
            print("Type: True/False")
        print(f"Correct Answer: {q.correct_answer}")
