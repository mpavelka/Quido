from .question import Question


class Quiz(object):
	
	def __init__(self):

		self.Slides = []
		self.CurrentSlide = None
		self._current_slide_index = None

		self.Questions = []
		self.CurrentQuestion = None
		self._current_question_index = None


	def add_question(self, question):
		self.Questions.append(question)

		# If this is first question, make it current
		if len(self.Questions) == 1:
			self.CurrentQuestion = question
			self._current_question_index = 0


	def add_questions(self, questions):
		for question in questions:
			self.add_question(question)


	def add_slide(self, slide):
		self.Slides.append(slide)

		# If this is the first slide, make it current
		if len(self.Slides) == 1:
			self.CurrentSlide = slide
			self._current_slide_index = 0


	def add_slides(self, sli):
		for question in questions:
			self.add_question(question)






