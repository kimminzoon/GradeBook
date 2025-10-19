class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        return sum(self.scores) / len(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


class GradeBook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        return sum(s.average() for s in self.students) / len(self.students)


def main():
    gb = GradeBook()
    gb.add_student(Student("Alice", [90, 85, 92]))
    gb.add_student(Student("Bob", [70, 75, 68]))

    print("전체 반 평균:", gb.class_average())
    for s in gb.students:
        print(f"{s.name} 평균: {s.average():.1f}, 학점: {s.grade()}")


if __name__ == "__main__":
    main()
