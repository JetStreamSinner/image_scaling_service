from pydantic import BaseModel


class ImageData(BaseModel):
    image_data: str


class ImageSize(BaseModel):
    target_width: int
    target_height: int


class Image(ImageData, ImageSize):
    pass


class ServiceResponse(BaseModel):
    data: str
    type: str
