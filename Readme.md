# Service description

Service for testing of functionality, base proxy service. Input data of this sevice is an image in base64 coding and target width and height for scaling, output also is image in base64 coding.

# Include service minimal interface

Description of interface which service should implement for interaction with proxy service

### /me

Its route return all required information about service

```json
{
  "service_name": "service_name", // str. Name of the service
  "service_description": "some description", // str. Some service description
  "arguments": [
    {
      "argument_name": "argument_name",
      "argument_description": "description",
      "type": "image" // mime type of argument
    },
    {
      "argument_name": "argument_name2",
      "argument_description": "description",
      "type": "text"
    }
  ]
}
```
