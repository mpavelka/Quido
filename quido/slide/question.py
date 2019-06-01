from .abc import SlideABC
from ..question import OptionsQuestion

class QuestionSlide(SlideABC):

	def on_enter(self):
		self.Quiz.next_question()


	def data(self):
		question = self.Quiz.CurrentQuestion
		return question.render()
