from MoodAnalyzer1 import MoodAnalyzer1
class MoodAnalyzerFactory:
	def createObject(self,message):
		myObject=MoodAnalyzer1(message)
		return myObject


	@staticmethod
	def createMoodAnalyzer(message):
		moodAnalyzer1=MoodAnalyzer1(message)
		return moodAnalyzer1


	@staticmethod
	def createMoodAnalyzer(message=None):
		moodAnalyzer1=MoodAnalyzer1(message)
		return moodAnalyzer1