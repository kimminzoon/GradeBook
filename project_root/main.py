from models import Student, GradeBook

def main():
    gb = GradeBook()
    gb.add_student(Student("Alice", [90, 85, 92]))
    gb.add_student(Student("Bob", [70, 75, 68]))

    print("전체 반 평균 점수:", round(gb.class_average(), 2))
    for s in gb.students:
        print(f"{s.name} - 평균: {s.average():.1f}, 학점: {s.grade()}")

if __name__ == "__main__":
    main()
