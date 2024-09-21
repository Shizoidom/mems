from PIL import Image
import matplotlib.pyplot as plt



if __name__ == '__main__':
    image_path = 'memes/mem.jpg'

    img = Image.open(image_path)

    plt.imshow(img)
    plt.axis('off')
    plt.show()

#комит в task1
print(123)
#еще один комит в task1
print(1234)
