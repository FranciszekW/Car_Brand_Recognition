import os

# List of 100 car brands recognized in Europe
car_brands = [
    # TODO sort these
    "Acura", "Alfa Romeo", "Aston Martin", "Audi", "BMW",
    "Bentley", "Bugatti", "Buick", "Caterham",
    "Chevrolet", "Chrysler", "Citroen", "Dacia", "Dodge",
    "Ferrari", "Fiat", "Ford", "GMC", "Honda",
    "Hyundai", "Infiniti", "Isuzu", "Jaguar", "Kia",
    "Koenigsegg", "Lamborghini", "Land Rover", "Lexus",
    "Lotus", "Maserati", "Mazda", "McLaren", "Mercedes-Benz",
    "Mini", "Mitsubishi", "Morgan", "Nissan",
    "Opel", "Pagani", "Peugeot", "Porsche", "Renault",
    "Rolls Royce", "Saab", "Seat", "Skoda", "Smart",
    "Subaru", "Suzuki", "Tata",
    "Tesla", "Toyota", "Volkswagen", "Volvo",
]

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the base directory to the 'src' directory, which is next to the 'scripts' directory
base_directory = os.path.join(script_directory, '..', 'data')

# Create base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Create folders for each car brand
for brand in car_brands:
    brand_folder = os.path.join(base_directory, brand)
    os.makedirs(brand_folder, exist_ok=True)

print(f"Created folders for {len(car_brands)} car brands in '{base_directory}' directory.")
