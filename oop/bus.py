from vehicle import Vehicle


class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(500)
bus1.add_group(['Elder', 'Zach', 'Rosalia'])
print(bus1.__dict__)