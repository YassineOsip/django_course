class Car:
    length = 15
    width = 8
    color = "red"
    volume = length * width * length
    mark = "BMW"
    def printVolume():
        print(Car.volume)



print(Car.color)
Car.printVolume()