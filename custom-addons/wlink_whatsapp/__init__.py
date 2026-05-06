# -*- coding: utf-8 -*-
# =============================================================================
# pycompileo2 runtime loader — AUTO-GENERATED, DO NOT EDIT
# =============================================================================
# This file detects the running Python version and imports the addon's
# pre-compiled business logic from the matching py{major}{minor}/ directory.
# =============================================================================
import importlib
import os
import sys

_ADDON_DIR = os.path.dirname(os.path.abspath(__file__))
_PY_TAG = "py{}{}".format(sys.version_info.major, sys.version_info.minor)
_COMPILED_DIR = os.path.join(_ADDON_DIR, _PY_TAG)

_SUPPORTED_VERSIONS = ['3.10', '3.11', '3.12', '3.13', '3.14']

if not os.path.isdir(_COMPILED_DIR):
    _current = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    raise ImportError(
        "pycompileo2: No compiled bytecode for Python {}.\n"
        "Supported versions: {}\n"
        "Compiled directory not found: {}".format(
            _current,
            ", ".join(sorted(_SUPPORTED_VERSIONS)),
            _COMPILED_DIR,
        )
    )

# Extend this package's __path__ so that relative imports
# (e.g. "from . import models") resolve to the compiled subtree.
if _COMPILED_DIR not in __path__:
    __path__.insert(0, _COMPILED_DIR)

# Parse the original __init__.py for import statements and execute them
# via importlib to avoid circular import issues with exec().
_init_in_compiled = os.path.join(_COMPILED_DIR, "__init__.py")
if os.path.isfile(_init_in_compiled):
    with open(_init_in_compiled) as _f:
        for _line in _f:
            _line = _line.strip()
            if _line.startswith("from . import "):
                _names = _line[len("from . import "):].split(",")
                for _n in _names:
                    _n = _n.strip()
                    if _n:
                        importlib.import_module("." + _n, __name__)
            elif _line.startswith("from .") and " import " in _line:
                _parts = _line.split(" import ", 1)
                _pkg = _parts[0].replace("from ", "").strip()
                importlib.import_module(_pkg, __name__)
            elif _line.startswith("import "):
                exec(_line)
else:
    # Fallback: import all subdirectories and .py files
    for _entry in sorted(os.listdir(_COMPILED_DIR)):
        _full = os.path.join(_COMPILED_DIR, _entry)
        if _entry == "__init__.py":
            continue
        if os.path.isdir(_full) or _entry.endswith(".py"):
            _mod_name = _entry[:-3] if _entry.endswith(".py") else _entry
            try:
                importlib.import_module("." + _mod_name, __name__)
            except ImportError:
                pass
