class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list =q_list
        self.score =0

    def still_has_questions(self):

       if self.question_number < len(self.question_list):
           return True
       elif self.question_number ==len(self.question_list):
           print("You've completed the quiz!!!")
           print(f"Your final score was: {self.score}/{self.question_number} ")

       else:
           return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer =input(f"Q.{self.question_number}:{current_question.text} ?(True/False):")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower()==correct_answer.lower() :
            self.score +=1
            print("You got it right")
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("you are wrong")
            print(f"Your score is {self.score}/{self.question_number}")
        print(f"your correct answer was: {correct_answer}")



