from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name: str, power_watt: float):
        self.name = name
        self.power_watt = power_watt
        
        self._is_on = False
        self.__logs = []

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass

    def _add_log(self, action: str):
        self.__logs.append(action)

    def get_logs(self) -> list[str]:
        return self.__logs.copy()

    def get_status(self) -> str:
        state = "ON" if self._is_on else "OFF"
        return f"Device: {self.name} | Power: {self.power_watt}W | Status: {state}"


class SmartLight(SmartDevice):
    def __init__(self, name: str, power_watt: float, brightness: int = 100):
        super().__init__(name, power_watt)
        self.brightness = brightness

    def turn_on(self) -> None:
        self._is_on = True
        self._add_log("Turned ON")
        print(f"Smart Light '{self.name}' turned on at {self.brightness}% brightness.")

    def turn_off(self) -> None:
        self._is_on = False
        self._add_log("Turned OFF")
        print(f"Smart Light '{self.name}' turned off.")

    def set_brightness(self, level: int) -> None:
        if 0 <= level <= 100:
            self.brightness = level
            print(f"Smart Light '{self.name}' brightness set to {level}%.")


class SmartThermostat(SmartDevice):
    def __init__(self, name: str, power_watt: float, target_temp: float = 22.0):
        super().__init__(name, power_watt)
        self.target_temp = target_temp

    def turn_on(self) -> None:
        self._is_on = True
        self._add_log("Turned ON")
        print(f"Thermostat '{self.name}' activated. Target Temperature: {self.target_temp}°C.")

    def turn_off(self) -> None:
        self._is_on = False
        self._add_log("Turned OFF")
        print(f"Thermostat '{self.name}' deactivated.")

    def set_temperature(self, new_temp: float) -> None:
        if self._is_on:
            self.target_temp = new_temp
            print(f"Thermostat '{self.name}' temperature updated to {new_temp}°C.")
        else:
            print(f"Cannot adjust '{self.name}': device is OFF.")
