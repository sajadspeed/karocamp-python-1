from delivery import BikeDelivery, CarDelivery

deliveries = [
    BikeDelivery("Tehran"),
    CarDelivery("Karaj"),
]

for delivery in deliveries:
    delivery.start()
    print("Status:", delivery.get_status())
    print("Estimated time:", delivery.calculate_time(), "minutes")
