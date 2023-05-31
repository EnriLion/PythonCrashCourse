#Testing a class

##A Variety of Assert Methods
#Python provies an assert method in the unittest.TestCase class(whether a condition you belive is true at a specific point in your code is indeed true).With these mthod we can verify if the values are True or False we can use these mehods only in a class that inherits from unittest.TestCase, so let's look at how we can use one of these methods in the context of testing an actual class:

#Assert  Methods Available from the unittest Module
#---------------------------------------------------------
# Method                            Use
#---------------------------------------------------------
# assertEqual(a, b)           Verify that a == b
# assertNotEqual(a, b)        Verify that a != b
# assertTrue(x)               Verify that x is True
# assertFalse(x)              Verify that x is False 
# assertIn(item, list)        Verify that item is in list 
# assertNotIn(item, list)     Verify that item is not in list 
#---------------------------------------------------------

#A class to test

#Testing a class is similar to testing a function. There are a few diference, so let's write a class to test. Consider a class that helps administer anonymous surveys:

class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):# a class that starts with a survey questions you provide and includes an empty list to store responses
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):# add a new response to the list
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):#print all the responses stored in the list
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):#store and show the results 
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


