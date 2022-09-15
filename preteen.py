from adult import Adult  # if it were .adult, would throw ImportError: attempted relative import with no known parent package

class Preteen(Adult):
    def __init__(self, name, age, money):
        super().__init__(name, age)
        self.money = money

    def play_video_game(self):
        message = f"{self.name} is playing a video game"
        return message


ted = Preteen("ted", 11, 360)
print(ted)
