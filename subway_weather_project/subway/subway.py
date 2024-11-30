import csv

import matplotlib.pyplot as plt

def process_csv(file_path):
    """
    주어진 CSV 파일에서 2019~2023년 데이터를 처리하여 반환합니다.
    """
    data = {year: [0] * 12 for year in range(2019, 2024)}  # 2019~2023년, 12개월 초기화
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # 헤더 건너뛰기

        for row in reader:
            if len(row) < 5:  # 데이터 길이 확인
                continue

            year_month = row[-2].strip()  # "Jan-23" 형식
            people = row[-1].strip()     # 승하차 인원수

            # 데이터 유효성 검사
            if not people.isdigit():
                continue

            # "Jan-23"을 분리하여 연도와 월로 나누기
            try:
                month, year_suffix = year_month.split('-')
                year = int("20" + year_suffix)  # "23" -> 2023
                if year < 2019 or year > 2023:  # 필요한 연도만 처리
                    continue

                month_index = months.index(month)  # 월 인덱스 계산
                data[year][month_index] += int(people)  # 월별 데이터 추가
            except (ValueError, IndexError):
                continue  # 형식 오류 처리

    return data

# CSV 파일 경로
file_paths = ["subway_2019.csv", "subway_2020.csv", "subway_2021.csv", "subway_2022.csv", "subway_2023.csv"]

# 모든 데이터를 저장할 딕셔너리 초기화
all_data = {year: [0] * 12 for year in range(2019, 2024)}

# 각 파일 처리
for file_path in file_paths:
    yearly_data = process_csv(file_path)
    for year, monthly_data in yearly_data.items():
        all_data[year] = [x + y for x, y in zip(all_data[year], monthly_data)]

# x축 (월) 정의
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# 그래프 그리기
plt.figure(figsize=(12, 6))

for year, monthly_data in sorted(all_data.items()):
    plt.plot(months, monthly_data, marker='o', label=f"{year}")  # 연도별 선 그래프

# 그래프 설정
plt.title("Monthly Subway Ridership (2019 - 2023)", fontsize=16)
plt.xlabel("Month", fontsize=12)
plt.ylabel("People", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Year")
plt.grid(True, linestyle='--', alpha=0.6)

# 그래프 표시
plt.tight_layout()
plt.show()
