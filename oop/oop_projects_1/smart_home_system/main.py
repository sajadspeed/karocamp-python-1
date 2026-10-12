from models import SmartDevice, SmartLight, SmartThermostat


living_room_light = SmartLight(name="Living Room Lamp", power_watt=15.0, brightness=80)
hall_thermostat = SmartThermostat(name="Main Hall Thermostat", power_watt=1200.0, target_temp=21.5)

home_devices = [living_room_light, hall_thermostat]
print("=== Smart Home Evening Routine ===")
for device in home_devices:
    device.turn_on()
    print(device.get_status())
    print("-" * 35)
