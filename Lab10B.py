def main():
    class Dog:
        def __init__(self, age, weight, name, furColor, breed):
            self.age = age
            self.weight = weight
            self.name = name
            self.furColor = furColor
            self.breed = breed
        def bark(self):
            print("Woof! Woof!")
        def rename(self):
            self.name = input(f"{self.name} isn’t a very good name. What should they be renamed to: ")
        def eat(self):
            self.weight = self.weight + float(input(f"{self.name} is hungry, how much should he eat: "))
        def desc(self):
            print(f"{self.name} is a {self.age} year old {self.furColor} {self.breed} that weighs {self.weight} lbs.")

    print("You are about to create a dog.")
    age = int(input("How old is the dog: "))
    weight = float(input("How much does the dog weigh: "))
    name = input("What is the dog's name: ")
    furColor = input("What color is the dog: ")
    breed = input("What breed is the dog: ")
    dog1 = Dog(age, weight, name, furColor, breed)
    dog1.desc()
    dog1.bark()
    dog1.eat()
    dog1.rename()
    dog1.desc()
if __name__ == "__main__":
    main()