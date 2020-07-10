# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base Class
class Vehicle:
    def __init__(self):
        pass

# Sky vehicles
class FlightVehicle:
    def __init__(self):
        super().__init__()

class Airplane:
    def __init__(self):
        super().__init__()

class Starship:
    def __init__(self):
        super().__init__()

# Ground Vehicles
class GroundVehicle:
    def __init__(self):
        super().__init__()

class Car:
    def __init__(self):
        super().__init__()

class Motorcycle:
    def __init__(self):
        super().__init__()
