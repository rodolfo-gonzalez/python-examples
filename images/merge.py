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

    c['width']  = int(c['width']/len(images))
    c['height'] = int(c['height']/len(images))
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


def main(output, images):
    c = get_image_size(images)

    merge(images, c).save(output + "/c_image.jpg")
    merge(images, c).show()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
