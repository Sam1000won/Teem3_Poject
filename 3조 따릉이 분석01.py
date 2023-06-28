import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rc
from matplotlib import font_manager

plt.rcParams['figure.dpi'] = 300

font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

df = pd.read_csv('C:/Users/Playdata/Desktop/메모장 정리/202208_KoreaBicycle_re.csv', encoding="cp949")

new_age2 = pd.DataFrame({
    '연령대': ['10대', '20대', '30대', '40대', '50대', '60대', '70대이상'],
    '이용자수': ['5455', '31103', '20695', '12186', '8283', '2666', '362'],
    '이용시간': ['172605.0', '1007978.0', '743493.0', '476285.0', '353119.0', '127994.0', '127994.0']
})
plt.plot(new_age2['연령대'], new_age2['이용자수'], marker='o', linestyle='-', label='이용자수')
plt.plot(new_age2['연령대'], new_age2['이용시간'], marker='o', linestyle='-', label='이용시간')

plt.title("Seoul Bike Demand by Age Group")
plt.xlabel("연령대")
plt.ylabel("데이터")
plt.legend()

plt.show()