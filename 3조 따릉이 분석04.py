import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from matplotlib import font_manager

plt.rcParams['figure.dpi'] = 300

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('대여일자.csv', encoding="cp949", delimiter='|')

df['                대여일자'] = pd.to_datetime(df['                대여일자'])
df['요일'] = df['                대여일자'].dt.day_name()

weekday_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

df_bar = df.groupby('요일').size().reindex(weekday_order).reset_index(name='사용횟수')

total_count = df_bar['사용횟수'].sum()
df_bar['백분율'] = df_bar['사용횟수'] / total_count * 100

fig, ax = plt.subplots(figsize=(10, 6))

x = df_bar['요일']
y = df_bar['백분율']

ax.bar(x, y)
ax.set_xlabel('day')
ax.set_ylabel('%')
ax.set_title('user')

plt.show()