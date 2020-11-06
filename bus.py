from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, starting_top_speed=100):
        super().__init__(starting_top_speed)
        self.passengers = []

    def add_group(self, passengers):
        self.passengers.extend(passengers)

bus1 = Bus(150)
bus1.add_group(['Max', 'Manuel', 'Anna'])
print(bus1.passengers)
bus1.drive()
bus1.add_warning('Over Loaded!')
print(bus1.get_warnings())

bus2 = Bus(250)
print(bus2.passengers)
bus2.drive()
print(bus2.get_warnings())