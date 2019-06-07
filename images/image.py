from PIL import Image
import sys

def merge(image_a, image_b, output):
    pass

def cut_Y(image):
    pass

def main(output, images):
    k = len(images)
    c = {
        "width": 0,
        "height": 0,
    }

    for key,image in enumerate(images):
        width, height = Image.open(image).size
        c['width']+= width
        c['height']+= height

        print("width: {} height: {}".format(width, height))
        print("width: {} height: {}".format(c['width'], c['height']))
    pass


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
