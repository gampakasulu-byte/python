
students = [
    {
        "name": "Ravi",
        "marks": [85, 90, 80],
        "attendance": 90,
        "income": 200000
    },
    {
        "name": "Sita",
        "marks": [90, 85, 95],
        "attendance": 95,
        "income": 180000
    },
    {
        "name": "Rahul",
        "marks": [70, 80, 75],
        "attendance": 80,
        "income": 220000
    },
    {
        "name": "Priya",
        "marks": [85, 85, 85],
        "attendance": 90,
        "income": 150000
    }
]

eligible = []

for student in students:
    aggregate = sum(student["marks"]) / len(student["marks"])

    if (aggregate >= 75 and
        min(student["marks"]) >= 60 and
        student["attendance"] >= 75 and
        student["income"] <= 250000):

        eligible.append({
            "name": student["name"],
            "aggregate": aggregate,
            "attendance": student["attendance"],
            "income": student["income"]
        })

# Ranking and tie-breaking rules
eligible.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        x["income"],
        x["name"]
    )
)

print("Eligible Scholarship Students:")
for rank, student in enumerate(eligible, 1):
    print(
        rank, student["name"],
        "Aggregate:", student["aggregate"],
        "Attendance:", student["attendance"],
        "Income:", student["income"]
    )
