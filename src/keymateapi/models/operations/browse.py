"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from keymateapi import utils
from typing import Any, Dict, Optional


@dataclasses.dataclass
class BrowseRequest:
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""URL starting with https://memory.keymate.ai. Must be a valid URL."""
    percentile: str = dataclasses.field(default='1', metadata={'query_param': { 'field_name': 'percentile', 'style': 'form', 'explode': True }})
    r"""For adjusting response scope in case of 'ResponseTooLarge' error. Starts with 1."""
    numofpages: str = dataclasses.field(default='1', metadata={'query_param': { 'field_name': 'numofpages', 'style': 'form', 'explode': True }})
    r"""Specifies the number of pages to return. Starts with 1 by default."""
    paging: Optional[str] = dataclasses.field(default='1', metadata={'query_param': { 'field_name': 'paging', 'style': 'form', 'explode': True }})
    r"""Used for pagination. Increments for subsequent pages."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseResponseResponseBody:
    r"""Generic or unexpected error."""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Results:
    UNSET='__SPEAKEASY_UNSET__'
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the search result"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""The URL of the search result"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""A summary of the HTML content of the search result"""
    full_content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_content'), 'exclude': lambda f: f is None }})
    r"""The entire HTML content of the search result (available for the first three results)"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseResponseBody:
    r"""Successful operation. Returns fetched results along with applicable rules."""
    currentkeymateuser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currentkeymateuser'), 'exclude': lambda f: f is None }})
    notice_for_human: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('noticeForHuman'), 'exclude': lambda f: f is None }})
    results: Optional[Results] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    rules: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class BrowseResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    two_hundred_application_json_object: Optional[BrowseResponseBody] = dataclasses.field(default=None)
    r"""Successful operation. Returns fetched results along with applicable rules."""
    default_application_json_object: Optional[BrowseResponseResponseBody] = dataclasses.field(default=None)
    r"""Generic or unexpected error."""
    
