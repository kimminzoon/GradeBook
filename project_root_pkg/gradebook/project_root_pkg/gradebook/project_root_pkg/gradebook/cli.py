import argparse
from .models import Student, GradeBook
from .io.csvio import read_scores_from_csv

def run_default():
    gb = GradeBook()
    gb.add_student(Student("Alice", [90, 85, 92]))
    gb.add_student(Student("Bob", [70, 75, 68]))

    print("전체 반 평균 점수:", round(gb.class_average(), 2))
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

def run_with_csv(csv_path: str):
    gb = GradeBook()
    for name, scores in read_scores_from_csv(csv_path):
        gb.add_student(Student(name, scores))

    print("전체 반 평균 점수:", round(gb.class_average(), 2))
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

def main():
    parser = argparse.ArgumentParser(description="GradeBook CLI")
    parser.add_argument("--csv", type=str, help="성적 CSV 파일 경로 (예: scores.csv)")
    args = parser.parse_args()

    if args.csv:
        run_with_csv(args.csv)
    else:
        run_default()
