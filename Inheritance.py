class Inheritance:
    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)
    def play(self):
        return "{} can play Cricket".format(self.name)

# instantiate the object
blu = Inheritance("Blu", 10)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())
print(blu.play())
