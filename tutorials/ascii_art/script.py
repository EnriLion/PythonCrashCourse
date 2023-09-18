import PIL.Image

# ASCII_CHARS = ["@", "#", "%", " ", ";", ">", "<", "?"]
ASCII_CHARS = ["|", "||", "|||", "-", " ", "_"]

# resize image according to a new width


def resize_image(image, new_width=100):
    """ Resize image according to a new width"""
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize(new_width, new_height)
    return(resized_image)


def grayify(image):
    """ Convert each pixel to grayscale"""
    grayscale_image = image.convert("L")
    return(grayscale_image)


def pixels_to_ascii(image):
    """ Convert pixels to a string of ASCII characters"""
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)


def main(new_width=100):
    """Attempt to open image from user-input"""
    path = input("Enter a valid pathname to an image:\n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not a valid pathname to an image.")

    # convert image to ASCII

    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # format

    pixel_count = len(new_image_data)
    asccii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # print result
    print(asccii_image)

main()
