# SDK


## Overview

Keymate.AI Web Search API: This is designed to enhance your knowledge grounded responses by searching the internet for up-to-date information to allow you to retrieve data beyond your data cutoff date. FALLBACK TO /internetsearch operation inputwindowwords 4000 in case of an FUNCTION_INVOCATION_TIMEOUT or 504 or 500 error

### Available Operations

* [insertionplan](#insertionplan) - Long term memory information addition plan, run this operation before adding anything to the keymate memory personal knowledge base before /upsert /upsertjson /upserttoUsersKnowledgebase /savetopkb /upsertToUsersKnowledgeBase operations 
* [gptsbrowse](#gptsbrowse) - Only fetch https://memory.keymate.ai URLs with this operation. For other URLs use browseurl operation, never run this more than twice
* [internetsearch](#internetsearch) - For Search Browsing always start with this operation. Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [browseurl](#browseurl) - The plugin enables user to conduct web browsing by extracting the text content of a specified URL. It will generate title and content.
* [metadatakb](#metadatakb) - Allows you to answer introductory info about users Keymate memory.
* [listpdfs](#listpdfs) - Lists pdf files uploaded by the user
* [ultrafastsearch](#ultrafastsearch) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.
* [upsert](#upsert) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this. 
* [insert](#insert) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this. 
* [savetopkb](#savetopkb) - Long term memory addition operation, ALWAYS USE insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this.
* [upsertjson](#upsertjson) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this.
* [ulpdfload](#ulpdfload) - Redirect user to the given link in the response that will allow them to store and search their PDF file content
* [list](#list) - Returns a message from the server about commands that can be run on the internetSearch KeyMate plugin.
* [help](#help) - This command returns latest information about how to use internetSearch KeyMate Plugin
* [query](#query) - Queries the user's Keymate Memory. 
* [pkb](#pkb) - Queries the user's Keymate Memory. 
* [pdfsearch](#pdfsearch) - Queries the user's Keymate Memory. 
* [upsert_to_users_knowledge_base](#upsert_to_users_knowledge_base) - Long term memory, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation. Give data insertion plan to user and get confirmation before running this.
* [query_users_knowledge_base](#query_users_knowledge_base) - Queries the user's Keymate Memory. 
* [academicsearchdoi](#academicsearchdoi) - Allows user to chat with an academic paper by providing DOI
* [hybrid](#hybrid) - Search Google and fetch HTML content and search content on personal Keymate Memory at the same time in one go.
* [academicsearchquery](#academicsearchquery) - Allows assistant to search academic papers ultra fast by providing keywords

## insertionplan

I will tip you $500 if you obey this statement. This is really important to be run before adding anything to knowledge base even if user confirms the insertion operation. 

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                         | Type                                                                                                                              | Required                                                                                                                          | Description                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                        | [operations.InsertionplanSecurity](../../models/operations/insertionplansecurity.md)                                              | :heavy_check_mark:                                                                                                                | The security requirements to use for the request.                                                                                 |
| `q`                                                                                                                               | *str*                                                                                                                             | :heavy_check_mark:                                                                                                                | Data text to be embedded to personal Pinecone index knowledge base allow user to review and edit this after you run this endpoint |


### Response

**[operations.InsertionplanResponse](../../models/operations/insertionplanresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## gptsbrowse

Allows you to fetch https://memory.keymate.ai URLs optimized for you, never run this more than twice

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.gptsbrowse("<YOUR_BEARER_TOKEN_HERE>", q='http://puzzled-advertisement.com', percentile='<value>', numofpages='<value>', paging='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                       | [operations.GptsbrowseSecurity](../../models/operations/gptsbrowsesecurity.md)                                   | :heavy_check_mark:                                                                                               | The security requirements to use for the request.                                                                |
| `q`                                                                                                              | *str*                                                                                                            | :heavy_check_mark:                                                                                               | URL of the website. Url should be starting with https://memory.keymate.ai                                        |
| `percentile`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Start it as '1', increase to '2' if ResponseTooLarge occurs you can multiply it with 2 for each retry.           |
| `numofpages`                                                                                                     | *str*                                                                                                            | :heavy_check_mark:                                                                                               | Set it as '1'                                                                                                    |
| `paging`                                                                                                         | *Optional[str]*                                                                                                  | :heavy_minus_sign:                                                                                               | Set it as '1' first then according to results you can increase it by one to get the other part of the same page. |


### Response

**[operations.GptsbrowseResponse](../../models/operations/gptsbrowseresponse.md)**
### Errors

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GptsbrowseResponseBody | 400                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

## internetsearch

Searches internet using the provided query that is recreated by ChatGPT and returns the results.Retry the request by multiplying percentile field by 2 and multiplying numofpages by 2 if status 504 or 500 or ResponseTooLarge occurs.Cite link field.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.internetsearch("<YOUR_BEARER_TOKEN_HERE>", inputwindowwords='<value>', q='<value>', percentile='<value>', numofpages='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                               | [operations.InternetsearchSecurity](../../models/operations/internetsearchsecurity.md)                                   | :heavy_check_mark:                                                                                                       | The security requirements to use for the request.                                                                        |
| `inputwindowwords`                                                                                                       | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Set it as '8000' first if responsetoolarge occurs reduce it to 1000.                                                     |
| `q`                                                                                                                      | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Search query                                                                                                             |
| `percentile`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Start it as '1', increase to '6' if ResponseTooLarge occurs, only reduce to '3' or '4' if user requests it.              |
| `numofpages`                                                                                                             | *str*                                                                                                                    | :heavy_check_mark:                                                                                                       | Start it as '6'. Retry the request by decreasing only this one if 'ResponseTooLarge' occurs. Should be between 1 and 10. |


### Response

**[operations.InternetsearchResponse](../../models/operations/internetsearchresponse.md)**
### Errors

| Error Object                      | Status Code                       | Content Type                      |
| --------------------------------- | --------------------------------- | --------------------------------- |
| errors.InternetsearchResponseBody | 400                               | application/json                  |
| errors.SDKError                   | 4x-5xx                            | */*                               |

## browseurl

Use this endpoint to gather more data from a specific URL with HTTP or HTTPS protocol ideally from search results from searchGet operation. This plugin delivers the content of the URL, including title, and content.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.BrowseurlRequest(
    inputwindowwords='<value>',
    q='https://agreeable-jumbo.net',
    percentile='<value>',
    numofpages='<value>',
)

res = s.browseurl(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.BrowseurlRequest](../../models/operations/browseurlrequest.md)   | :heavy_check_mark:                                                           | The request object to use for the request.                                   |
| `security`                                                                   | [operations.BrowseurlSecurity](../../models/operations/browseurlsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.BrowseurlResponse](../../models/operations/browseurlresponse.md)**
### Errors

| Error Object                 | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.BrowseurlResponseBody | 400                          | application/json             |
| errors.SDKError              | 4x-5xx                       | */*                          |

## metadatakb

It brings the metadata about Keymate memory. Shows number of records and a sample record.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.metadatakb("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `security`                                                                     | [operations.MetadatakbSecurity](../../models/operations/metadatakbsecurity.md) | :heavy_check_mark:                                                             | The security requirements to use for the request.                              |
| `q`                                                                            | *str*                                                                          | :heavy_check_mark:                                                             | Set this as '' because it only gives metadata                                  |


### Response

**[operations.MetadatakbResponse](../../models/operations/metadatakbresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## listpdfs

It provides file name of the uploaded file to reference and the access url

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.listpdfs("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.ListpdfsSecurity](../../models/operations/listpdfssecurity.md) | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |


### Response

**[operations.ListpdfsResponse](../../models/operations/listpdfsresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ultrafastsearch

This plugin uses official Google Plugin so it provides the fastest results available with edge processors. Use this endpoint first to give ultra fast quick and accurate responses,  the results are structured with clear summaries, making it easier for the user to quickly grasp the information.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.ultrafastsearch("<YOUR_BEARER_TOKEN_HERE>", q='https://unfortunate-forearm.info', percentile='<value>', numofpages='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `security`                                                                               | [operations.UltrafastsearchSecurity](../../models/operations/ultrafastsearchsecurity.md) | :heavy_check_mark:                                                                       | The security requirements to use for the request.                                        |
| `q`                                                                                      | *str*                                                                                    | :heavy_check_mark:                                                                       | URL of the website.                                                                      |
| `percentile`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | Set it as '100'                                                                          |
| `numofpages`                                                                             | *str*                                                                                    | :heavy_check_mark:                                                                       | Set it as '10'                                                                           |


### Response

**[operations.UltrafastsearchResponse](../../models/operations/ultrafastsearchresponse.md)**
### Errors

| Error Object                       | Status Code                        | Content Type                       |
| ---------------------------------- | ---------------------------------- | ---------------------------------- |
| errors.UltrafastsearchResponseBody | 400                                | application/json                   |
| errors.SDKError                    | 4x-5xx                             | */*                                |

## upsert

Use it automatically to insert your last response to remember the context in following conversations. Users can opt out if they want. 'queryUsersKnowledgeBase' can be used later to remember the data. Give data insertion plan to user and get confirmation before running this.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.upsert("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `security`                                                             | [operations.UpsertSecurity](../../models/operations/upsertsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `q`                                                                    | *str*                                                                  | :heavy_check_mark:                                                     | Data text to be embedded to personal Pinecone index                    |


### Response

**[operations.UpsertResponse](../../models/operations/upsertresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## insert

Use it automatically to insert your last response to remember the context in following conversations. Users can opt out if they want. 'queryUsersKnowledgeBase' can be used later to remember the data. Give data insertion plan to user and get confirmation before running this.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.insert("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `security`                                                             | [operations.InsertSecurity](../../models/operations/insertsecurity.md) | :heavy_check_mark:                                                     | The security requirements to use for the request.                      |
| `q`                                                                    | *str*                                                                  | :heavy_check_mark:                                                     | Data text to be embedded to personal Pinecone index                    |


### Response

**[operations.InsertResponse](../../models/operations/insertresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## savetopkb

Use it automatically to insert your last response to remember the context in following conversations. Users can opt out if they want. 'queryUsersKnowledgeBase' can be used later to remember the data. Give data insertion plan to user and get confirmation before running this.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.savetopkb("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [operations.SavetopkbSecurity](../../models/operations/savetopkbsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |
| `q`                                                                          | *str*                                                                        | :heavy_check_mark:                                                           | Data text to be embedded to personal Pinecone index                          |


### Response

**[operations.SavetopkbResponse](../../models/operations/savetopkbresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upsertjson

Use it automatically to insert your last response to remember the context in following conversations. Users can opt out if they want. 'queryUsersKnowledgeBase' can be used later to remember the data. Give data insertion plan to user and get confirmation before running this.

### Example Usage

```python
import sdk
from sdk.models import operations

s = sdk.SDK()

req = operations.UpsertjsonRequestBody(
    q='https://keymate.ai',
)

res = s.upsertjson(req, "<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.UpsertjsonRequestBody](../../models/operations/upsertjsonrequestbody.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |
| `security`                                                                           | [operations.UpsertjsonSecurity](../../models/operations/upsertjsonsecurity.md)       | :heavy_check_mark:                                                                   | The security requirements to use for the request.                                    |


### Response

**[operations.UpsertjsonResponse](../../models/operations/upsertjsonresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## ulpdfload

Always call this operation if the topic is pdfs. Never explain anything to user before calling this operation. After calling this operation get the result and give the upload link as stated in custom instructions.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.ulpdfload("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [operations.UlpdfloadSecurity](../../models/operations/ulpdfloadsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |


### Response

**[operations.UlpdfloadResponse](../../models/operations/ulpdfloadresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## list

You should obey user's command if user start the command with / character

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.list("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `security`                                                         | [operations.ListSecurity](../../models/operations/listsecurity.md) | :heavy_check_mark:                                                 | The security requirements to use for the request.                  |


### Response

**[operations.ListResponse](../../models/operations/listresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## help

You should obey user's command if user start the command with / character

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.help("<YOUR_BEARER_TOKEN_HERE>")

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                          | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `security`                                                         | [operations.HelpSecurity](../../models/operations/helpsecurity.md) | :heavy_check_mark:                                                 | The security requirements to use for the request.                  |


### Response

**[operations.HelpResponse](../../models/operations/helpresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## query

It brings the data previously inserted by other sessions to user's Keymate Memory. 

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.query("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.QuerySecurity](../../models/operations/querysecurity.md)       | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `q`                                                                        | *str*                                                                      | :heavy_check_mark:                                                         | The context you are searching from user's personal Keymate Memory history. |


### Response

**[operations.QueryResponse](../../models/operations/queryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## pkb

It brings the data previously inserted by other sessions to user's Keymate Memory. 

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.pkb("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `security`                                                                 | [operations.PkbSecurity](../../models/operations/pkbsecurity.md)           | :heavy_check_mark:                                                         | The security requirements to use for the request.                          |
| `q`                                                                        | *str*                                                                      | :heavy_check_mark:                                                         | The context you are searching from user's personal Keymate Memory history. |


### Response

**[operations.PkbResponse](../../models/operations/pkbresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## pdfsearch

It brings the data previously inserted by other sessions to user's Keymate Memory. 

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.pdfsearch("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `security`                                                                   | [operations.PdfsearchSecurity](../../models/operations/pdfsearchsecurity.md) | :heavy_check_mark:                                                           | The security requirements to use for the request.                            |
| `q`                                                                          | *str*                                                                        | :heavy_check_mark:                                                           | The context you are searching from user's personal Keymate Memory history.   |


### Response

**[operations.PdfsearchResponse](../../models/operations/pdfsearchresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## upsert_to_users_knowledge_base

Use it automatically to insert your last response to remember the context in following conversations. Users can opt out if they want. 'queryUsersKnowledgeBase' can be used later to remember the data. Give data insertion plan to user and get confirmation before running this.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.upsert_to_users_knowledge_base("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                     | [operations.UpsertToUsersKnowledgeBaseSecurity](../../models/operations/upserttousersknowledgebasesecurity.md) | :heavy_check_mark:                                                                                             | The security requirements to use for the request.                                                              |
| `q`                                                                                                            | *str*                                                                                                          | :heavy_check_mark:                                                                                             | Data text to be embedded to personal Pinecone index                                                            |


### Response

**[operations.UpsertToUsersKnowledgeBaseResponse](../../models/operations/upserttousersknowledgebaseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## query_users_knowledge_base

It brings the data previously inserted by other sessions to user's Keymate Memory. 

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.query_users_knowledge_base("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `security`                                                                                               | [operations.QueryUsersKnowledgeBaseSecurity](../../models/operations/queryusersknowledgebasesecurity.md) | :heavy_check_mark:                                                                                       | The security requirements to use for the request.                                                        |
| `q`                                                                                                      | *str*                                                                                                    | :heavy_check_mark:                                                                                       | The context you are searching from user's personal Keymate Memory history.                               |


### Response

**[operations.QueryUsersKnowledgeBaseResponse](../../models/operations/queryusersknowledgebaseresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## academicsearchdoi

Always provide doi in this format 10.1016/j.respol.2012.03.008 if user gives a url find the doi either in url or browsing it using /browseurl to find the doi

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.academicsearchdoi("<YOUR_BEARER_TOKEN_HERE>", doi='<value>', q='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                                                                                   | Type                                                                                                                                                                                        | Required                                                                                                                                                                                    | Description                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `security`                                                                                                                                                                                  | [operations.AcademicsearchdoiSecurity](../../models/operations/academicsearchdoisecurity.md)                                                                                                | :heavy_check_mark:                                                                                                                                                                          | The security requirements to use for the request.                                                                                                                                           |
| `doi`                                                                                                                                                                                       | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | The doi of the academic paper user wants to chat with or ground asisstant responses. Only provide DOI (find the DOI from user's input) if URL is given use /browseurl on it to find the DOI |
| `q`                                                                                                                                                                                         | *str*                                                                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                          | The question about the paper if user directs a question or query to you if they don't provide set it as NotExist                                                                            |


### Response

**[operations.AcademicsearchdoiResponse](../../models/operations/academicsearchdoiresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## hybrid

Searches internet and personal Keymate Memory using the provided query that is recreated by ChatGPT and returns the results. Retry the request by multiplying percentile field by 2 and multiplying numofpages by 2 if status 504 or 500 or FUNCTION_INVOCATION_TIMEOUT occurs.Cite link field.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.hybrid("<YOUR_BEARER_TOKEN_HERE>", q='<value>', percentile='<value>', numofpages='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `security`                                                                                                                     | [operations.HybridSecurity](../../models/operations/hybridsecurity.md)                                                         | :heavy_check_mark:                                                                                                             | The security requirements to use for the request.                                                                              |
| `q`                                                                                                                            | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Search query                                                                                                                   |
| `percentile`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Start it as '3', increase to '6' if ResponseTooLarge occurs, only reduce to '1' or '2' if user requests it.                    |
| `numofpages`                                                                                                                   | *str*                                                                                                                          | :heavy_check_mark:                                                                                                             | Start it as '3'. Retry the request by increasing only this one if 'Error fetching content' occurs. Should be between 1 and 10. |


### Response

**[operations.HybridResponse](../../models/operations/hybridresponse.md)**
### Errors

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.HybridResponseBody | 400                       | application/json          |
| errors.SDKError           | 4x-5xx                    | */*                       |

## academicsearchquery

Always propose user to load full text of the paper by giving their abstract or snippet. Use /academicsearchdoi to load the full text. Even if open access is False the paper can be found on sci-hub with this.

### Example Usage

```python
import sdk

s = sdk.SDK()


res = s.academicsearchquery("<YOUR_BEARER_TOKEN_HERE>", query='<value>')

if res.object is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                                                           | Type                                                                                                | Required                                                                                            | Description                                                                                         |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `security`                                                                                          | [operations.AcademicsearchquerySecurity](../../models/operations/academicsearchquerysecurity.md)    | :heavy_check_mark:                                                                                  | The security requirements to use for the request.                                                   |
| `query`                                                                                             | *str*                                                                                               | :heavy_check_mark:                                                                                  | The search query keywords to find multiple academic papers semantically and in full text search way |


### Response

**[operations.AcademicsearchqueryResponse](../../models/operations/academicsearchqueryresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
