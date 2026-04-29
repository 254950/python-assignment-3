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

#5.1
def check_files():
    print("Checking file...")
    
    if os.path.exists(file_name):
        print(f"File found: {file_name}")
    else:
        print(f"Error: {file_name} not found.")
        return False

    print("\nChecking output folder...")
    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")
    return True

def load_data(filename):
    students = []
    print("\nLoading data...")
    try:
        with open(filename, encoding='utf-8') as z:
            reader = csv.DictReader(z)
            for row in reader:
                students.append(row)
            
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception:
        print("Error: something went wrong while reading the file.")
        return []

def preview_data(students, n=5):
    print("\nFirst 5 rows:")
    print("-" * 30)
    
    for i in range(n):
        s = students[i]
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
    
    print("-" * 30)
if check_files():
    students = load_data(file_name)
    if students:
        preview_data(students)

#5.2
def get_top_students(students, n=10):
    valid_students = []

    for s in students:
        try:
            score = float(s['final_exam_score'])
            valid_students.append(s)
        except ValueError:
            print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
            continue

    sorted_students = sorted(
        valid_students,
        key=lambda x: float(x['final_exam_score']),
        reverse=True
    )

    return sorted_students[:n]

top10 = get_top_students(students)
top5 = get_top_students(students, 5)

print("-" * 30)
print("\nTop 10 Students by Exam Score")
print("-" * 30)
for i in range(len(top10)):
    s = top10[i]
    print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
print("-" * 30)
print("\nTop 5 Students by Exam Score")
print("-" * 30)
for i in range(len(top5)):
    s = top5[i]
    print(f"{i+1}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")
print("-" * 30)

#5.3
def lambda_tasks(students):
    print("-" * 30)
    print("\nLambda / Map / Filter")
    print("-" * 30)

    try:
        top_scorers = list(filter(lambda s: float(s['final_exam_score']) > 95, students))
        print(f"final_exam_score > 95 : {len(top_scorers)}")
    except:
        print("Error in final_exam_score")

    try:
        gpa_values = list(map(lambda s: float(s['GPA']), students))
        print(f"GPA values (first 5): {gpa_values[:5]}")
    except:
        print("Error in GPA")

    try:
        good_assignments = list(filter(lambda s: float(s['assignment_score']) > 90, students))
        print(f"assignment_score > 90 : {len(good_assignments)}")
    except:
        print("Error in assignment_score")

    print("-" * 30)
lambda_tasks(students)

#5.4
print("\nTesting error handling...")
load_data("wrong_file.csv")

#6.1
class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("-" * 30)
        print("\nChecking file...")

        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        print("\nChecking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")
            print("-" * 30)

fm = FileManager(file_name)
fm.check_file()
fm.create_output_folder()

#6.2
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("\nLoading data...")

        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.students.append(row)

            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students

        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            return []

    def preview(self, n=5):
        print("\nFirst 5 rows:")
        print("-" * 30)

        for i in range(n):
            s = self.students[i]
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("-" * 30)

dl = DataLoader(file_name)
students = dl.load()

if students:
    dl.preview()

#6.3
class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        valid_students = []

        for s in self.students:
            try:
                float(s['final_exam_score'])
                valid_students.append(s)
            except ValueError:
                print(f"Warning: could not convert value for student {s['student_id']} — skipping row.")
                continue

        sorted_students = sorted(
            valid_students,
            key=lambda x: float(x['final_exam_score']),
            reverse=True
        )

        top10 = sorted_students[:10]

        self.result = {
            "analysis": "Top 10 Students by Exam Score",
            "total_students": len(self.students),
            "top_10": []
        }

        for i in range(len(top10)):
            s = top10[i]
            self.result["top_10"].append({
                "rank": i + 1,
                "student_id": s['student_id'],
                "country": s['country'],
                "major": s['major'],
                "final_exam_score": float(s['final_exam_score']),
                "GPA": float(s['GPA'])
            })

        return self.result

    def print_results(self):
        print("-" * 60)
        print("\nTop 10 Students by Exam Score")
        print("-" * 60)

        for s in self.result["top_10"]:
            print(f"{s['rank']}. {s['student_id']} | {s['country']} | {s['major']} | Score: {s['final_exam_score']} | GPA: {s['GPA']}")

        print("-" * 60)
        
analyser = DataAnalyser(students)
result = analyser.analyse()
analyser.print_results()

#6.4
class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(self.result, f, indent=4)

            print(f"\nResult saved to {self.output_path}")

        except Exception:
            print("Error: could not save file.")

saver = ResultSaver(result, "output/result.json")
saver.save_json()
print("-" * 40)

#6.5
file_name = "global_university_students_performance_habits_10000.csv"

fm = FileManager(file_name)
if not fm.check_file():
    print("Stopping program.")
    exit()
fm.create_output_folder()

dl = DataLoader(file_name)
dl.load()
dl.preview()

analyser = DataAnalyser(dl.students)
analyser.analyse()
analyser.print_results()

saver = ResultSaver(analyser.result, "output/result.json")
saver.save_json()
