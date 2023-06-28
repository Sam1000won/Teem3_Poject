from folium import Tooltip
import numpy as np
import pandas as pd
import folium
from IPython.display import display

map2 = folium.Map(
    location=[37.5502, 126.982],
    zoom_start=11,
    max_zoom=13,
    min_zoom=11,
    width=800,
    height=600
    )

for _, row in df2.groupby("자치구").mean().iterrows():
    gu = row.name
    distance = row["이동거리(M)"]
    if distance < 2500:
        color = 'green'
        size = 7
    elif distance < 3000:
        color = 'orange'
        size = 10
    else:
        color = 'red'
        size = 12

    gu_name = f"{gu}청"
    office_location = gu_office.loc[gu_office["시설명"]==gu_name, ["위도","경도"]].values[0]
    folium.CircleMarker(
        location=office_location,
        radius=size,
        color=color,
        fill=True,
        fill_opacity=0.7,
    ).add_child(Tooltip(gu)).add_to(map2)  # Tooltip을 사용하여 자치구 이름을 띄웁니다.

print("두 번째 지도: 지역별 평균 이동거리(M) - 구청 위치")
display(map2)