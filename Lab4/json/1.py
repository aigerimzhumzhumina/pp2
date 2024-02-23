import json

with open("C:/Users/Пользователь/Documents/pp2/Lab4/json/car.json", "r") as file:
    car_data = json.load(file)


print("Car Details")
print("=" * 80)

print("{:<20} {:<20} {:<20}".format("Make", "Model", "Color"))
print("-" * 20, "-" * 20, "-" * 20)

make = car_data.get('make', '')
model = car_data.get('model', '')
color = car_data.get('color', '')

print("{:<20} {:<20} {:<20}".format(make, model, color))
