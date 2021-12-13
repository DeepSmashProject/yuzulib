import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import time
def test():
    # x軸:時刻
    x = np.arange(0, 100, 0.5)

    # 周波数を高くしていく
    for Hz in np.arange(0.1, 10.1, 0.01):
        # sin波を取得
        y = np.sin(2.0 * np.pi * (x * Hz) / 100)
        # グラフを描画する
        line, = plt.plot(x, y, color='blue')
        # 次の描画まで0.01秒待つ
        plt.pause(0.01)
        # グラフをクリア
        line.remove()

def test2():
    fig,ax = plt.subplots(1,1)
    image = np.array([[1,1,1], [2,2,2], [3,3,3]])
    im = ax.imshow(image)

    while True:       
        image = np.multiply(1.1, image)
        im.set_data(image)
        fig.canvas.draw_idle()
        plt.pause(0.01)
        time.sleep(1)

if __name__ == "__main__":
    test2()