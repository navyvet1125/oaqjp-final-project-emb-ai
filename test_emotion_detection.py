""" This file contains the test cases for the emotion detection module."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        """ This function tests the emotion_detector function in the emotion_detector module"""
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], 'joy')
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], 'anger')
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], 'disgust')
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], 'sadness')
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], 'fear')
        self.assertEqual(emotion_detector(''), '<b>Invalid text! Please try again!</b>')


unittest.main()
