import base64

def CustomBase64Converter(image_path):
    with open(image_path, "rb") as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return image_data


def CustomInMemoryBase64Converter(image_path):
        read_image = image_path.read()
        image_data = base64.b64encode(read_image).decode('utf-8')
        return image_data