def greet(name):
    return f"안녕하세요, {name}님!"

def calculate_total(scores):
    return sum(scores)

def print_summary(name, scores):
    total = calculate_total(scores)
    avg = total / len(scores)
    print(f"{name}님의 총점: {total}, 평균: {avg:.1f}")

if __name__ == "__main__":
    name = "Alice"
    scores = [90, 85, 92]
    print(greet(name))
    print_summary(name, scores)
