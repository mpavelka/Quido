import os
from quido import Quiz, Question, OptionsQuestion

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

exit(1)

quiz.add_slide(
	MarkdownSlide(
		quiz,
		path=os.path.join(os.path.dirname(__file__), "var", "markdown", "01_welcome.md"),
	)
)
quiz.add_slide(
	QuestionSlide(quiz)
)
quiz.add_slide(
	StatisticsSlide(quiz)
)
quiz.add_slide(
	QuestionSlide(
		quiz,
		OptionsQuestion("What is your name?",
			options=[
				"First is correct",
				"Incorrect",
				"Incorrect2",
			]
		)
	)
)
quiz.add_slide(
	QuestionSlide(
		quiz,
		
	)
)
quiz.add_slide(
	StatisticsSlide(
		quiz,
		question_id="Q_ARE_YOU_CORRECT"
	)
)


# Start quiz
quiz.reset()

quiz.set_answer()
quiz.next_slide()
quiz.get_current_slide()
quiz.set_slide(1)
quiz.set_slide(id="dfa")

quiz.answer_current(user, 1)
quiz.answer(question_id="Q_ARE_YOU_CORRECT", user=user, answer=1)














