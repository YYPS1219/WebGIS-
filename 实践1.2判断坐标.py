x1=input("请输入经度：")
y1=input("请输入纬度：")
if  180 > float(x1) > 0 and 90 > float(y1) > 0:
    print(f"该点位于{x1}°E,{y1}°N")
elif 0 > float(x1) >-180 and 0 > float(y1) > -90:
    print(f"该点位于{x1}°W,{y1}°S")

    