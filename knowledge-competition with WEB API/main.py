from question_model import Question
from data import question_data
from question_machine import  QuestionMachine
from user_interface import  UserInterface
# TODO 2: Creating the List of Question Objects from the Data  and Saving into Question Pool

question_pool = []

for data in question_data:

    text = data['question']
    answer = data['correct_answer']
    question_ = Question(text, answer)
    question_pool.append(question_)

question_machine_ = QuestionMachine(question_pool)
user_interface = UserInterface(question_machine_)

# while question_machine_.any_unused_question():
#     question_machine_.next_question()

print("You've completed the competiton!")
print(f"Your Final Score was {question_machine_.score}/{len(question_pool)}.")