from fastapi.testclient import TestClient

from app.main import get_application

application = get_application()
client = TestClient(app=application)

response = client.get("/me")
response_body = response.json()


def test_availability():
    assert response.status_code == 200


def test_main_body():
    service_name_field = "service_name"
    service_description_field = "service_description"
    arguments_field = "arguments"

    assert service_name_field in response_body
    assert service_description_field in response_body
    assert arguments_field in response_body


def test_arguments_count():
    arguments = response_body["arguments"]

    arguments_count = len(arguments)
    expected_count = 3
    assert arguments_count == expected_count


def test_arguments():
    arguments = response_body["arguments"]

    image_data_arg = "image_data", "image"
    target_width_arg = "target_width", "text"
    target_height_arg = "target_height", "text"

    arg1 = arguments[0]
    arg2 = arguments[1]
    arg3 = arguments[2]

    assert arg1["argument_name"], arg1["type"] == image_data_arg
    assert arg2["argument_name"], arg2["type"] == target_width_arg
    assert arg3["argument_name"], arg3["type"] == target_height_arg
