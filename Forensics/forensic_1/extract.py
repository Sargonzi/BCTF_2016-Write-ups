import contextlib
import lzma
import tarfile

with contextlib.closing(lzma.LZMAFile('50-flag.tar.xz')) as xz:
    with tarfile.open(fileobj=xz) as f:
        f.extractall('.')
