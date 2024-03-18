"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class ListSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListStatus:
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""/internetsearch : Searches the internet using a provided query and returns results, including HTML content and PDF summaries from the links.
    /ultrafastsearch: Provides ultra-fast search results from multiple sources, giving a comprehensive view with structured summaries.
    /browseurl: Extracts the text content of a specified URL, generating title and content.
    /upsert, /savetopkb, /upsertToUsersKnowledgeBase: Inserts the last response to remember the context in following conversations, enhancing the user's personal Keymate Memory.
    /query and /pkb, /pdfsearch: Queries the user's Keymate Memory to understand user's intent, context, preferences from previously inserted data.
    /help: Returns a message explaining how to use the internetSearch plugin.
    /list: Returns a message listing the available commands that can be run on the internetSearch plugin.
    /ulpdfload: Returns a message providing a URL where users can upload their PDF files.
    academicsearchdoi: Allows you to load an academic paper with given DOI, ChatGPT uses the whole text to answer you.
    academicsearchquery: Allows you to search for academic papers with given text, then you can load any paper's full text with it's DOI.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListResponseBody:
    r"""Successful operation"""
    status: Optional[ListStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class ListResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[ListResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    
