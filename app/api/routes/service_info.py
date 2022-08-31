from fastapi import APIRouter

service_info = APIRouter()


@service_info.get("/me")
def service_info_handler():
    return {
        "service_name": "Image scaling service",
        "service_description": "Service for rotating input images",
        "arguments": [
            {
                "argument_name": "image_data",
                "argument_description": "Image for rotation, represented in base64",
                "type": "image"
            },
            {
                "argument_name": "target_width",
                "argument_description": "Target width",
                "type": "text"
            },
            {
                "argument_name": "target_height",
                "argument_description": "Target height",
                "type": "text"
            }
        ]
    }
