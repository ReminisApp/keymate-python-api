"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class SavetopkbSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclasses.dataclass
class SavetopkbRequest:
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""Data text to be embedded to personal Pinecone index"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavetopkbStatus:
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The result of the operation"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SavetopkbResponseBody:
    r"""Successful operation"""
    status: Optional[SavetopkbStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class SavetopkbResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[SavetopkbResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    

