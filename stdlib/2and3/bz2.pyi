import io
import sys
from os.path import _PathType
from typing import IO, Any, Optional, TextIO, Union, overload

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

_PathOrFile = Union[_PathType, IO[bytes]]

def compress(data: bytes, compresslevel: int = ...) -> bytes: ...
def decompress(data: bytes) -> bytes: ...

if sys.version_info >= (3, 3):
    if sys.version_info >= (3, 4):
        # Changed in version 3.4: The 'x' (exclusive creation) mode was added.
        _OPEN_BINARY_MODE = Literal["r", "rb", "w", "wb", "x", "xb", "a", "ab"]
        _OPEN_TEXT_MODE = Literal["rt", "wt", "xt", "at"]
    else:
        _OPEN_BINARY_MODE = Literal["r", "rb", "w", "wb", "a", "ab"]
        _OPEN_TEXT_MODE = Literal["rt", "wt", "at"]
    @overload
    def open(
        filename: _PathOrFile,
        mode: _OPEN_BINARY_MODE = ...,
        compresslevel: int = ...,
        encoding: None = ...,
        errors: None = ...,
        newline: None = ...,
    ) -> BZ2File: ...
    @overload
    def open(
        filename: _PathType,
        mode: _OPEN_TEXT_MODE,
        compresslevel: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> TextIO: ...
    @overload
    def open(
        filename: _PathOrFile,
        mode: str = ...,
        compresslevel: int = ...,
        encoding: Optional[str] = ...,
        errors: Optional[str] = ...,
        newline: Optional[str] = ...,
    ) -> Union[BZ2File, TextIO]: ...

class BZ2File(io.BufferedIOBase, IO[bytes]):  # type: ignore  # python/mypy#5027
    def __init__(
        self, filename: _PathOrFile, mode: str = ..., buffering: Optional[Any] = ..., compresslevel: int = ...
    ) -> None: ...

class BZ2Compressor(object):
    def __init__(self, compresslevel: int = ...) -> None: ...
    def compress(self, data: bytes) -> bytes: ...
    def flush(self) -> bytes: ...

class BZ2Decompressor(object):
    if sys.version_info >= (3, 5):
        def decompress(self, data: bytes, max_length: int = ...) -> bytes: ...
    else:
        def decompress(self, data: bytes) -> bytes: ...
    if sys.version_info >= (3, 3):
        @property
        def eof(self) -> bool: ...
    if sys.version_info >= (3, 5):
        @property
        def needs_input(self) -> bool: ...
    @property
    def unused_data(self) -> bytes: ...
