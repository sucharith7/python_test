import pytest
from MoodAnalyzer import MoodAnalyzer
class TestMoodAnalyzer:
	def test_GivenMood_ContainSad_ReturnSad(self):
		moodAnalyzer=MoodAnalyzer()
		mood=moodAnalyzer.analyzeMood("this is sad message")
		assert mood=="SAD"
