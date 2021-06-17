# dynamic_import_2.py
import importlib
from types import ModuleType
from typing import List, Union, Optional, Callable


def methods_importer(method: str, modules: List[Union[str, ModuleType]]) -> Optional[object]:
    for module in modules:
        try:

            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError('Must be list of strings or ModuleType')

            met = getattr(mod, method, None)

            if met:
                return met

        except ImportError:
            continue

    return None


print(methods_importer("__call__", ["builtins"]))
# <built-in function __import__>

print(methods_importer("nothing", ["builtins"]))
# None

import math, builtins, scipy
print(methods_importer("callable", [math, builtins, scipy]))
# <built-in function sum>

#import sys

#print(sys.meta_path)
# [
#   <class '_frozen_importlib.BuiltinImporter'>,
#   <class '_frozen_importlib.FrozenImporter'>,
#   <class '_frozen_importlib_external.PathFinder'>
# ]
