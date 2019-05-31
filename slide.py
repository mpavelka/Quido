import abc
import hashlib


class SlideABC(abc.ABC):
	SEQ=0

	def __init__(self, quiz, id=None):
		if id is None:
			id = str(QuestionABC.SEQ)
			SlideABC.SEQ += 1

		self.Quiz = quiz


	def on_enter(self):
		pass


	def on_exit(self):
		pass



class QuestionSlide(SlideABC):

	def on_enter(self):
		self.Quiz.next_question()



class OptionsQuestion(SlideABC):

	def __init__(self, markdown: str, options: list, correct: int):
		super().__init__(markdown)

	def evaluate_answer(self, answer):
		return True

