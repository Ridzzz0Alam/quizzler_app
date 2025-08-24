import html     # To decode HTML entitites like &quot;

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0        # Index of the current question
        self.score = 0                  # Tracks user's score
        self.question_list = q_list     # List of Question object
        self.current_question = None    # Holds the current question

    def still_has_questions(self):
        return self.question_number < len(self.question_list)   # Returns True if there are more questions to show


    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)      # Converts HTML entitites into readbale characters
        return f"Q.{self.question_number}: {q_text}"
    

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False