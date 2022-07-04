from matplotlib import transforms
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
import matplotlib.animation as animation


fig = plt.figure(1)
fig.patch.set_facecolor("red")

ax_main = fig.add_axes([0.05, 0.05, 0.9, 0.9])
ax_main.set_frame_on(True)
ax_main.set_xticks([])
ax_main.set_yticks([])
pic = mpimg.imread("../resources/image.jpg")
ax_main.imshow(pic, aspect="auto")

ax_bw = fig.add_axes([0.6, 0.6, 0.4, 0.4])
ax_bw.set_frame_on(True)
ax_bw.set_xticks([])
ax_bw.set_yticks([])
pic2 = np.zeros_like(pic)
pic2[:, :, 0] = pic2[:, :, 1] = pic2[:, :, 2] = (
    pic[:, :, 0] + pic[:, :, 1] + pic[:, :, 2]
) / 3
ax_bw.imshow(pic2, aspect="auto")

ax_text = fig.add_axes([0.05, 0.05, 0.3, 0.1])
ax_text.set_frame_on(True)
ax_text.set_xticks([])
ax_text.set_yticks([])
ax_text.text(
    0.5,
    0.5,
    "DAEMON",
    fontsize=20,
    fontweight="bold",
    va="center",
    ha="center",
    transform=ax_text.transAxes,
)
