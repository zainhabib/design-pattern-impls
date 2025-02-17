class Driver:
    def __init__(self, name: str, age:str):
        self.name = name
        self.age = age


class Car:
    def __init__(self, driver: Driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}.")


class CarProxy:
    def __init__(self, driver: Driver):
        self.driver = driver
        self.car = Car(driver)

    def drive(self):
        if self.driver.age >= 16:
            self.car.drive()
        else:
            print("Driver too young.")



def main():
    driver = Driver("John", 20)
    car = CarProxy(driver)
    car.drive()

if __name__ == "__main__":
    main()
