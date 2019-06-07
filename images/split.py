from PIL import Image
import sys
import math

def get_image_size(images):
    c = {
        "width": 0,
        "height": 0,
        "slices": len(images)
    }

    for key,image in enumerate(images):
        width, height = Image.open(image).size
        c['width']+= width
        c['height']+= height

    c['width']  = int(c['width']/c['slices'])
    c['height'] = int(c['height']/c['slices'])
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

def slice_image(image,c, output):
    upper = 0
    left = 0
    slice_size = c['height'] / c['slices']
    count = 1

    for slice in range(c['slices']):
        if count == c['slices']:
            lower = c['height']
        else:
            lower = int(count + slice_size)
        bbox = (left, upper, c['width'], lower)
        working_slice = image.crop(bbox)
        upper += slice_size
        working_slice.save(output + "/c_image_" + str(count) + ".jpg")
        count +=1
    pass

def main(output, images):
    c = get_image_size(images)
    slice_image(merge(images, c), c, output)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
