from models import Doctor, Human, SoftwareEngineer


engineer = SoftwareEngineer(name="Alice", age=28, programming_language="Python")
surgeon = Doctor(name="Dr. Bob", age=42, specialization="Cardiology")

staffs = [engineer, surgeon]


for h in staffs:
    print(f"\n--- Professional Profile: {h.name} ---")
    h.speak()
    h.perform_duty()
    print(f"Current Energy Level: {h.get_energy()}%")
