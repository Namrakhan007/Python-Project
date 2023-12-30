from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


Question_bank = []

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text,question_answer)
    Question_bank.append(new_question)

quiz = QuizBrain(Question_bank)

while quiz.still_has_questions():
     quiz.next_question()
