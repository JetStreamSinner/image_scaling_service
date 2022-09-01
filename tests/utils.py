import base64
import pathlib

from PIL import Image


def encode_base64(arg: bytes):
    return base64.b64encode(arg)


def decode_base64(arg: str):
    return base64.b64decode(arg)


def read_image(path: pathlib.Path):
    image = Image.open(path)
    return image.tobytes()


def generate_body(image_data: str, target_width: int, target_height: int):
    return {
        "image_data": image_data,
        "target_width": target_width,
        "target_height": target_height
    }
