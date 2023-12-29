from __future__ import annotations
import json
from typing import Any, Dict
from pydantic import RootModel, field_validator
from datetime import datetime

DATE = "%Y-%m-%d"
TIME = "%H:%M:%S"
DATETIME = f"{DATE} {TIME}"


class TableValue(RootModel):
    @property
    def link(self) -> str:
        return self.root["link"]

    @property
    def display_value(self) -> Any:
        return self.root["display_value"]

    @property
    def value(self) -> Any:
        return self.root["value"]

    @field_validator("*", mode="before")
    def val(cls, v, field):
        v = cls._initialize_dict(v)
        return v

    @field_validator("*", mode="after")
    def val1(cls, v: Dict, field):
        v = cls._process_dict(v)
        return v

    @staticmethod
    def _initialize_dict(v):
        if not isinstance(v, dict):
            v = {"link": None, "value": v, "display_value": None}

        if not v.get("link", None):
            v["link"] = None
        if not v.get("value", None):
            v["value"] = None
        if not v.get("display_value", None):
            v["display_value"] = None

        return v

    @staticmethod
    def _process_dict(v: Dict):
        for key, value in v.items():
            if value == "":
                value = None
            if value is not None:
                value = TableValue._try_json_loads(value)
                value = TableValue._try_datetime_parse(value)
            v[key] = value

        return v

    @staticmethod
    def _try_json_loads(value):
        try:
            value = json.loads(value)
        except Exception:
            pass
        return value

    @staticmethod
    def _try_datetime_parse(value):
        try:
            value = datetime.strptime(value, DATETIME)
        except Exception:
            pass
        return value
