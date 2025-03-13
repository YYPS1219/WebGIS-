import pandas as pd

# 读取 CSV 文件
WJLJ=r"F:\学习\前端\实践数据\ArcGIS\laji\CE.csv"
df = pd.read_csv(WJLJ)

# 打印 DataFrame
print(df)