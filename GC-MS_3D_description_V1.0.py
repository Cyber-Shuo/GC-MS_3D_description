import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import norm

# construct four different one-dimensional Gaussian distributions
mean1, std1 = 10, 1
mean2, std2 = 20, 5
mean3, std3 = 25, 3
mean4, std4 = 40, 2

gaussian1 = np.random.normal(mean1, std1, 100)
gaussian2 = np.random.normal(mean2, std2, 100)
gaussian3 = np.random.normal(mean3, std3, 100)
gaussian4 = np.random.normal(mean4, std4, 100)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# calculate a histogram
hist1, bins1 = np.histogram(gaussian1, bins=30, density=True)
hist2, bins2 = np.histogram(gaussian2, bins=30, density=True)
hist3, bins3 = np.histogram(gaussian3, bins=30, density=True)
hist4, bins4 = np.histogram(gaussian4, bins=30, density=True)

# calculate the fitted curve
x = np.linspace(0, 50, 1000)
y1 = norm.pdf(x, mean1, std1)
y2 = norm.pdf(x, mean2, std2)
y3 = norm.pdf(x, mean3, std3)
y4 = norm.pdf(x, mean4, std4)
y5 = y1 + y2 + y3 + y4

# plotting three-dimensional histograms
width = (bins1[1] - bins1[0]) * 0.8
x1 = np.array([(bins1[i] + bins1[i + 1]) / 2 for i in range(len(bins1) - 1)])
x2 = np.array([(bins2[i] + bins2[i + 1]) / 2 for i in range(len(bins2) - 1)])
x3 = np.array([(bins3[i] + bins3[i + 1]) / 2 for i in range(len(bins3) - 1)])
x4 = np.array([(bins4[i] + bins4[i + 1]) / 2 for i in range(len(bins4) - 1)])

ax.bar(x1, hist1, zs=10, zdir='y', width=width, alpha=0.8, color='r')
ax.bar(x2, hist2, zs=30, zdir='y', width=width, alpha=0.8, color='g')
ax.bar(x3, hist3, zs=50, zdir='y', width=width, alpha=0.8, color='b')
ax.bar(x4, hist4, zs=80, zdir='y', width=width, alpha=0.8, color='y')

ax.plot(x, y1, zs=10, zdir='y', color='r', label='Gaussian 1')
ax.plot(x, y2, zs=30, zdir='y', color='g', label='Gaussian 2')
ax.plot(x, y3, zs=50, zdir='y', color='b', label='Gaussian 3')
ax.plot(x, y4, zs=80, zdir='y', color='y', label='Gaussian 4')

ax.set_xlabel('Retention Time/min')
ax.set_ylabel('m/Z')
ax.set_zlabel('Intensity')
plt.title('3D chromatography')

# plotting 2D chromatograms
fig_1 = plt.figure()
ax_1 = fig_1.add_subplot()
ax_1.fill(x, y1, color='r', alpha=0.5)
ax_1.fill(x, y2, color='g', alpha=0.5)
ax_1.fill(x, y3, color='b', alpha=0.5)
ax_1.fill(x, y4, color='y', alpha=0.5)
ax_1.plot(x, y5, color='black')
ax_1.set_title('chromatography')
ax_1.set_xlabel('Retention Time/min')
ax_1.set_ylabel('Intensity')

# plotting two-dimensional massspectra
z_1 = norm.pdf(20, mean1, std1)
z_2 = norm.pdf(20, mean2, std2)
z_3 = norm.pdf(20, mean3, std3)
z_4 = norm.pdf(20, mean4, std4)
fig_2 = plt.figure()
ax_2 = fig_2.add_subplot()
plt.axvline(x=10, ymin=0, ymax=z_1)
plt.axvline(x=30, ymin=0, ymax=z_2)
plt.axvline(x=50, ymin=0, ymax=z_3)
plt.axvline(x=80, ymin=0, ymax=z_4)
ax_2.set_title('Retention Time=20min Mass spectrometry')
ax_2.set_xlabel('m/Z')
ax_2.set_ylabel('Intensity')

plt.show()
