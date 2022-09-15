from preteen import Preteen
from adult import Adult

class Child(Preteen):
    # def __init__(self, height):
    #     self.height = height
        # returns child __init__ takes 2 positional arguments but 3 were given
        # no longer accessing child init; accessing adult init
    def __init__(self, name, age, height, money):
        super().__init__(name, age, money)  # acessing init method from adult
        # usig super to give it to adult
        # give you acess to methods on the parent
        self.height = height

    def swing(self):
        return f"{self.name} is swinging"

    def speak(self):
        return "Stranger danger!"

class Baby(Adult):
    pass


evelyn = Child("evelyn", 4, 77, 100)
print(evelyn.play_video_game())
print(evelyn.weight)
print(evelyn.height)
print(evelyn.swing())
print(evelyn.speak())  # overrides inherited .speak()

da_baby = Baby("baby", 0)
print(da_baby.speak())
