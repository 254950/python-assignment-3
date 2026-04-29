import os
import csv
import json

#4.1
print('Checking file...')
file_name = 'global_university_students_performance_habits_10000.csv'
folder_name = 'output'

if os.path.exists(file_name):
    print(f'File found: {file_name}')
else:
    print(f'Error: {file_name} not found. Please download the file from LMS.')


print('Checking output folder...')
if os.path.exists(folder_name):
    print('folder exists')
else:
    os.makedirs(folder_name)
    print('Output folder created: output/')

#4.2
students = []

with open(file_name, encoding='UTF-8') as z:
    reader = csv.DictReader(z)

    for row in reader:
        students.append(row)

print(f"\nTotal students: {len(students)}")
print("First 5 rows:")
print("-" * 30)

for i in range(5):
    s = students[i]
    
    print(f'{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA : {s['GPA']}')
print("-" * 30)

#4.3
print("\n-------------------------------")
print("Top 10 Students by Exam Score")
print("-" * 30)

top10 = sorted(
    students,
    key=lambda x: float(x['final_exam_score']),
    reverse=True
)[:10]

for i in range(len(top10)):
    s = top10[i]
    print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")

print("-" * 30)

#4.4
print("\n===============================")
print("ANALYSIS RESULT")
print("=" * 30)

result = {
    "analysis": "Top 10 Students by Exam Score",
    "total_students": len(students),
    "top_10": []
}

for i in range(len(top10)):
    s = top10[i]
    result["top_10"].append({
        "rank": i + 1,
        "student_id": s["student_id"],
        "country": s["country"],
        "major": s["major"],
        "final_exam_score": float(s["final_exam_score"]),
        "GPA": float(s["GPA"])
    })

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4)

print(f"Analysis : {result['analysis']}")
print(f"Total students : {result['total_students']}")
print("Top 10 saved to output/result.json")
print("=" * 30)
print("Result saved to output/result.json")
