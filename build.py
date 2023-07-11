# script to pick up the appropriate precompiled tdlib binary when
# building a python wheel for pypi.
# this is referenced in build.py and should not be called manually

import platform
import tempfile
import traceback
import warnings
from functools import partial
from pathlib import Path
from subprocess import run

ARCH_ALIASES = {
    "x86_64": "amd64",
    "aarch64": "arm64",
    "arm64v8": "arm64",
}

SYSTEM_LIB_EXTENSION = {
    "darwin": "dylib",
    "linux": "so",
    "freebsd": "so",
}


TDLIB_TAG = "aiotdlib_0.20.0"
TDLIB_REPO = "https://github.com/pylakey/td"
BINARIES_DIR = Path("__file__").parent / "tdlib"


def build(tdlib: Path):
    with tempfile.TemporaryDirectory() as d:
        do = partial(run, check=True)
        do(["git", "clone", TDLIB_REPO, "--depth", "1", "--branch", TDLIB_TAG], cwd=d)
        build_dir = Path(d) / "td" / "build"
        install_dir = Path(d) / "td" / "install"
        build_dir.mkdir()
        install_dir.mkdir()
        do(
            [
                "cmake",
                "-DCMAKE_BUILD_TYPE=Release",
                f"-DCMAKE_INSTALL_PREFIX:PATH={install_dir}",
                "-DTD_ENABLE_LTO=ON",
                "..",
            ],
            cwd=build_dir,
        )
        do(["cmake", "--build", ".", "--target", "install"], cwd=build_dir)
        built = next(install_dir.glob("lib/libtdjson*"))
        built.link_to(tdlib)


def get_binary_name():
    uname = platform.uname()
    system_name = uname.system.lower()
    machine_name = uname.machine.lower()
    machine_name = ARCH_ALIASES.get(machine_name, machine_name)
    extension = SYSTEM_LIB_EXTENSION.get(system_name)
    return f"libtdjson_{system_name}_{machine_name}.{extension}"


def main():
    binary_name = get_binary_name()
    dest = Path(".") / "aiotdlib" / "tdlib"
    out = dest / binary_name
    if out.exists():
        return

    tdlib = BINARIES_DIR / binary_name
    if not tdlib.exists():
        try:
            build(tdlib)
        except Exception as e:
            warnings.warn(
                "Could not build TDlib, you will have to pass "
                "library_path= in the Client constructor."
            )
            traceback.print_exception(e)
            exit(0)

    dest.mkdir(exist_ok=True)
    tdlib.link_to(out)


if __name__ == "__main__":
    main()
