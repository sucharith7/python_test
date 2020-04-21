from CustomException import CustomException
class MoodAnalyzer:
	def analyzeMood(self,message):
		try:
			if message.__contains__("sad"):
				return "SAD"
			else:
				return "HAPPY"
		except Exception as exception:
			raise CustomException ("please enter a proper message")
