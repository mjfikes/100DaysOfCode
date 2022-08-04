class QuizBrain:
    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.question_number = 0

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.questions_list)

    def next_question(self):
        curr_q = self.questions_list[self.question_number]
        self.question_number += 1
        guess = input('{0}. {1} True/False? '.format(self.question_number,curr_q.text))


