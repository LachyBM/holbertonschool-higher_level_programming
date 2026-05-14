#!/usr/bin/python3

students =[
        ('Sam',24),
        ('Zac',24),
        ('Sean',23),
        ('Venghour',28),
        ('Lachlan', 28)
        ]

old= list(filter(lambda student: student[1] >= 25, students))
old.sort(key=lambda student: student[1])
print(tuple([student[0] for student in old]))
