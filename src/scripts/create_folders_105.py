import os

# List of 100 car brands recognized in Europe
car_brands = [
    "Volkswagen", "Renault", "Peugeot", "Ford", "BMW",
    "Mercedes-Benz", "Audi", "Fiat", "Opel", "Skoda",
    "Citroen", "Seat", "Nissan", "Kia", "Hyundai",
    "Dacia", "Toyota", "Mazda", "Mini", "Jaguar",
    "Land Rover", "Porsche", "Tesla", "Ferrari", "Lamborghini",
    "Maserati", "Alfa Romeo", "Volvo", "Subaru", "Bentley",
    "Rolls Royce", "Aston Martin", "Bugatti", "McLaren", "Nissan",
    "Isuzu", "Smart", "Suzu", "Tata", "Saab",
    "Chrysler", "Dodge", "GMC", "Mazda", "Acura",
    "Infiniti", "Mitsubishi", "Geely", "Great Wall", "BYD",
    "Changan", "Rivian", "Lucid", "Polestar", "MG",
    "Honda", "Nissan", "Citroen", "Peugeot", "Fiat",
    "Skoda", "Dacia", "Renault", "Toyota", "Volvo",
    "Seat", "Mazda", "Opel", "Chevrolet", "Kia",
    "Suzuki", "Lexus", "Subaru", "Land Rover", "Jaguar",
    "Porsche", "Mitsubishi", "Chrysler", "Dodge", "Buick",
    "Lincoln", "Ford", "Nissan", "Toyota", "Mazda",
    "Honda", "Chevrolet", "Hyundai", "Volkswagen", "Audi",
    "Bristol", "Alfa Romeo", "Aston Martin", "Ferrari", "Lamborghini",
    "McLaren", "Bugatti", "Pagani", "Koenigsegg", "Noble",
    "Morgan", "TVR", "Caterham", "Lotus", "Smart",
]

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the base directory to the 'src' directory, which is next to the 'scripts' directory
base_directory = os.path.join(script_directory, '..', 'Car_Brands')

# Create base directory if it doesn't exist
if not os.path.exists(base_directory):
    os.makedirs(base_directory)

# Create folders for each car brand
for brand in car_brands:
    brand_folder = os.path.join(base_directory, brand)
    os.makedirs(brand_folder, exist_ok=True)

print(f"Created folders for {len(car_brands)} car brands in '{base_directory}' directory.")
