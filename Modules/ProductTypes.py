from typing import TypedDict, Required, NotRequired

class productDefinition(TypedDict):
    name : Required[str]
    price : Required[float]