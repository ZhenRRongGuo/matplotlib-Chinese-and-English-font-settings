# matplotlib-
! 使用matplotlib绘图，让中文显示宋体，英文显示Times New Roman

# 问题
### 加入字体配置
```
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = ['Times New Roman', 'SimSun']
plt.rcParams.update(
    {
        'axes.unicode_minus': False, # 关闭unicode负号转义，避免负号显示为方块
        "mathtext.fontset": "stix",  # 使用 STIX 字体（类似 Times New Roman）
    }
)
```
或者这样
```
plt.rcParams['font.sans-serif'] = ['Times New Roman', 'SimSun']
plt.rcParams['axes.unicode_minus'] = False # 关闭unicode负号转义，避免负号显示为方块
plt.rcParams['mathtext.fontset'] = 'stix'
```
这两段代码效果等价，实现结果如下，中文无法正常显示
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/19969d04-4b62-4a2f-9626-f2c8c7717fe3" />
### 更换字体顺序
调整 'Times New Roman' 和 'SimSun' 的顺序，即：
```
plt.rcParams['font.sans-serif'] = ['SimSun', 'Times New Roman']
```
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/04399cd4-1f08-46ac-b0f5-97479af8649d" />
中文能够正常显示，但英文字符变为宋体，而不是新罗马
# 解决方案
1. 将 'SimSun' 的顺序调整到 'Times New Roman' 前面
   ```
  plt.rcParams['font.sans-serif'] = ['SimSun', 'Times New Roman']
  plt.rcParams['axes.unicode_minus'] = False # 关闭unicode负号转义，避免负号显示为方块
  plt.rcParams['mathtext.fontset'] = 'stix'
   ```
2. 英文字符使用r格式化，并用美元符号$包裹（即使用tex格式），如果需要直立体，使用\text{}命令，如
  ```
  label='线条1, ' + r'$n=100$$\text{abc}$'
  label=r'线条2, $n=200$'
  ax.set_xlabel(r'迭代次数 $\text{(Iteration)}$')
  ax.set_ylabel(r'误差值 $\text{(Error Value)}$')
  ```
3. 设置轴标签字体为 Times New Roman
  ```
  ax.tick_params(axis='both', labelfontfamily='Times New Roman')
  ```
4. 最终效果
<img width="640" height="480" alt="image" src="https://github.com/user-attachments/assets/1d73af59-614e-4515-a906-b4509b8a12d1" />
# 完整代码
```
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

```
