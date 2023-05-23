# -*- coding:utf-8 -*-
import numpy as np

# Load data from file
a = np.loadtxt(r'your\path\to\file.xyz')

# Extract each column and calculate the minimum value and resolution
x, y, z = a[:, 0], a[:, 2], a[:, 1]

Xmin, Ymin, Zmin = np.min(x), np.min(y), np.min(z)
resoX = np.min(np.delete(x, np.where(x == Xmin))) - Xmin
resoY = np.min(np.delete(y, np.where(y == Ymin))) - Ymin
resoZ = np.min(np.delete(z, np.where(z == Zmin))) - Zmin

print(resoX, resoY, resoZ)
print(resoX * resoY * resoZ)

# Transform the new one-dimensional matrices with interval 1 starting from 1
X_new = (x - Xmin) / resoX + 1
Y_new = (y - Ymin) / resoY + 1
Z_new = (z - Zmin) / resoZ + 1

lenx = int(round(np.max(X_new), 0)) + 1
leny = int(round(np.max(Y_new), 0)) + 1
lenz = int(round(np.max(Z_new), 0)) + 1

print(lenx, leny, lenz)
print(X_new, Y_new, Z_new)

# Combine the matrices vertically and transpose them to create a three-dimensional matrix
Mar = np.transpose(np.vstack((X_new, Y_new, Z_new)))
print(Mar)

# Create a new matrix filled with zeros
OriMar = np.zeros([lenz, lenx, leny])  # z (dimension), y (row), x (column)

# Assign the corresponding points to the new matrix and set them to 1
for i in range(len(Mar)):
    zz, yy, xx = map(int, Mar[i])
    OriMar[zz, xx, yy] = 1

m = OriMar.reshape(lenz * lenx, leny)

np.savetxt(
    r'your\path\to\file.txt',
    m, fmt='%d'
)

# -*- coding:utf-8 -*-
import numpy as np

# Load data from file
a = np.loadtxt(r'C:\Users\D\Desktop\stl-to-voxel\材料\STLmodel\cone.xyz')

# Extract each column and calculate the minimum value and resolution
x, y, z = a[:, 0], a[:, 2], a[:, 1]

Xmin, Ymin, Zmin = np.min(x), np.min(y), np.min(z)
resoX = np.min(np.delete(x, np.where(x == Xmin))) - Xmin
resoY = np.min(np.delete(y, np.where(y == Ymin))) - Ymin
resoZ = np.min(np.delete(z, np.where(z == Zmin))) - Zmin

print(resoX, resoY, resoZ)
print(resoX * resoY * resoZ)

# Transform the new one-dimensional matrices with interval 1 starting from 1
X_new = (x - Xmin) / resoX + 1
Y_new = (y - Ymin) / resoY + 1
Z_new = (z - Zmin) / resoZ + 1

lenx = int(round(np.max(X_new), 0)) + 1
leny = int(round(np.max(Y_new), 0)) + 1
lenz = int(round(np.max(Z_new), 0)) + 1

print(lenx, leny, lenz)
print(X_new, Y_new, Z_new)

# Combine the matrices vertically and transpose them to create a three-dimensional matrix
Mar = np.transpose(np.vstack((X_new, Y_new, Z_new)))
print(Mar)

# Create a new matrix filled with zeros
OriMar = np.zeros([lenz, lenx, leny])  # z (dimension), y (row), x (column)

# Assign the corresponding points to the new matrix and set them to 1
for i in range(len(Mar)):
    zz, yy, xx = map(int, Mar[i])
    OriMar[zz, xx, yy] = 1

m = OriMar.reshape(lenz * lenx, leny)

np.savetxt(
    r'C:\Users\D\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04LTS_79rhkp1fndgsc\LocalState\rootfs\home\d\FLUKA\stl-voxel\BVM\voxel(cone).txt',
    m, fmt='%d'
)
