from CustomException import CustomException
class MoodAnalyzer1:
	def __init__(self,message=None):
		self.message=message

	def analyzeMood(self,message=None):
		try:
			if message == None:
				message = self.message

			if message.__contains__("sad"):
				return "SAD"
			else:
				return "HAPPY"

		except Exception as exception:
			raise CustomException("please enter proper message")


	def __eq__(self,other):
		return self.message == other.message