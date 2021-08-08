class Car:
  def __init__(self, seats, kms):
    self.kms = kms
    self.seats = seats

  def drive(self, distance):
    if not isinstance(distance, int) and not isinstance(distance, float):
      raise TypeError("The distance should be a positive number")

    if distance < 0:
      raise ValueError("Please provide a positive distance")

    self.kms += distance

  def recline_seats(self):
    for seat in self.seats:
      try:
        seat.recline()
      except ValueError:
        continue

  def show_seats(self):
    [print(seat) for seat in self.seats]

class CarSeat:
  def __init__(self, material, reclined=False):
    self.reclined = reclined
    self.material = material

  def __str__(self):
    return f"I'm a {'reclined' if self.reclined else 'non-reclined'} seat. I was made with {self.material}."

  def recline(self):
    if self.reclined:
      raise ValueError("The seat is already reclined. Do you want to broke it?")
    self.reclined = True

  def back_to_initial_position(self):
    if not self.reclined:
      raise ValueError("The seat is already in the initial position.")
    self.reclined = False

seats = [CarSeat("leather") for i in range(4)]
my_lambo = Car(seats, 0)
print(f"Current km traveled: {my_lambo.kms}.")
my_lambo.drive(500)
print(f"Current km traveled: {my_lambo.kms}.")

seats = [CarSeat("cotton" if i % 2 else "synthetics") for i in range(7)]
my_bus = Car(seats, 1000)
my_bus.show_seats()

print("\n---------------\n")

my_bus.recline_seats()
my_bus.show_seats()