points_dict={}
with open(r"F:\学习\前端\实践数据\ArcGIS\laji\CE.csv", "r", encoding="utf-8") as file:
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
print(points_dict)