from typing import Optional, Union

from pydantic import BaseModel


class MetadataFilterItem(BaseModel):

    """
    Metadata Filter.
    """
    key: str
    '''
     field condition 
     e.g. 
        FieldCondition
            Match 
                MatchValue - str, int, bool
                MatchText - str
                MatchAny - list[str], list[int]
                MatchExcept - list[str], list[int]
            Range 
                le - float
                lt - float
                ge - float
                gt - float 
    '''
    field_condition: str
    value_selector: Optional[list[str]] = None
    arg: Optional[Union[str, int, bool, float, list[str], list[int]]] = None


class MetadataFilterConfig(BaseModel):
    """
    Metadata Filter Config.
    """
    filter_items: list[MetadataFilterItem]