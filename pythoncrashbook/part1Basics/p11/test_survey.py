#Testing the AnonymousSurvey Class
##Write a test that verifies one aspect of the way AnonymousSurvey behaves. We'll use the assertIn() method to verify that the respons is in the list of reponses after it's been stored:
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):#we impor the unittest that inherist from the unittes.TestCase
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):# A good descriptive name for this method is the_store_single_response() if this thest fails, we'll know from the method name shwon the output of the failing test that there was a problem storing a single repsonse the survey
        """Test for the class AnonymousSurvey"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)# to thest the behavior we create an instance called my_survey
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)#adn we verify the repsonse stored correctly by asserting that English in the list my_survey.responses

#Let's create another test that we add another method to TestAnonymousSurvey

    def test_store_three_response(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']# we define list containing three diferent responses and then we call store_response() for each of the responses
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn('English', my_survey.responses)# Once the responses have been stored we write another loop and assert that each response is now in my_survet.responses


if __name__ == '__main__':
    unittest.main()

