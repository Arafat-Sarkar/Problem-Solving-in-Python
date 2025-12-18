n = int(input())
students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# unique + sort
grades = sorted(set([s[1] for s in students]))

# second lowest grade
second_lowest = grades[1]

# grade second lowest
names = [s[0] for s in students if s[1] == second_lowest]

# alphabetically sort print
for name in sorted(names):
    print(name)
