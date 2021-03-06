from .abc import SlideABC



class MarkdownSlide(SlideABC):


	def __init__(self, quiz, markdown):
		self._markdown = markdown


	def on_enter(self):
		self.Quiz.next_question()


	def data(self):
		return {
			"markdown": self._markdown
		}
