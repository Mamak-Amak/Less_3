

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asphalt_mass(self, weight = 25, thickness = 5):
        return f"{self._length} m  * {self._width} m * {weight} кг {thickness} см =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.asphalt_mass())




