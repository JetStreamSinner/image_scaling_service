import io
from fastapi import APIRouter

from app.api.dependencies.image_scaler import scale_image, decode_image, encode_image
from app.models.schemas.job_info import ServiceResponse, Image

job = APIRouter()


@job.post("/do_job", response_model=ServiceResponse)
def do_job_handler(job_info: Image):
    decoded_image = decode_image(encoded_image=job_info.image_data)
    scaled_image = scale_image(image_data=decoded_image,
                               target_width=job_info.target_width, target_height=job_info.target_height)
    image_byte_array = io.BytesIO()
    scaled_image.save(image_byte_array, format="PNG")
    encoded_image = encode_image(image_byte_array.getvalue())
    return ServiceResponse(data=encoded_image, type="image")
