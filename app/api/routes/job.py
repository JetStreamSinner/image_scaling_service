import io

from fastapi import APIRouter, HTTPException

from app.api.dependencies.image_scaler import scale_image, decode_image, encode_image, validate_input
from app.models.schemas.job_info import ServiceResponse, Image

job = APIRouter()


@job.post("/do_job", response_model=ServiceResponse)
def do_job_handler(job_info: Image):
    input_bad = not validate_input(task_data=job_info)
    if input_bad:
        raise HTTPException(status_code=400, detail="Bad arguments")

    decoded_image = decode_image(encoded_image=job_info.image_data)
    scaled_image = scale_image(image_data=decoded_image,
                               target_width=job_info.target_width, target_height=job_info.target_height)

    image_byte_array = io.BytesIO()
    scaled_image.save(image_byte_array, format="PNG")
    encoded_image = encode_image(image_byte_array.getvalue())
    return ServiceResponse(data=encoded_image, type="image")
