from PIL import Image


def change():
    for i in range(1, 51):
        image = Image.open("emoji/happy" + str(i) + ".png")
        rgb_im = image.convert('RGB')
        rgb_im.save("emoji_data/happy" + str(i) + ".jpg")

    for i in range(1, 51):
        image = Image.open("emoji/sad" + str(i) + ".png")
        rgb_im = image.convert('RGB')
        rgb_im.save("emoji_data/sad" + str(i) + ".jpg")

change()
