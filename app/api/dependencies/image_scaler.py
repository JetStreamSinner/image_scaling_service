import base64
import binascii
import io

import PIL.Image
from fastapi import HTTPException

from app.models.schemas.job_info import Image


def encode_image(raw_image: bytes):
    return base64.b64encode(raw_image)


def decode_image(encoded_image: str):
    try:
        decoded = base64.b64decode(encoded_image)
    except binascii.Error:
        raise HTTPException(status_code=400, detail="Bad arguments")
    return decoded


def component_valid(val: int):
    return val >= 0


def validate_input(task_data: Image):
    image_data = task_data.image_data
    width = task_data.target_width
    height = task_data.target_height
    arguments_ok = image_data and component_valid(width) and component_valid(height)
    return arguments_ok


def scale_image(image_data: bytes, target_width: int, target_height: int):
    try:
        image_data = PIL.Image.open(io.BytesIO(image_data))
    except PIL.UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Bad arguments")

    target_size = (target_width, target_height)
    resized_image = image_data.resize(target_size)
    return resized_image
