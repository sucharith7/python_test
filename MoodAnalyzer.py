class MoodAnalyzer:
	def analyzeMood(self,message):
		if message.__contains__("sad"):
			return "SAD"
		else:
			return "HAPPY"
