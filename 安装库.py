import pandas as pd

# 打印 Pandas 的版本信息
print("Pandas 已成功安装，版本为：", pd.__version__)

# 创建一个简单的 DataFrame 并打印
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
print("\n示例 DataFrame：")
print(df)