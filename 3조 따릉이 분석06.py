import numpy as np
import pandas as pd
import folium
from IPython.display import display
from folium import plugins

csv1 = pd.read_csv('/content/202208_KoreaBicycle_re.csv', encoding='cp949')
csv2 = pd.read_csv('/content/202212_KoreanBiycle_Address.csv')
csv3 = pd.read_csv('/content/서울시 시설물 정보.csv', encoding='cp949')

mycsv = pd.merge(csv1, csv2[['대여소번호', '위도', '경도','자치구']], on='대여소번호')

distancemean = mycsv.groupby('대여소명').agg({
    '이동거리(M)': 'mean',
    '위도': 'mean',
    '경도': 'mean',
    '자치구': 'first'
})

df2 = distancemean.reset_index().rename(columns={'index': '대여소명'})
df2
gu_office = csv3[csv3['시설용도분류']=='FU_BF']
gu_office = gu_office[['위도','경도','시설명']]
gu_office = gu_office.reset_index(drop=True)
gu_office['시설명'].replace('영등포구청,영등포 보건소', '영등포구청', inplace=True)
gu_office.drop(24,axis=0, inplace=True)
gu_office = gu_office.reset_index(drop=True)
gu_office

map1 = folium.Map(
    location=[37.5502, 126.982],
    zoom_start=11,
    max_zoom=14,
    min_zoom=11,
    width=800,
    height=600
    )

for _, row in df2.iterrows():
    distance = row["이동거리(M)"]
    if distance < 2000:
        color = '#48A328'
        size = 3
    elif distance < 4000:
        color = '#F3B02E'
        size = 3
    else:
        color = '#D43F1C'
        size = 7

    folium.CircleMarker(
        location=[row["위도"], row["경도"]],
        radius=size,
        color=color,
        fill=True,
        fill_opacity=0.7
    ).add_to(map1)

print("첫 번째 지도: 대여소별 이동거리(M)")
display(map1)