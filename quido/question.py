import abc
import hashlib
from .answer import Answer



class QuestionABC(abc.ABC):
	SEQ=0

	def __init__(self, markdown: str):
		self.Markdown = markdown
		self.Answers = {}

		self.Id = str(QuestionABC.SEQ)
		QuestionABC.SEQ += 1


	def set_id(self, id):
		self.Id = id
		return self


	def render(self):
		_dict = {}
		_dict["markdown"] = self.Markdown
		return _dict


	def answer(self, user, answer):
		self.Answers[user] = Answer(self, answer, user)


	def render_answers(self):
		return [answer.render() for user, answer in self.Answers.items()]


	@abc.abstractmethod
	def evaluate_answer(self, answer):
		raise NotImplemented()



class Question(QuestionABC):


	def evaluate_answer(self, answer):
		return True



class OptionsQuestion(QuestionABC):


	def __init__(self, markdown: str, options: list, correct: str):
		super().__init__(markdown)
		self._options = options
		self._correct = correct


	def evaluate_answer(self, answer):
		return answer == self._correct 


	def to_dict(self):
		_dict = super().to_dict()
		_dict["options"] = self._options
		return _dict
