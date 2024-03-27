cars = {"uaz", "toyota", "honda", "lada", "changan"}
sorted_cars = sorted(cars)
print(sorted_cars)
sorted_cars = sorted(cars, key=lambda x: False if 'n' in x else True)
print(sorted_cars)

print("=============================================================")

people = [
    {"name": "John", "age": 30, "sex": "male"},
    {"name": "Kate", "age": 20, "sex": "female"},
    {"name": "Nick", "age": 41, "sex": "male"},
    {"name": "Adam", "age": 41, "sex": "male"},
    {"name": "Luda", "age": 34, "sex": "female"},
]
print(people)
sorted_people = sorted(people, key=lambda x: (x["age"], x["name"]))
print(sorted_people)

print("=============================================================")

filtered_people = list(filter(lambda x: x["age"] > 30, people))
print(filtered_people)

print("=============================================================")
