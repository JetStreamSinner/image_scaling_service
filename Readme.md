# Service description
# Include service minimal interface

Description of interface which service should implement for interaction with proxy service

### /me

Its route return all required information about service

```json
{
  "name": "service_name", // str. Name of the service
  "description": "some description", // str. Some service description
  "input": [
    {
      "argument_name": "argument_name",
      "argument_description": "description",
      "type": "image"
    },
    {
      "argument_name": "argument_name2",
      "argument_description": "description",
      "type": "int"
    }
  ]
}
```