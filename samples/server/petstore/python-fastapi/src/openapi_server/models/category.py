# coding: utf-8

from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class Category(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    Category - a model defined in OpenAPI

        id: The id of this Category [Optional].
        name: The name of this Category [Optional].
    """

    id: Optional[int] = None
    name: Optional[str] = None

    @validator("name")
    def name_pattern(cls, value):
        assert value is not None and re.match(r"^[a-zA-Z0-9]+[a-zA-Z0-9\.\-_]*[a-zA-Z0-9]+$", value)
        return value
