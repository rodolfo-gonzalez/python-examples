from PIL import Image
import sys

def get_image_size(images):
    c = {
        "width": 0,
        "height": 0,
    }

    for key,image in enumerate(images):
        width, height = Image.open(image).size
        c['width']+= width
        c['height']+= height
        print("{} {}".format(width, height))

    c['width']  = int(c['width']/len(images))
    c['height'] = int(c['height']/len(images))
    return c

def merge(image_a, image_b, output):
    pass


def main(output, images):
    c = get_image_size(images)
    print("{} {}".format(c['width'] ,c['height']))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
