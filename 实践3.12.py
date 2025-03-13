#ZZJG=[]
CDJD=[123.5,124.3,123.6,157.9,98.7]
#for x in CDJD:
    #if x >=  123.5:
       # print(x,end=",")#(方法一)
        #ZZJG.append(str(x))#（方法二）
#if ZZJG:
      # JG=",".join(ZZJG)
      # print(f"大于123.5°的有:{JG}")
##results=[str(x) for x in CDJD if x >= 123.5]
#if results:
    #print("大于123.5°的有:",",".join(results))
# 初始化累加变量和计数器
total = 0  # 用于累加所有数字
count = 0  # 用于记录数字的个数

# 遍历列表中的每个数字
for number in CDJD:
    total += number  # 累加当前数字
    count += 1       # 数字计数加1

# 计算平均值
if count > 0:  # 防止除以零
    average = total / count
    print("平均值是：", average)
else:
    print("列表为空，无法计算平均值。")