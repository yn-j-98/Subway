import pandas as pd
import matplotlib.pyplot as plt

# 강수량 데이터 로드 함수
def load_precipitation_data(file_path):
    # CSV 파일을 DataFrame으로 로드
    df_precipitation = pd.read_csv(file_path)
    
    # 필요한 데이터만 추출 (날짜와 강수량)
    df_precipitation = df_precipitation[['날짜', '강수량(mm)']]
    df_precipitation['날짜'] = pd.to_datetime(df_precipitation['날짜'], format='%Y-%m-%d')  # 날짜 형식 변환
    
    return df_precipitation

# 지하철 데이터 로드 함수
def load_subway_data(file_path):
    # CSV 파일을 DataFrame으로 로드
    df_subway = pd.read_csv(file_path)
    
    # 날짜 형식을 맞춰줍니다. (사용일자 -> 날짜 형식)
    df_subway['사용일자'] = pd.to_datetime(df_subway['사용일자'], format='%Y%m%d')
    
    return df_subway

# 파일 경로 설정 (예시로 2024년 1월 데이터 사용)
precipitation_file = 'precipitation_202401.csv'  # 강수량 데이터 (1월)
subway_file = 'subway_202401.csv'  # 지하철 데이터 (1월)

# 데이터 로드
precipitation_data = load_precipitation_data(precipitation_file)
subway_data = load_subway_data(subway_file)

# 데이터 확인 (강수량 및 지하철 승차 데이터)
print("강수량 데이터:")
print(precipitation_data.head())
print("\n지하철 데이터:")
print(subway_data.head())

# 날짜를 기준으로 강수량과 지하철 데이터를 병합
merged_data = pd.merge(subway_data, precipitation_data, left_on='사용일자', right_on='날짜', how='left')

# 병합된 데이터 확인
print("\n병합된 데이터:")
print(merged_data.head())

# 강수량에 따른 지하철 승차 인원 분석 (scatter plot)
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['강수량(mm)'], merged_data['승차총승객수'], alpha=0.5)
plt.title('강수량에 따른 지하철 승차 인원')
plt.xlabel('강수량 (mm)')
plt.ylabel('승차총승객수')
plt.show()

# 다른 월 데이터를 처리할 때는 파일 경로를 변경하여 같은 방식으로 처리 가능

# 예시: 2024년 4월 데이터 처리
precipitation_file_april = 'precipitation_202404.csv'
subway_file_april = 'subway_202404.csv'

precipitation_data_april = load_precipitation_data(precipitation_file_april)
subway_data_april = load_subway_data(subway_file_april)

# 4월 데이터 병합
merged_data_april = pd.merge(subway_data_april, precipitation_data_april, left_on='사용일자', right_on='날짜', how='left')

# 병합된 데이터 확인
print("\n2024년 4월 병합된 데이터:")
print(merged_data_april.head())

# 강수량에 따른 지하철 승차 인원 분석 (scatter plot for April)
plt.figure(figsize=(10, 6))
plt.scatter(merged_data_april['강수량(mm)'], merged_data_april['승차총승객수'], alpha=0.5)
plt.title('2024년 4월 강수량에 따른 지하철 승차 인원')
plt.xlabel('강수량 (mm)')
plt.ylabel('승차총승객수')
plt.show()
