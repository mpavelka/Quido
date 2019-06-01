class Answer(object):

	def __init__(self, question, answer, user=None):
		self.Question = question
		self.Answer = answer
		self.User = user

	def render(self):
		return {
			"question_id": self.Question.Id,
			"answer": self.Answer,
			"user": str(self.User),
			"correct": self.Question.evaluate_answer(self.Answer)
		}
