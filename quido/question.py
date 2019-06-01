import abc
import hashlib



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


	def to_dict(self):
		_dict = {}
		_dict["markdown"] = self.Markdown
		return _dict


	def add_answer(self, user, answer):
		self.Answers[user] = answer


	@abc.abstractmethod
	def evaluate_answer(self, answer):
		raise NotImplemented()



class Question(QuestionABC):


	def evaluate_answer(self, answer):
		return True



class OptionsQuestion(QuestionABC):


	def __init__(self, markdown: str, options: list, correct: int):
		super().__init__(markdown)
		self._options = options
		self._correct = correct


	def evaluate_answer(self, answer):
		return answer == self._correct 


	def to_dict(self):
		_dict = super().to_dict()
		_dict["options"] = self._options
		return _dict
