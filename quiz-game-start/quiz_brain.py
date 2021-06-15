class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {q.text} (True/False)?:")
        self.check_answer(answer, q.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,current_answer):
        if user_answer.lower() == current_answer.lower():
            print("you get it right!")
            self.score += 1
        else:
            print("that's wrong!")
        print(f"the current answer: {current_answer}")
        print(f"your current score is: {self.score}/{self.question_number}")
        print("\n")