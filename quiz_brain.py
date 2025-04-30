class QuizBrain:

    def __init__(self,question_list):
        self.question_n = 0
        self.question_list = question_list
        self.score =0

    def still_has_question(self):
        return self.question_n < len(self.question_list)

    def next_question(self):
            current_question = self.question_list[self.question_n]
            self.question_n +=1
            user_an = input(f"Q.{self.question_n }: {current_question.text} (true/false) : ")
            self.check_ans(user_an,current_question.answer)


    def check_ans(self,user_ans,correct_ans):

        if user_ans.lower() == correct_ans.lower():
            print("you are right !")
            self.score +=1
            print(f"your score is : {self.score}/ {self.question_n}")
        else:
            print(" you are wrong ")
            self.score -= 1
            print(f"your score : {self.score}/{self.question_n} total question asked.")
        print(f"right answer is {correct_ans}")

        print("\n")

