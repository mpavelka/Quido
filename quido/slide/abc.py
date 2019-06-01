import abc
import hashlib


class SlideABC(abc.ABC):
	SEQ=0

	def __init__(self, quiz):
		self.Quiz = quiz

		self.Id = str(SlideABC.SEQ)
		SlideABC.SEQ += 1


	def set_id(self, id):
		self.Id = id
		return self


	def on_enter(self):
		pass


	def on_exit(self):
		pass


	def render(self):
		return {
			"type": type(self).__name__,
			"data": self.to_dict()
		}


	@abc.abstractmethod
	def to_dict(self):
		raise NotImplemented()
