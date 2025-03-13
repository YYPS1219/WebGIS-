#SCLB:输出列表
SCLB=[]
#CDJD:测点经度
CDJD={"测点A":123.5,"测点B":124.3,"测点C":123.6,"测点D":157.9,"测点F":98.7}
CDWD={"测点A":28.3,"测点B":35.2,"测点C":17.8,"测点D":23.9,"测点F":45.2}#CDWD:测点纬度
#point=input("请输入需要查询的点号：")
#longitude=CDJD[point]
#latitude=CDWD[point]]
#if(longitude<150)and(latitude>30):
    #print(f"{point}在区域内")
#else:
  #  print(f"{point}不在区域内")
for point in CDJD.keys():
    longitude=CDJD[point]
    latitude=CDWD[point]
    if(longitude>150)and(latitude>60):
        SCLB.append(point)
if SCLB:
    result="，".join(SCLB)
    print(f"经度大于120，纬度大于30的点：{result}")
else:
    print("该点不存在")


    