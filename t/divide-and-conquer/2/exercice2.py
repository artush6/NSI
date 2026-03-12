import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


# Recursive divide-and-conquer rotation
def rotate(image):
    n = len(image)

    if n <= 1:
        return image

    temp = np.copy(image[n//2:, :n//2])

    image[n//2:, :n//2] = rotate(image[n//2:, n//2:])
    image[n//2:, n//2:] = rotate(image[:n//2, n//2:])
    image[:n//2, n//2:] = rotate(image[:n//2, :n//2])
    image[:n//2, :n//2] = rotate(temp)
    return image


# More efficient rotation without recursion
def rotate2(image):
    n = len(image)

    for i in range(n // 2):
        for j in range(n // 2):

            # sauvegarde pixel A (haut gauche)
            temp = np.copy(image[i, j])

            # C -> A
            image[i, j] = image[i + n//2, j]

            # D -> C
            image[i + n//2, j] = image[i + n//2, j + n//2]

            # B -> D
            image[i + n//2, j + n//2] = image[i, j + n//2]

            # A -> B
            image[i, j + n//2] = temp

    return image


# Load image
image = np.array(Image.open("animal.jpg"))

# Show original image
plt.figure("Image de départ")
plt.imshow(image)
plt.axis("off")
plt.show()

# Apply rotations
image = rotate(image)      # recursive rotation
image = rotate2(image)     # first efficient rotation
image = rotate2(image)     # second rotation (total effect: 180° after rotate)

# Show final image
plt.figure("Image finale")
plt.imshow(image)
plt.axis("off")
plt.show()
