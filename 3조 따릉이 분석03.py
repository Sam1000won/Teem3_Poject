import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from matplotlib import font_manager

plt.rcParams['figure.dpi'] = 300

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('C:/Users/Playdata/Desktop/메모장 정리/202208_KoreaBicycle_re.csv', encoding="cp949")

df_waffle = df[df['나이'] >= 10].loc[:, ['대여일자', '나이']]
df_waffle = df_waffle.groupby(['대여일자', '나이']).size().unstack().reset_index()
df_waffle.drop('대여일자', axis=1, inplace=True)
df_waffle.fillna(0, inplace=True)
df_waffle = df_waffle.astype(int)

total_sum = df_waffle.values.sum()
df_waffle = df_waffle.apply(lambda x: (x / total_sum) * 100)

fig, ax = plt.subplots(figsize=(10, 6))

x = df_waffle.columns
y = df_waffle.values[0]

ax.bar(x, y)

ax.set_title('', fontsize=10)

plt.show()