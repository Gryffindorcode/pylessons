people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclow"},
    {"name": "Harry", "house": "Slytherin"},
]


def f(person):
    return person["name"]


people.sort(key=f)

print(people)
