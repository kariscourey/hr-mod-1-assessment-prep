# print(user_info(name="Crystal", age=25, is_happy=False, is_admin="Of Course"))


"""
Classes
"""



from adult import Adult
from preteen import Preteen



mike = Adult("Mike", 25)
crystal = Adult("Crystal", 24)
kayla = Preteen("Kayla", 12)

print(mike.speak())
print(crystal.speak())
print(crystal.age)
print(crystal.name)
print(crystal.weight)
print(mike.weight)
print(mike.make_a_meal())
print(crystal.make_a_meal())
print(kayla.speak())
print(kayla.make_a_meal())
print(kayla.play_video_game())
# print(mike.play_video_game())
