#Defining a function

def greet_user():
    """Display a simple greetimg.""" #this is called a docstring, whcih describe what the function does( are enclosed in triple quotes)
    print("Hello!")

greet_user()#the function only has one job print("Hello")

#Passing information to a function
print("\n")

def greet_user(username):
    """Display a simple greetimg.""" #this is called a docstring, whcih describe what the function does( are enclosed in triple quotes)
    print(f"Hello, {username.title()}!")

greet_user('jesse')#the function has the job to passing the username to a function

#Arguments and Parameters

#The variable username in the definition of greet_user() is an example of a "parameter" a piece of information that's passed from a function call to a function

#In this case the argument 'jesse' was passed to the function greet_user(), and the value was assgined to the parameter username

#Note: People sometimes speak of arguments and parameters interchangeably. Don't be surprised if you se the variable sin a function definition referred to as arguments or the variables in a function call referred to as paraimeters.


