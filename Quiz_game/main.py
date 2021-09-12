from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

new_list = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    new_list.append(new_question)

quiz = QuizBrain(new_list)

while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print("\n\nYou have completed the quiz. Hurray!!")
print(f"\t\tFinal Score: {quiz.score}/{quiz.question_number}")
