import platform
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


SYSTEM_LIB_EXTENSION = {
    "darwin": "dylib",
    "linux": "so",
    "freebsd": "so",
}

ARCH_ALIASES = {
    "x86_64": "amd64",
    "aarch64": "arm64",
    "arm64v8": "arm64",
}


def get_bundled_tdlib_filename():
    uname = platform.uname()
    system_name = uname.system.lower()
    machine_name = uname.machine.lower()
    machine_name = ARCH_ALIASES.get(machine_name, machine_name)
    extension = SYSTEM_LIB_EXTENSION.get(system_name)

    if not bool(extension):
        raise RuntimeError("Prebuilt TDLib binary is not included for this system")

    binary_name = f"libtdjson_{system_name}_{machine_name}.{extension}"
    return binary_name


class CustomHook(BuildHookInterface):
    PLUGIN_NAME = "hatch"

    def initialize(self, version, build_data):
        build_data["pure_python"] = False
        build_data["tag"] = (
            f"py3-none-{platform.system().lower()}_{platform.machine().lower()}"
        )
        dest.hardlink_to(tdlib_path)

    def finalize(self, version, build_data, artifact_path):
        dest.unlink()


TDLIB_PREBUILT_PATH = Path(__file__).parent / "tdlib"

filename = get_bundled_tdlib_filename()

tdlib_path = TDLIB_PREBUILT_PATH / filename
dest = Path("aiotdlib/tdlib") / filename
