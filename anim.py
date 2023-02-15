import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from star import Star, Vector, DELTA_TIME
from random import uniform
from collections import deque

SIZE = 100

star_1 = Star(position=Vector(uniform(-SIZE, SIZE), uniform(-SIZE, SIZE), uniform(-SIZE, SIZE)), velocity=Vector(0, 0, 0), mass=1.0)
star_2 = Star(position=Vector(uniform(-SIZE, SIZE), uniform(-SIZE, SIZE), uniform(-SIZE, SIZE)), velocity=Vector(0, 0, 0), mass=1.0)
star_3 = Star(position=Vector(uniform(-SIZE, SIZE), uniform(-SIZE, SIZE), uniform(-SIZE, SIZE)), velocity=Vector(0, 0, 0), mass=1.0)
star_4 = Star(position=Vector(uniform(-SIZE, SIZE), uniform(-SIZE, SIZE), uniform(-SIZE, SIZE)), velocity=Vector(0, 0, 0), mass=1e-4)

stars = [star_1, star_2, star_3, star_4]
star_lines = [deque(maxlen=300), deque(maxlen=300), deque(maxlen=300), deque(maxlen=300)]

plt.style.use("dark_background")
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.set_axis_off()
ax.set_xlim(-SIZE//2, SIZE//2)
ax.set_ylim(-SIZE//2, SIZE//2)
ax.set_zlim(-SIZE//2, SIZE//2)

colors = ["r", "b", "y", "w"]

def update(num):
    ax.clear()
    ax.set_axis_off()
    ax.set_xlim(-SIZE//2, SIZE//2)
    ax.set_ylim(-SIZE//2, SIZE//2)
    ax.set_zlim(-SIZE//2, SIZE//2)
    stars[0].update([stars[1].get_data(), stars[2].get_data()])
    stars[1].update([stars[0].get_data(), stars[2].get_data()])
    stars[2].update([stars[1].get_data(), stars[0].get_data()])
    stars[3].update([stars[1].get_data(), stars[0].get_data(), stars[2].get_data()])
    for i in range(4):
        star_lines[i].append(stars[i].position)
        ax.scatter(stars[i].position.x, stars[i].position.y, stars[i].position.z, c=colors[i])
        ax.plot3D(xs=[p.x for p in star_lines[i]], ys=[p.y for p in star_lines[i]], zs=[p.z for p in star_lines[i]], c=colors[i])
    ax.plot3D(xs=[0, 0], ys=[0, 0], zs=[-SIZE, SIZE], c='grey', linewidth=0.4)
    ax.plot3D(xs=[0, 0], ys=[-SIZE, SIZE], zs=[0, 0], c='grey', linewidth=0.4)
    ax.plot3D(xs=[-SIZE, SIZE], ys=[0, 0], zs=[0, 0], c='grey', linewidth=0.4)
    return ax

animation = FuncAnimation(fig=fig, func=update, frames=1000, interval=DELTA_TIME)

plt.show()