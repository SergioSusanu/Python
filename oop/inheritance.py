class Animal:
    def __init__(self, age, weight) -> None:
        self.age = age
        self.weight = weight

class Dog(Animal):
    def __init__(self, age, weight, breed) -> None:
        super().__init__(age, weight)
        self.breed = breed

    def request_out(self, location):
        print("I want to go out "+ location)

Bernie = Dog(23,50,"Rotweller")
print(str(Bernie.age), str(Bernie.weight), Bernie.breed)
print(Bernie.request_out("Central Park"))

class A:
    a = "5"

class B(A):
    b = "6"

class C(B):
    d ='7'

b = B()
print(b.a)
print(issubclass(B,A))

c = C()
print(issubclass(C,A))
print(isinstance(c,A))