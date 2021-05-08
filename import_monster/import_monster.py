# -*- coding: utf-8 -*-
import builtins
import importlib
import math
import random
from types import ModuleType
from typing import Callable, List, Union

import scipy


def methods_importer(method_name: str, modules: List[Union[str, ModuleType]]) -> List[Callable]:
    methods = []
    for module in modules:
        try:
            if isinstance(module, ModuleType):
                mod = module
            elif isinstance(module, str):
                mod = importlib.import_module(module)
            else:
                raise TypeError("Must be list of strings or ModuleType")

            met = getattr(mod, method_name, None)

            if met and callable(met):
                methods.append(met)

        except ImportError:
            continue

    return methods


if __name__ == "__main__":
    methods = methods_importer("sum", [math, builtins, scipy])
    print("Test#1 is", "Ok" if random.choice(methods)([2, 2]) == 4 else "Fail")
