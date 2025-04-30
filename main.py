from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans =  question["correct_answer"]
    new_question = Question(text=question_text,answer=question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()
print("you completed the task")
print(f"************** your total score was {quiz.score} out of 12 ************************")
