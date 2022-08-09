from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

#question_bank = [Question(q.get('text'), q.get('answer')) for q in question_data]
question_bank = [Question(html.unescape(q.get('question')), q.get('correct_answer')) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz Complete!")
print(f"Your final score was {quiz.score}/{len(question_bank)}")
