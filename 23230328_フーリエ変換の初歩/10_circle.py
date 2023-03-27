import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 大中小の円の半径
R1 = 1
R2 = 0.5
R3 = 0.25

# 1度あたりのラジアン
DEG_TO_RAD = np.pi / 180

# FigureとAxesを作成
fig = plt.figure(figsize=(10, 6))
# XY座標のグラフを追加
ax1 = fig.add_subplot(221)
# θY座標のグラフを追加
ax2 = fig.add_subplot(222)
# θX座標のグラフを追加
ax3 = fig.add_subplot(223)

# 円描画の範囲
theta = np.linspace(0, 2*np.pi, 100)

# 点Rの移動する角度の範囲
theta_p = np.arange(0, 361, 1)

# 点Rの軌跡
theta_list = []
theta_x_list = []
theta_y_list = []

# フレームごとの描画関数
def animate(frame):
    global theta_list, theta_x_list, theta_y_list
    global x_p, y_p
    ax1.clear()
    ax2.clear()
    ax3.clear()
    
    # 点Pの座標
    theta_p_rad = theta_p[frame] * DEG_TO_RAD
    x_p = np.cos(theta_p_rad)
    y_p = np.sin(theta_p_rad)
    
    # 円の描画
    ax1.plot(np.cos(theta), np.sin(theta), 'b')
    ax1.plot(x_p, y_p, 'ob')
    
    # 点Qの座標
    theta_q_rad = theta_p[(frame*2)%len(theta_p)] * DEG_TO_RAD
    x_q = R2 * np.cos(theta_q_rad)+x_p
    y_q = R2 * np.sin(theta_q_rad)+y_p
    
    # 円の描画
    ax1.plot(R2 * np.cos(theta)+x_p, R2 * np.sin(theta)+y_p, 'g')
    ax1.plot(x_q, y_q, 'og')

    # 点Rの座標
    theta_r_rad = theta_p[(frame*3)%len(theta_p)] * DEG_TO_RAD
    x_r = R3 * np.cos(theta_r_rad)+x_q
    y_r = R3 * np.sin(theta_r_rad)+y_q    

    # 円の描画
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.plot(R3 * np.cos(theta)+x_q, R3 * np.sin(theta)+y_q, 'k')
    ax1.plot(x_r, y_r, 'or')

    # 点Rの周波数上の軌跡を更新
    theta_list.append(theta_p[frame])
    theta_x_list.append(x_r)
    theta_y_list.append(y_r)
    
    # θY座標の描画
    ax2.set_xlim(0, 360)
    ax2.set_ylim(-2, 2)
    ax2.plot(theta_list, theta_y_list, '.k')
    ax2.plot(theta_p[frame], y_r, 'or')

    # θX座標の描画
    ax3.set_xlim(-2, 2)
    ax3.set_ylim(360, 0)
    ax3.plot(theta_x_list, theta_list, '.k')
    ax3.plot(x_r, theta_p[frame], 'or')
    
# アニメーションの作成
ani = animation.FuncAnimation(fig, animate, frames=len(theta_p), interval=5, blit=False)

# アニメーションの表示
ani.save("aaa.png")
plt.show()
