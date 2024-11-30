'''
Created on 2024. 11. 29.

@author: yenaj
'''
import csv  # CSV 파일 읽기를 위한 라이브러리
import matplotlib.pyplot as plt  # 그래프 생성을 위한 라이브러리

# CSV 파일 경로 지정
file_path = "subway_2023.csv"

# 월별 데이터와 승하차인원수를 저장할 리스트 초기화
months = []  # 월을 저장할 리스트
peoples = []  # 각 월의 승하차인원수를 저장할 리스트

# CSV 파일 열기
with open(file_path, mode='r') as file:
    reader = csv.reader(file)  # CSV 파일을 읽어올 수 있는 reader 객체 생성
    header = next(reader)  # 첫 번째 줄(헤더)은 건너뛰기
    
    # CSV 파일의 각 줄을 순회하며 데이터 처리 
    for row in reader:
        a = row[-2]  # 수송연월 데이터 (예: "Jan-23")
        b = row[-1]  # 승하차인원수 데이터
        
        # 월 데이터가 처음 등장하면 리스트에 추가
        if a not in months:
            months.append(a)  # 중복되지 않게 월 추가
            
        # 해당 월의 인덱스를 찾기
        index = months.index(a)
        
        # 해당 월의 데이터를 합산하기 위해 peoples 리스트 크기를 동적으로 조정
        if len(peoples) <= index:
            peoples.append(0)  # 새로운 월 데이터를 위한 초기값 추가
        
        # 월별 승하차인원수 데이터를 합산
        peoples[index] += int(b)  # 문자열을 정수로 변환 후 합산

# 그래프 크기 설정
plt.figure(figsize=(10, 6))  # 가로 10, 세로 6 크기의 그래프 생성

# 막대그래프 생성
plt.bar(months, peoples, color='skyblue')  # X축: months, Y축: peoples, 색상: 하늘색

# 그래프 제목 및 축 레이블 설정
plt.title("Monthly Subway Ridership", fontsize=15)  # 그래프 제목
plt.xlabel("Month", fontsize=12)  # X축 레이블
plt.ylabel("People", fontsize=12)  # Y축 레이블

# 각 막대 위에 승하차인원수를 표시
for i, v in enumerate(peoples):  
    plt.text(i, v + 50000, f"{v:,}", ha='center', fontsize=9)  
    # i: X축 위치, v: Y축 값, `f"{v:,}"`: 천 단위 콤마 추가, ha='center': 텍스트 중앙 정렬

# X축 레이블을 기울여서 겹치지 않게 표시
plt.xticks(rotation=45)

# 그래프 레이아웃 자동 조정
plt.tight_layout()

# 그래프 표시
plt.show()
            
            
            