from vehicles import WaterVehicle, WheeledVehicle, Car


def main():
    vehicles = [
        WaterVehicle("Boat"),
        WheeledVehicle("Bicycle"),
        Car("Sedan", "Toyota")
    ]

    for vehicle in vehicles:
        print(vehicle.move())


if __name__ == "__main__":
    main()
