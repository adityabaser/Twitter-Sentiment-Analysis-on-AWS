# from TwitterFile import TwitterClass
'''
Assignment 3
'''

# import sys, os
# myPath = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, myPath + '/../')

# print (sys.path)
import unittest
import numpy as np
import twitter_file





# tw = Twitter()
#
# tweet = "NaMo wins the next elections successfully @mc"
#
# cleaned = tw.clean_text(tweet)
#
# tokenized = tw.tokenize_text(cleaned)
#
# replaced = tw.replace_token_with_index(tokenized)
# #
# padded = tw.pad_sequence(replaced)

class TestMyModule(unittest.TestCase):

    """
    Class to test
    """

    def test_clean_text(self):
        """
        Testing clean_text
        """

        twitt = twitter_file.TwitterClass()
        tweet = "Namo www.timesnow.com loses elections @amit"

        result = twitt.clean_text(tweet)

        expected_result = 'namo   loses elections '

        self.assertEqual(result, expected_result)

    def test_tokenize_text(self):
        """
        Testing Tokenized text
        """
        twitt = twitter_file.TwitterClass()
        cleaned_tweet = 'namo   loses elections '

        result = twitt.tokenize_text(cleaned_tweet)

        expected_result = ['namo', 'loses', 'elections']

        self.assertEqual(result, expected_result)
    @staticmethod
    def test_replace_token_with_index():
        """
        Testing replacing
        """
        twitt = twitter_file.TwitterClass()
        token_tweet = ['namo', 'loses', 'elections']

        result = twitt.replace_token_with_index(token_tweet)

        expected_result = [22435, 12334, 17879]

        np.testing.assert_array_equal(result, expected_result)

    @staticmethod
    def test_pad_sequence():
        """
        Testing padded sequence
        """
        twitt = twitter_file.TwitterClass()
        ind_tweet = [22435, 12334, 17879]

        result = twitt.pad_sequence(ind_tweet)

        expected_result = [22435, 12334, 17879, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, \
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


        np.testing.assert_array_equal(result, expected_result)

#
# print (cleaned)
# print (tokenized)
# print (replaced)
# #
# print (padded)
#
# import unittest
#
#
# class TestMyModule(unittest.TestCase):
#
# 	def setUp(self):
# 		return
#
# 	def test_do_divide(self):
#
# 		first_arg = 4
# 		second_arg = 2
#
# 		result = class_example.do_divide(first_arg, second_arg)
#
# 		expected_result = 3
#
# 		self.assertEqual(result, expected_result)
