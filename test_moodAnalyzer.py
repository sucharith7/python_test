import pytest
from MoodAnalyzer import MoodAnalyzer
class TestMoodAnalyzer:
	def test_GivenMood_ContainSad_ReturnSad(self):
		moodAnalyzer=MoodAnalyzer()
		mood=moodAnalyzer.analyzeMood("this is sad message")
		assert mood=="SAD"


	def test_GivenMood_ContainedHappy_ReturnHappy(self):
		moodAnalyzer=MoodAnalyzer()
		mood=moodAnalyzer.analyzeMood("this is happy message")
		assert mood=="HAPPY"


	def test_GivenMood_ContaineNone_ReturnHappy(self):
		moodAnalyzer=MoodAnalyzer()
		mood=moodAnalyzer.analyzeMood("None")
		assert mood=="HAPPY"


	def test_GivenMood_ContainedNone_ReturnCustomException(self):
		try:
			moodAnalyzer=MoodAnalyzer()
			mood=moodAnalyzer.analyzeMood(None)
			
		except Exception as exception:
			assert exception.message == "please enter a proper message"