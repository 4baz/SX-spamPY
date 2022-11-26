from PIL import ImageGrab, Image


def clipboard_mon():

    img = ImageGrab.grabclipboard()
    print(img)
# <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=200x71 at 0x105E68700>

    if img == None:
        return 0



    print(isinstance(img, Image.Image))
# True

    print(img.size)
# (200, 71)

    print(img.mode)
# RGB
    cnv = img.convert('RGB')
    cnv.save('temp_image.jpg')

    return img

