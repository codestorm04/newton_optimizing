import matplotlib.pyplot as plt
import numpy as np

# 定义 x 变量的范围 (-3，3) 数量 50 
x=np.linspace(-40,40,5000)
# y=x**2
y = x*x*x + 2*x*x +3*x + 4
# y = np.exp(x) + 2*x*x + 3*x

# 绘制 y=x^2 的图像，设置 color 为 red，线宽度是 1，线的样式是 --
plt.plot(x,y,color='red',linewidth=1.0,linestyle='-')

plt.xlabel('x')
plt.ylabel('y')
ax=plt.gca()

# 使用.spines设置边框：x轴；将右边颜色设置为 none。
# 使用.set_position设置边框位置：y=0的位置；（位置所有属性：outward，axes，data）
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置标签
ax.set_title('y = f(x)',fontsize=14,color='r')

# 显示图像
plt.show()