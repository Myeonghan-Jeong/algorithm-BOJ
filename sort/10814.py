# 10814 / sort people with ASC age, order of register
N = int(input())
people = [[]] * N
for n in range(N):
    age, name = input().split()
    people[n] = [int(age), name, n]

people.sort(key=lambda p: (p[0], p[2]))
for person in people:
    print(person[0], person[1])
