import abc
import hashlib


class QuestionABC(abc.ABC):
	SEQ=0

	def __init__(self, markdown: str, id=None):
		if id is None:
			id = str(QuestionABC.SEQ)
			QuestionABC.SEQ += 1
		self.Id = id
		self.Markdown = markdown

		print(self.Id)

	@abc.abstractmethod
	def evaluate_answer(self, answer):
		raise NotImplemented()



class Question(QuestionABC):

	def evaluate_answer(self, answer):
		return True



class OptionsQuestion(QuestionABC):

	def __init__(self, markdown: str, options: list, correct: int):
		super().__init__(markdown)

	def evaluate_answer(self, answer):
		return True

