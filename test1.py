import matplotlib.pyplot as plt
import numpy as np

# -------------------------- 全局字体配置 --------------------------
# 中文用宋体（SimSun），英文用Times New Roman
# plt.rcParams['font.sans-serif'] = ['Times New Roman', 'SimSun']
plt.rcParams['font.sans-serif'] = ['SimSun', 'Times New Roman']
# 关闭unicode负号转义，避免负号显示为方块
plt.rcParams['axes.unicode_minus'] = False
# 公式（$...$内的内容）使用STIX字体
plt.rcParams['mathtext.fontset'] = 'stix'


# 生成数据
x = np.linspace(0, 15, 200)
y_conj = np.exp(-0.1 * x) * np.sin(2 * x)
y_grad = np.exp(-0.2 * x) * np.cos(2 * x)

# 创建画布
fig, ax = plt.subplots(num='1')

# 绘制曲线并添加混合标签
# ax.plot(x, y_conj, label='线条1, n=100abc', linewidth=2, color='#FF6B6B')
# ax.plot(x, y_grad, label='线条2, n=200', linewidth=2, color='#4ECDC4')
ax.plot(x, y_conj, label='线条1, ' + r'$n=100$$\text{abc}$', linewidth=2, color='#FF6B6B')
ax.plot(x, y_grad, label=r'线条2, $n=200$', linewidth=2, color='#4ECDC4')

# 添加图表元素（含中英文混合文本）
# ax.set_xlabel('迭代次数 (Iteration)')
# ax.set_ylabel('误差值 (Error Value)')
ax.set_xlabel(r'迭代次数 $\text{(Iteration)}$')
ax.set_ylabel(r'误差值 $\text{(Error Value)}$')
ax.tick_params(axis='both', labelfontfamily='Times New Roman')
ax.grid(alpha=0.3, linestyle='--')
ax.legend(fontsize=11, loc='upper right')

# 显示图表
plt.show()
