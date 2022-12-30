class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname#con init asigno los elementos a los atributos

  def printname(self):
    print(self.firstname, self.lastname)



x = Person("John", "Doe")#creo el elemento y llamo al metodo
x.printname()



class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year#constructor del padre y el nuevo atributo

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()



