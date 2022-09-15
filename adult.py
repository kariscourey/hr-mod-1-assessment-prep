class Adult:
    def __init__(self, name, age):  # these are the values that we want every instance created with this class to have
        self.name = name
        self.age = age
        self.weight = 200

    def speak(self):
        message = f"Hello, I am {self.name}, how are you?"
        return message

    def make_a_meal(self):
        message = f"{self.name} is cooking a wonderful meal"
        return message
