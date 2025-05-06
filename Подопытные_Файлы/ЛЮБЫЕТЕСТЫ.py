import matplotlib.pyplot as plt

x=[0, 100, 500, 1000, 1500]
y1=[0.0, 0.004, 0.321, 2.995, 13.041]
y2=[0.0, 0.002, 0.183, 1.561, 6.951]
y4=[0.0, 0.002, 0.101, 0.949, 5.279]
y8=[0.0, 0.003, 0.091, 0.653, 3.024]
y16=[0.0, 0.005, 0.069, 0.515, 1.875]
y32=[0.0, 0.014, 0.072, 0.488, 4.590]
y64=[0.0, 0.021, 0.068, 0.493, 2.747]
y128=[0.0, 0.041, 0.095, 0.524, 2.679]
fig, ax = plt.subplots()

ax.plot(x, y1, label='1')

ax.plot(x, y2, label='2')
ax.plot(x, y4, label='4')
ax.plot(x, y8, label='8')
ax.plot(x, y16, label='16')
ax.plot(x, y32, label='32')
ax.plot(x, y64, label='64')
ax.plot(x, y128, label='128')

ax.set_xlabel('X-ось (Размер)')  # Подпись оси X
ax.set_ylabel('Y-ось (Время)')   # Подпись оси Y

ax.legend()
plt.show()