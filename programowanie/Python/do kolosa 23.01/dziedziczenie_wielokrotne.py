# class A:
#     pass
# class B(A):
#     pass
# class C(A):
#     pass
# class D(B,C):
#     pass 




# class ParentClass:
#     def speak(self):
#         print("Jestem rodzicem")

# class ChildClass(ParentClass):
#     def speak(self):
#         super().speak() # Funckja 'super' sluzy do wywolania z metody bazowej z klasy potomnej
#         print("Jestem dzieckiem")

# child = ChildClass()
# child.speak()




####### Polimorfizm #########

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         return 3.14 * self.radius
    

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height 


#     def calculate_area(self):
#         return self.height * self.width
    

# circle = Circle(5)
# rectangle = Rectangle(4,3)

# def area(shape):
#     return shape.calculate_area()


# print("Pole koła:", area(circle))
# print("Pole prostokąta:", area(rectangle))
# # print(circle.calculate_area())
# # print(rectangle.calculate_area())



# class Animal:
#     def speak(self):
#         pass


# class Dog:
#     def speak(self):
#         print ("Hau!")


# class Cat:
#     def speak(self):
#         print ("Miau!")


# dog = Dog()
# cat = Cat()

# def animal_speak(animal):
#     return animal.speak()

# animal_speak(cat)
# animal_speak(dog)


# from abc import ABC, abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius**2
#     def perimeter(self):
#         return 2 * 3.14 * self.radius
    

# class Rectangle(Shape):
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.height * self.width
#     def perimeter(self):
#         return 2 * (self.width + self.height)
    

# circle = Circle(5)
# rectangle = Rectangle(4,3)

# print("Pole koła: ", circle.area())
# print("Obwód koła: ", circle.perimeter())
# print("Pole prostokąta: ", rectangle.area())
# print("Obówd prostokąta: ", rectangle.perimeter())





############### funkcja str ########

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age} lat"
    
    def __len__(self):
        return len(self.name)

    
person = Person("Wiktor", 30)
print(person)
print(len(person))