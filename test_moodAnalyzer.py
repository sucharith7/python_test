import pytest
from MoodAnalyzer1 import MoodAnalyzer1
from MoodAnalyzer import MoodAnalyzer
from CustomException import CustomException
from MoodAnalyzerFactory import MoodAnalyzerFactory
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


	def test_givenMoodAnalyzerclass_whenProper_shouldReturnObject(self):
		moodAnalyzerFactory=MoodAnalyzerFactory() 
		moodAnalyzer1= moodAnalyzerFactory.createObject("i am in happy mood")
		mood=moodAnalyzer1.analyzeMood()
		assert mood == "HAPPY"