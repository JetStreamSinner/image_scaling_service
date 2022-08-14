from pydantic import BaseModel


class Image(BaseModel):
    image_data: str


class ScaleImage(Image):
    target_width: int
    target_height: int
