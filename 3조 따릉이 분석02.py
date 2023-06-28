import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from matplotlib import font_manager

plt.rcParams['figure.dpi'] = 300

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('C:/Users/Playdata/Desktop/메모장 정리/202208_KoreaBicycle_re.csv', encoding="cp949")

df.rename(columns={'연령대코드': '나이', '이동거리(M)': '이동거리', '이용시간(분)': '이용시간'}, inplace=True)
df1 = df.copy()

gender_counts2 = df1[df1['나이'] != '정보없음'].groupby(['나이', '성별']).size().unstack()

plt.figure(figsize=(18, 6))

plt.subplot(1, 3, 2)
plt.pie(gender_counts2['F'], labels=gender_counts2.index, autopct='%1.1f%%')
plt.title('F')

plt.subplot(1, 3, 3)
plt.pie(gender_counts2['M'], labels=gender_counts2.index, autopct='%1.1f%%')
plt.title('M')

plt.tight_layout()
plt.show()