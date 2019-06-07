from PIL import Image
import sys
import math

def get_image_size(images):
    c = {
        "width": 0,
        "height": 0,
        "slice_size": len(images)
    }

    for key,image in enumerate(images):
        width, height = Image.open(image).size
        c['width']+= width
        c['height']+= height

    c['width']  = int(c['width']/c['slice_size'])
    c['height'] = int(c['height']/c['slice_size'])
    return c

def merge(images, c):
    c_image = None
    for key,image_path in enumerate(images):
        image = Image.open(image_path)
        image = image.resize((c['width'],c['height'])).convert("RGBA")

        if key == 0:
            c_image = image

        c_image = Image.blend(c_image, image, alpha=.4)
    return c_image.convert("RGB")

def slice_image(image,c):
    slices = int(math.ceil(c['height']/c['slice_size']))
    pass

def main(output, images):
    c = get_image_size(images)
    slice_image(merge(images, c))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
