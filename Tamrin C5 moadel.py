students = [
    {"name": "Ali", "grades": [18, 19, 17]},
    {"name": "Sara", "grades": [20, 20, 19]},
    {"name": "Reza", "grades": [15, 16, 14]}
]

for s in students:
    avg = sum(s["grades"])/len(s["grades"])
    print(f"{s['name']} معدل: {avg}")

avg_dict = {s["name"]: sum(s["grades"])/len(s["grades"]) for s in students}
print(avg_dict)

max_student = max(avg_dict, key=avg_dict.get)
print(f"دانش آموز با بالاترین معدل: {max_student} - معدل: {avg_dict[max_student]}")
