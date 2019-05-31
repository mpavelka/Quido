from .question import Question


class Quiz(object):
	
	def __init__(self):

		self.Slides = []
		self.CurrentSlide = None
		self._current_slide_index = -1

		self.Questions = []
		self.CurrentQuestion = None
		self._current_question_index = -1


	def add_question(self, question):
		self.Questions.append(question)


	def add_questions(self, questions):
		for question in questions:
			self.add_question(question)


	def next_question(self):
		# No questions at all
		if len(self.Questions) == 0:
			return False

		# No more questions
		if self._current_question_index + 1 == len(self.Questions):
			self.CurrentQuestion = None
			self._current_question_index = -1
			return False

		# Next question
		self._current_question_index += 1
		self.CurrentQuestion = self.Questions[self._current_question_index]
		return True


	def add_slide(self, slide):
		self.Slides.append(slide)


	def add_slides(self, slides):
		for slide in slides:
			self.add_slide(slide)


	def next_slide(self):
		# Exit previous slide
		if self.CurrentSlide is not None:
			self.CurrentSlide.on_exit()

		# No slides at all
		if len(self.Slides) == 0:
			return False

		# No more slides
		if self._current_slide_index + 1 == len(self.Slides):
			self.CurrentSlide = None
			self._current_slide_index = -1
			return False

		# Next slide
		self._current_slide_index += 1
		self.CurrentSlide = self.Slides[self._current_slide_index]
		# Run slide's on_enter
		self.CurrentSlide.on_enter()
		return True






