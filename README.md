GradeBook

이 프로젝트는 파이썬으로 만든 성적 관리 프로그램(GradeBook)입니다.
학생들의 점수를 입력받아 평균과 학점을 계산하며,
모듈 구조와 패키지 구조를 단계별로 학습할 수 있는 예제입니다.

프로젝트 구조

GradeBook/
├─ .gitignore
├─ README.md
├─ project_root/
│ ├─ main.py
│ ├─ models.py
│ └─ utils.py
├─ project_root_pkg/
│ ├─ gradebook/
│ │ ├─ init.py
│ │ ├─ main.py
│ │ ├─ cli.py
│ │ ├─ models.py
│ │ ├─ utils.py
│ │ └─ io/
│ │ ├─ init.py
│ │ └─ csvio.py
│ ├─ tests/
│ │ └─ test_utils.py
│ └─ scores.csv

실행 방법

(1) 기본 실행
python -m gradebook

(2) CSV 파일 실행
python -m gradebook --csv scores.csv

테스트 실행

python -m unittest discover -s tests

주요 기능

학생 점수 입력 및 평균 계산

학점 자동 부여

CSV 파일로 데이터 불러오기

모듈화 및 패키지 구조 학습 예시 제공
