#CDJD:测点经度
CDJD={"测点A":123.5,"测点B":124.3,"测点C":123.6,"测点D":157.9,"测点F":98.7}
CDWD={"测点A":28.3,"测点B":35.2,"测点C":17.8,"测点D":23.9,"测点F":45.2}#CDWD:测点纬度
point=input("请输入需要查询的点号：")
longitude=CDJD[point]
latitude=CDWD[point]
print(f"{point}经度：{longitude},纬度：{latitude}")
#for point in CDJD.keys():
    #longitude=CDJD[point]
    #latitude=CDWD[point]
    #print(f"{point}经度：{longitude},纬度：{latitude}")