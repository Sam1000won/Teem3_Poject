import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import warnings
import matplotlib.pyplot as plt
plt.rcParams['figure.dpi'] = 300

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('C:/Users/Playdata/Desktop/메모장 정리/202208_KoreaBicycle_re.csv', encoding="cp949")

warnings.filterwarnings("ignore")
def def_sex():
    filtered_data = df[df['성별'] != 'X']
    filtered_data.loc[:, '성별'] = filtered_data['성별'].map({'M': 1, 'F': 0})
    filtered_data = filtered_data.dropna()
    filtered_data.reset_index(drop=True, inplace=True)
    return filtered_data['성별']

sex = def_sex()

def def_age(df):
    filtered_data = df[df['연령대코드'] != 0].copy()
    filtered_data.reset_index(drop=True, inplace=True)
    return filtered_data['연령대코드']

age = def_age(df)

def def_lord(df):
    filtered_data = df[df['이동거리(M)'] != 0].copy()
    filtered_data.reset_index(drop=True, inplace=True)
    return filtered_data['이동거리(M)']
lord = def_lord(df)

def def_time(df):
    filtered_data = df[df['이용시간(분)'] != 0].copy()
    filtered_data.reset_index(drop=True, inplace=True)
    return filtered_data['이용시간(분)']
time = def_time(df)

def def_sum(df):
    min_length = min(len(sex), len(age), len(lord), len(time))
    sex_subset = sex[:min_length].values.reshape(-1, 1)
    age_subset = age[:min_length].values.reshape(-1, 1)
    lord_subset = lord[:min_length].values.reshape(-1, 1)
    time_subset = time[:min_length].values.reshape(-1, 1)
    combined_matrix = np.column_stack((sex_subset, age_subset, lord_subset, time_subset))
    return combined_matrix

mix = def_sum(df)
mean_gender = np.mean(sex)
mean_age = np.mean(age)
mean_distance = np.mean(lord)
mean_duration = np.mean(time)
prediction_data = np.array([[mean_gender, mean_age, mean_distance, mean_duration]])

min_length = min(len(sex), len(age), len(lord), len(time))
sex = sex[:min_length]
age = age[:min_length]
lord = lord[:min_length]
time = time[:min_length]
X_train = np.column_stack((sex, age, lord, time))
y_train = mix
model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(prediction_data)
rounded_prediction = np.floor(prediction_data).astype(int)

labels = ['성별', '나이', '이용거리', '이용시간(분)']

predicted_values = [0, 29, 2973, 25]

x = np.arange(len(labels))

plt.bar(x, predicted_values, width=0.4, align='center', label='예측값')
plt.xlabel('변수')
plt.ylabel('값')
plt.title('예측값과 실제값 비교')
plt.xticks(x, labels)
plt.legend()
plt.show()