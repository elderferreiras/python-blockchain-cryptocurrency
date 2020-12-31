from vehicle import Vehicle


class Car(Vehicle):
    def brag(self):
        print('Look how cool my car is!')


car1 = Car()
car1.drive()

car2 = Car(starting_top_speed=23)
car2.drive()
print(car2)

car3 = Car(1)
car3.drive()
