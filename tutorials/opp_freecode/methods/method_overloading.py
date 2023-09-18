class OverloadingDemo:
    def add(self, x, y):
        print(x+y)

    def add(self, x, y, z):
        print(x+y+z)

obj = OverloadingDemo()
# obj.add(2,3) -- python doesn't support method overloading by default
obj.add(2, 3, 5)
