import csv

def read_scores_from_csv(filename):
    """CSV에서 (name, [scores...]) 튜플 리스트를 반환"""
    students = []
    with open(filename, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            scores = []
            i = 1
            while True:
                key = f"score{i}"
                if key not in row or not row[key]:
                    break
                scores.append(int(row[key]))
                i += 1
            students.append((name, scores))
    return students
