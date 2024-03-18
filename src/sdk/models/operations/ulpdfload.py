"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ...models.components import httpmetadata as components_httpmetadata
from dataclasses_json import Undefined, dataclass_json
from sdk import utils
from typing import Optional


@dataclasses.dataclass
class UlpdfloadSecurity:
    bearer_auth: str = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer', 'field_name': 'Authorization' }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UlpdfloadStatus:
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""You will receive a response like this when you call this operation use the operation's result. To upload PDF files, please visit https://ln.keymate.ai/keyword [https://ln.keymate.ai/keyword]"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UlpdfloadResponseBody:
    r"""Successful operation"""
    status: Optional[UlpdfloadStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class UlpdfloadResponse:
    http_meta: components_httpmetadata.HTTPMetadata = dataclasses.field()
    object: Optional[UlpdfloadResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    
