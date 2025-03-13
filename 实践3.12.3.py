#X=[-3514763.792,-1703849.060,1712971.188,2122989.618,-4266464.247,-610466.581,1644634.783,-2728895.135,-132111.746,-3993118.627]
#Y=[1059214.277,1571737.314,3109306.426,-2084260.351,-2733456.199,-1708410.124,990877.872,-136672.810,6423622.068,6970313.308]
# 定义一个空字典来存储点的坐标
points_dict = {}

# 打开文件并读取内容
with open(r"F:\学习\前端\实践数据\ArcGIS\实践3.12点坐标.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # 读取所有行

# 跳过第一行（标题行）
for line in lines[1:]:
    # 去掉每行的换行符并按逗号分割
    parts = line.strip().split(',')
    
    # 提取点号（OBJECTID）和坐标
    object_id = int(parts[0])  # 点号
    longitude = float(parts[1])  # 经度
    latitude = float(parts[2])  # 纬度
    
    # 将点的坐标存储到字典中，以点号为键
    points_dict[object_id] = (longitude, latitude)
for object_id, (longitude, latitude) in points_dict.items():
       if longitude > 0 and latitude < 0:
        print(f"{object_id} 是正确点")
# 输出字典内容
#for point_id, (longitude, latitude) in points_dict.items():
    #print(f"点号 {point_id} 的坐标：经度 = {longitude}, 纬度 = {latitude}")