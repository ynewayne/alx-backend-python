#!/usr/bin/env python3
from typing import TypeVar, Mapping, Any, Union

# Define a TypeVar for the return type
T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary based on the key.
    
    Args:
        dct (Mapping): The dictionary from which to retrieve the value.
        key (Any): The key to search for in the dictionary.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.
        
    Returns:
        Union[Any, T]: The value associated with the key if found, otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
