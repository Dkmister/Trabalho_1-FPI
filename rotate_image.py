from PIL import Image

#===============================
#   Given a image, return a Image matrix with
#   Inverted values of the original one
#===============================
def rotate_image(a_image):
    xy = a_image.size
    w = xy[0]
    h = xy[1]
    # new_image = zero_triples[w][h]
    for i in xrange(w):
        for j in xrange(h):
            rgb = im.getpixel((i,j))
            # new_image[w-i-1][h-j-1] += rgb[i][j]

im = Image.open("young-stalin.jpeg")
rotate_image(im)

