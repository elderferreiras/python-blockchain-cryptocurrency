persons = [
    {
        'name': 'Zach',
        'age': 33,
        'hobbies': [
            'reading',
            'writing',
        ],
    },
    {
        'name': 'Elder',
        'age': 29,
        'hobbies': [
            'reading',
            'writing',
            'photography',
        ],
    },
    {
        'name': 'Rosalia',
        'age': 0.2,
        'hobbies': [
            'chewing',
        ],
    },
]

print(persons)
print([person['name'] for person in persons])
print(all([person['age'] > 20 for person in persons]))

copied_persons = persons[:]
copied_persons[0]['name'] = 'Zachary'
print(copied_persons)

p1, p2, p3 = persons

print(p1)
print(p2)
print(p3)
