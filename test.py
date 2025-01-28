class Dog:
  def __init__(self, name, breed):
    self.name = name
    self.breed = breed

  def bark(self):
    print("Woof!")

my_dog = Dog("Buddy", "Labrador")
print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Labrador
my_dog.bark()  # Output: Woof!