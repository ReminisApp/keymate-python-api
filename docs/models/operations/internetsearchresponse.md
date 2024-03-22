# InternetsearchResponse


## Fields

| Field                                                                                                                    | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `http_meta`                                                                                                              | [components.HTTPMetadata](../../models/components/httpmetadata.md)                                                       | :heavy_check_mark:                                                                                                       | N/A                                                                                                                      |
| `two_hundred_application_json_object`                                                                                    | [Optional[operations.InternetsearchResponseBody]](../../models/operations/internetsearchresponsebody.md)                 | :heavy_minus_sign:                                                                                                       | Successful search operation. Returns data based on query and user's plan.                                                |
| `default_application_json_object`                                                                                        | [Optional[operations.InternetsearchResponseResponseBody]](../../models/operations/internetsearchresponseresponsebody.md) | :heavy_minus_sign:                                                                                                       | Generic or unexpected error.                                                                                             |