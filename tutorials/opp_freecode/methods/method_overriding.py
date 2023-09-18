class ParentClass:
    def call_me(self):
        print("I am parent class")


class ChildClass(ParentClass):
    def call_me(self):
        print("I am child class")
        super().call_me()
        # we get the class of the parent

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()

# In the above code when the call_me() method was called on the child object, the call_me() from the child class was invoked.

# We can invoke the parent's clas call_me() method from the chidl class using super().
