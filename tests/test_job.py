import pathlib

import pytest
from fastapi.testclient import TestClient

from app.main import get_application
from tests import utils

application = get_application()
client = TestClient(app=application)


class TestBadArguments:
    image_path = pathlib.Path("tests/resources/job/image_to_scale.jpg")

    correct_image = utils.encode_base64(utils.read_image(path=image_path))
    correct_width = 800
    correct_height = 600

    empty_image = ""
    bad_image = "bad image"
    bad_width = -123
    bad_height = -123

    params = [
        utils.generate_body(empty_image, correct_width, correct_height),
        utils.generate_body(bad_image, correct_width, correct_height),
        utils.generate_body(correct_image, bad_width, correct_height),
        utils.generate_body(correct_image, correct_width, bad_height)
    ]

    @pytest.mark.parametrize("request_body", params)
    def test_arguments(self, request_body):
        response = client.post("/do_job", json=request_body)
        response_body = response.json()

        expected_response = {"detail": "Bad arguments"}
        assert response.status_code == 400
        assert response_body == expected_response
