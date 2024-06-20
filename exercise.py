# CREATE A CLASS CARS WITH THE FOLLOWING ATTRIBUTES
# MODEL, YEAR OF MANUFACTURE, TYPE, COLOR
# CREATE A METHOD TO PRINT
# "MY DREAM CAR IS...MANUFACTURED IN.... BEING A...TYPE, IN COLOR .... "
# INITIALIZE WITH AT LEAST 5 OBJECTS
class Cars:
    def __init__(self, model, yom, type, color):
        self.model = model
        self.yom = yom
        self.type = type
        self.color = color

    def display(self):
        print(
            "My dream car is a" + self.model + ' manufactured in ' + self.yom + " of brand " + self.type + " and color " + self.color)


my_car = Cars(' Mercedes', ' 2019', ' AMG', ' Navy blue')
my_car.display()
my_car1 = Cars(' Ford', ' 2023', ' Raptor', ' White')
my_car1.display()
my_car2 = Cars(' Ford', ' 2024', ' Mustang', ' Red')
my_car2.display()
my_car3 = Cars(' Porsche', ' 2019', ' Cayenne', ' Black')
my_car3.display()
my_car4 = Cars(' Mercedes', ' 2019', ' AMG', ' Navy blue')
my_car4.display()
my_car5 = Cars(' Mercedes', ' 2019', ' AMG', ' Navy blue')
my_car5.display()
