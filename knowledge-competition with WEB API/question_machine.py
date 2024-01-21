# TODO 3: Creating a Question Machine Class
# Question Machine Class Responsibilities : Asking the questions | Checking if the answer was correct | Checking is game over
import html


class QuestionMachine:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

# TODO 4: Creating methods for Question Machine Class
    def any_unused_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        quest_text = html.unescape(current_question.text)
        user_answer = input(f"Question {self.question_number}: {quest_text} (True/False)?: ")
        self.check_answer(user_answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\t Congratulations, Keep going on!")
        else:
            print("\t Oh No, It was wrong answer.")
            print(f"\t The correct answer was {correct_answer}.")

        print(f"The current score is {self.score}/{self.question_number}.")
        print("\n")