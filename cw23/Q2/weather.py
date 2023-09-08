from abc import ABC, abstractmethod


class Display(ABC):
    @abstractmethod
    def update(self, temperature, humidity):
        pass


class Station(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    @abstractmethod
    def notify_observer(self, observer):
        pass

    @abstractmethod
    def set_measurements(self, temperature, humidity):
        pass


class WeatherStation(Station):
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity)

    def set_measurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify_observers()


class TemperatureDisplay(Display):
    def update(self, temperature, humidity):
        print(f"Temperature Display: {temperature}")


class HumidityDisplay(Display):
    def update(self, temperature, humidity):
        print(f"Humidity Display: {humidity}")


weather_station = WeatherStation()

temperature_display = TemperatureDisplay()
humidity_display = HumidityDisplay()

weather_station.add_observer(temperature_display)
weather_station.add_observer(humidity_display)

weather_station.set_measurements(25, 60)
