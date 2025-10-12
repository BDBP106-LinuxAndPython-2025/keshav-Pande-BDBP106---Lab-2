studentmarks = {
    "Rahul": {49, 58, 35, 64},
    "Keshav": {80, 92, 94, 83},
    "Sita": {44, 65, 76, 54}
}

print("Students who scored above 60 in all subjects:")
for name, marks in studentmarks.items():
    if all(mark > 60 for mark in marks):
        print(name)
