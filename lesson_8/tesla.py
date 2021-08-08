class Vehicle:
    """Tesla Vehicle representation"""
    # Is it ok or should i use VALID_ENGINES?
    valid_engines = ['electric', 'diesel', 'gas', 'hybrid']

    def __init__(self, color, price, engine, number_of_wheels=4):
        self._color = color
        self._price = price
        self.set_engine(engine)
        self._number_of_wheels = number_of_wheels

    def get_color(self):
        """Returns the 'private' attribute color."""
        return self._color

    def get_price(self):
        """Returns the 'private' attribute price."""
        return self._price

    def set_engine(self, new_engine):
        """Set a new engine, checking that it's valid.."""
        if new_engine not in Vehicle.valid_engines:
            raise ValueError(f"The engine should be one of the following values: {', '.join(Vehicle.valid_engines)}.")
        self._engine = new_engine

    def update_price(self, new_price):
        """Set a new price, checking that it's valid.."""
        if not isinstance(new_price, float) and not isinstance(new_price, int):
            raise TypeError("The price should be a float.")

        if new_price < 0:
            raise ValueError("The price should be a positive number.")

        self._price = new_price


class ElectricCar(Vehicle):
    """Tesla Electric Car representation."""

    def __init__(self, color, price, dist_range):
        super().__init__(color, price, "electric")
        self._dist_range = dist_range

    def get_dist_range(self):
        """Returns the current dist range."""
        return self._dist_range

    def update_dist_range(self, new_dist_range):
        """Charging the car with new range in km that this car can travel."""
        if not isinstance(new_dist_range, float) and not isinstance(new_dist_range, int):
            raise TypeError("The dist range should be a float.")

        if new_dist_range < 0:
            raise ValueError("The dist range should be a positive number.")

        self._dist_range = new_dist_range

    def is_journey_possible(self, journey_dist_range):
        """Returns whether the car can make the journey with the given range depending on the current charge/range."""
        if not isinstance(journey_dist_range, float) and not isinstance(journey_dist_range, int):
            raise TypeError("The journey dist range should be a float.")

        if journey_dist_range < 0:
            raise ValueError("The journey dist range should be a positive number.")

        return self._dist_range >= journey_dist_range


class HybridCar(Vehicle):
    """Tesla Hybrid Car representation."""

    def __init__(self, color, price, fuel_level):
        super().__init__(color, price, "hybrid")
        self._fuel_level = fuel_level

    def get_fuel_level(self):
        """Returns the current fuel level."""
        return self._fuel_level

    def refuel(self):
        """Fills the gas tank to 100%."""
        self._fuel_level = 100


def car_tests():
    """Tests behaviour of the Vehicle class."""
    car = Vehicle(color='red', price=12000, engine='gas', number_of_wheels=6)
    assert car.get_color() == 'red'
    assert car.get_price() == 12000
    car.update_price(10000)
    assert car.get_price() == 10000


def electric_tests():
    """Tests behaviour of the ElectricCar class."""
    electric = ElectricCar(color='green', price=13000, dist_range=350)
    assert electric.get_dist_range() == 350
    assert electric.is_journey_possible(300)

    electric.update_dist_range(250)
    assert electric.get_dist_range() == 250
    assert not electric.is_journey_possible(300)


def hybrid_tests():
    """Tests behaviour of the HybridCar class."""
    hybrid = HybridCar(color='blue', price=14000, fuel_level=80)
    assert hybrid.get_fuel_level() == 80
    hybrid.refuel()
    assert hybrid.get_fuel_level() == 100


def main():
    """Main function that runs some tests."""
    car_tests()
    electric_tests()
    hybrid_tests()
    print("All tests passed!")


if __name__ == "__main__":
    main()
