import os
from quido import Quiz, Question, OptionsQuestion, QuestionSlide

quiz = Quiz()
quiz.add_questions([
	Question("What is your name?"),
	OptionsQuestion("What is your name???",
		options=[
			"First is correct",
			"Incorrect",
			"Incorrect2",
		],
		correct=0, # default
	),
	OptionsQuestion("Are you correct?",
		options=[
			"Correct1",
			"Incorrect",
			"Correct2",
		],
		correct=[0,2],
	),
])

quiz.add_slides([
	QuestionSlide(quiz),
	QuestionSlide(quiz),
	QuestionSlide(quiz),
])


while quiz.next_slide():
	print(quiz.CurrentSlide.render())
