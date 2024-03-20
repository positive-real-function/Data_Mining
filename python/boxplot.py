import matplotlib.pyplot as plt
import numpy as np

# 导入数据
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# np.random.seed(0)
# data=np.random.normal(size=(100,))
data = np.array(arr)

# 计算第25、50和75百分位数
p25 = np.percentile(data, 25)
p50 = np.percentile(data, 50)
p75 = np.percentile(data, 75)
# 计算最大值最小值
Max = data.max()
Min = data.min()

print("最小值：",Min)
print("第25百分位数：", p25)
print("第50百分位数：", p50)
print("第75百分位数：", p75)
print("最大值：",Max)

# 绘制箱线图
plt.boxplot(data)

# 添加标题和标签
plt.title("Boxplot")
plt.xlabel("Data")

# 显示图形
plt.show()
