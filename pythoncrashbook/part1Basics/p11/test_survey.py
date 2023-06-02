#Testing the AnonymousSurvey Class
##Write a test that verifies one aspect of the way AnonymousSurvey behaves. We'll use the assertIn() method to verify that the respons is in the list of reponses after it's been stored:
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):#we impor the unittest that inherist from the unittes.TestCase
    """Test for the class AnonymousSurvey"""

    def test_store_single_response(self):# A good descriptive name for this method is the_store_single_response() if this thest fails, we'll know from the method name shwon the output of the failing test that there was a problem storing a single repsonse the survey
        """Test for the class AnonymousSurvey"""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)# to thest the behavior we create an instance called my_survey
        # my_survey.store_response('English')
        # self.assertIn('English', my_survey.responses)#adn we verify the repsonse stored correctly by asserting that English in the list my_survey.responses
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

#Let's create another test that we add another method to TestAnonymousSurvey

    def test_store_three_response(self):
        """Test that three individual responses are stored properly."""
        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)
        # responses = ['English', 'Spanish', 'Mandarin']# we define list containing three diferent responses and then we call store_response() for each of the responses
        for response in self.responses:
        #     my_survey.store_response(response)
              self.my_survey.store_response(response)

        for response in self.responses:
        #     my_survey.store_response(response)
              self.assertIn(response, self.my_survey.responses)

        # for response in responses:
        # self.assertIn('English', my_survey.responses)# Once the responses have been stored we write another loop and assert that each response is now in my_survet.responses

#The setUp() Method

#The setup method runs the  method setup() before running other method starting with test_.Any objects created in the setUp() method are then available in each test method you write; we use setUp() to create a surve instance and a set of responses that can be used in test_store_single_response() and test_store_three_response():

    def setUp(self):
        """
        Create a survey and a set of responses for use in al l test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)#creates a survey instance
        self.responses = ['English', 'Spanish', 'Mandarin']#creates a list of reponses  and any of these are prefixed by self(can be used anywhere in the class)

#The method test_store_single_response() verifies that the first response in self.responses - self.reponses[0] can be stored correclty
#The method test_store_three_response() verifies that all three responses in self.responses can be stored correctly

#When a test case is running. Python prints one character for each unit test it is completed a passing test prints a dot, a test that results in an error prints an E, and a test that results in a failed assertion prints an F. This is why you'll see a different number of dots and characters on the first line of the output and maybe take a long time but we can see the result that how many are padding




if __name__ == '__main__':
    unittest.main()

