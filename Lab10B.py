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
        def renamed(self, newName):
            self.name = newName
        def eat(self, food):
            self.weight = self.weight + food
    def dogDesc(age, weight, name, furColor, breed):
        print(f"{name} is a {age} year old {furColor} {breed} that weighs {weight} lbs.")
    print("You are about to create a dog.")
    age = int(input("How old is the dog: "))
    weight = float(input("How much does the dog weigh: "))
    name = input("What is the dog's name: ")
    furColor = input("What color is the dog: ")
    breed = input("What breed is the dog: ")
    dog1 = Dog(age, weight, name, furColor, breed)
    dogDesc(dog1.age, dog1.weight, dog1.name, dog1.furColor, dog1.breed)
    dog1.bark()
    food = float(input(f"{dog1.name} is hungry, how much should he eat: "))
    newName = input(f"{dog1.name} isn't a very good name. What should they be renamed to: ")
    dog1.eat(food)
    dog1.renamed(newName)
    dogDesc(dog1.age, dog1.weight, dog1.name, dog1.furColor, dog1.breed)

if __name__ == "__main__":
    main()