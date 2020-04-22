import pytest
from MoodAnalyzer1 import MoodAnalyzerr
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
		moodAnalyzerr= moodAnalyzerFactory.createObject("i am in happy mood")
		mood=moodAnalyzerr.analyzeMood()
		assert mood == "HAPPY"


	def givenMoodAnalyzerclass_whenProper_shouldReturnObject():
		#moodAnalyzerFactory=MoodAnalyzerFactory()
		Moodanalyzerx= MoodAnalyzerFactory.createMoodAnalyzer("i am in happy mood")
		Moodanalyzery=MoodAnalyzerr("i am in happy mood")
		assert Moodanalyzerx==Moodanalyzery


	def test_givenNone_thencalled_defaultConstructor_ReturnObject(self):
		MoodAnalyzerx= MoodAnalyzerFactory.createMoodAnalyzer()
		MoodAnalyzery=MoodAnalyzerr()
		assert MoodAnalyzerx == MoodAnalyzery
