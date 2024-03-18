# Keymate-API

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install openapi
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import sdk

s = sdk.SDK()


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [SDK](docs/sdks/sdk/README.md)

* [insertionplan](docs/sdks/sdk/README.md#insertionplan) - Long term memory information addition plan, run this operation before adding anything to the keymate memory personal knowledge base before /upsert /upsertjson /upserttoUsersKnowledgebase /savetopkb /upsertToUsersKnowledgeBase operations 
* [gptsbrowse](docs/sdks/sdk/README.md#gptsbrowse) - Only fetch https://memory.keymate.ai URLs with this operation. For other URLs use browseurl operation, never run this more than twice
* [internetsearch](docs/sdks/sdk/README.md#internetsearch) - For Search Browsing always start with this operation. Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [browseurl](docs/sdks/sdk/README.md#browseurl) - The plugin enables user to conduct web browsing by extracting the text content of a specified URL. It will generate title and content.
* [metadatakb](docs/sdks/sdk/README.md#metadatakb) - Allows you to answer introductory info about users Keymate memory.
* [listpdfs](docs/sdks/sdk/README.md#listpdfs) - Lists pdf files uploaded by the user
* [ultrafastsearch](docs/sdks/sdk/README.md#ultrafastsearch) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.
* [upsert](docs/sdks/sdk/README.md#upsert) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this. 
* [insert](docs/sdks/sdk/README.md#insert) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this. 
* [savetopkb](docs/sdks/sdk/README.md#savetopkb) - Long term memory addition operation, ALWAYS USE insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this.
* [upsertjson](docs/sdks/sdk/README.md#upsertjson) - Long term memory addition operation, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation before running this. Give data insertion plan to user and get confirmation before running this.
* [ulpdfload](docs/sdks/sdk/README.md#ulpdfload) - Redirect user to the given link in the response that will allow them to store and search their PDF file content
* [list](docs/sdks/sdk/README.md#list) - Returns a message from the server about commands that can be run on the internetSearch KeyMate plugin.
* [help](docs/sdks/sdk/README.md#help) - This command returns latest information about how to use internetSearch KeyMate Plugin
* [query](docs/sdks/sdk/README.md#query) - Queries the user's Keymate Memory. 
* [pkb](docs/sdks/sdk/README.md#pkb) - Queries the user's Keymate Memory. 
* [pdfsearch](docs/sdks/sdk/README.md#pdfsearch) - Queries the user's Keymate Memory. 
* [upsert_to_users_knowledge_base](docs/sdks/sdk/README.md#upsert_to_users_knowledge_base) - Long term memory, ALWAYS USE Call the searchweb.keymate.ai API with the insertionplan operation. Give data insertion plan to user and get confirmation before running this.
* [query_users_knowledge_base](docs/sdks/sdk/README.md#query_users_knowledge_base) - Queries the user's Keymate Memory. 
* [academicsearchdoi](docs/sdks/sdk/README.md#academicsearchdoi) - Allows user to chat with an academic paper by providing DOI
* [hybrid](docs/sdks/sdk/README.md#hybrid) - Search Google and fetch HTML content and search content on personal Keymate Memory at the same time in one go.
* [academicsearchquery](docs/sdks/sdk/README.md#academicsearchquery) - Allows assistant to search academic papers ultra fast by providing keywords
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                  | Status Code                   | Content Type                  |
| ----------------------------- | ----------------------------- | ----------------------------- |
| errors.GptsbrowseResponseBody | 400                           | application/json              |
| errors.SDKError               | 4x-5xx                        | */*                           |

### Example

```python
import sdk
from sdk.models import errors

s = sdk.SDK()


res = None
try:
    res = s.gptsbrowse("<YOUR_BEARER_TOKEN_HERE>", q='http://puzzled-advertisement.com', percentile='<value>', numofpages='<value>', paging='<value>')
except errors.GptsbrowseResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://searchweb.keymate.ai` | None |

#### Example

```python
import sdk

s = sdk.SDK(
    server_idx=0,
)


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import sdk

s = sdk.SDK(
    server_url="https://searchweb.keymate.ai",
)


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import sdk
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = sdk.SDK(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:


### Per-Operation Security Schemes

Some operations in this SDK require the security scheme to be specified at the request level. For example:
```python
import sdk

s = sdk.SDK()


res = s.insertionplan("<YOUR_BEARER_TOKEN_HERE>", q='<value>')

if res.object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
