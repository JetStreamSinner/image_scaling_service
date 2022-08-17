from fastapi import APIRouter

service_info = APIRouter()


@service_info.get("/me")
def service_info_handler():
    return {
        "name": "Rotating Service",
        "description": "Service for rotating input images",
        "input": [
            {
                "argument_name": "image",
                "argument_description": "Image for rotation, represented in base64",
                "type": "str"
            },
            {
                "argument_name": "width",
                "argument_description": "Target width",
                "type": "int"
            },
            {
                "argument_name": "height",
                "argument_description": "Target height",
                "type": "int"
            }
        ]
    }
