import os
import platform
import re
import shutil
from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

SYSTEM_LIB_EXTENSION = {
    "darwin": "dylib",
    "linux": "so",
    "freebsd": "so",
}

# Architecture aliases for platform tags
ARCH_ALIASES = {
    "x86_64": "x86_64",
    "amd64": "x86_64",
    "aarch64": "arm64",  # Back to arm64 for macOS compatibility
    "arm64": "arm64",
    "arm64v8": "arm64",
}

# Architecture aliases for filenames
FILENAME_ARCH_ALIASES = {
    "x86_64": "amd64" if platform.system().lower() == "linux" else "x86_64",
    "amd64": "amd64" if platform.system().lower() == "linux" else "x86_64",
    "aarch64": "arm64",
    "arm64": "arm64",
    "arm64v8": "arm64",
}

# Minimum OS versions for different platforms
PLATFORM_TAGS = {
    ("darwin", "arm64"): "macosx_11_0_arm64",
    ("darwin", "x86_64"): "macosx_10_9_x86_64",
    ("linux", "aarch64"): "manylinux_2_28_aarch64",  # Now using aarch64 for Linux
    ("linux", "x86_64"): "manylinux_2_28_x86_64",
}


def get_macos_arch_from_env():
    """Get architecture from ARCHFLAGS environment variable for macOS."""
    archflags = os.environ.get("ARCHFLAGS", "")
    if not archflags:
        return None

    # Look for -arch xxx in ARCHFLAGS
    match = re.search(r"-arch\s+(\w+)", archflags)
    if not match:
        return None

    arch = match.group(1)
    return ARCH_ALIASES.get(arch, arch)


def get_normalized_arch(machine_name: str) -> str:
    """Normalize architecture name to unified format."""
    system = platform.system().lower()
    arch = ARCH_ALIASES.get(machine_name.lower(), machine_name.lower())

    # For Linux, convert arm64 to aarch64 for platform tags
    if system == "linux" and arch == "arm64":
        return "aarch64"

    return arch


def get_filename_arch(machine_name: str) -> str:
    """Get architecture name for use in filename."""
    return FILENAME_ARCH_ALIASES.get(machine_name.lower(), machine_name.lower())


def get_bundled_tdlib_filename():
    uname = platform.uname()
    system_name = uname.system.lower()
    machine_name = uname.machine.lower()

    # Check ARCHFLAGS for macOS
    if system_name == "darwin":
        env_arch = get_macos_arch_from_env()
        if env_arch:
            machine_name = env_arch

    # Get architecture name for filename
    machine_name = get_filename_arch(machine_name)
    extension = SYSTEM_LIB_EXTENSION.get(system_name)

    if not extension:
        return None

    # Generate filename in format libtdjson_{system}_{arch}.{ext}
    binary_name = f"libtdjson_{system_name}_{machine_name}.{extension}"
    return binary_name


class CustomHook(BuildHookInterface):
    PLUGIN_NAME = "hatch"

    def initialize(self, version, build_data):
        build_data["pure_python"] = False

        # Get platform according to specification
        system = platform.system().lower()
        machine = platform.machine().lower()

        # Check ARCHFLAGS for macOS
        if system == "darwin":
            env_arch = get_macos_arch_from_env()
            if env_arch:
                machine = env_arch

        # Normalize architecture for platform tag
        machine = get_normalized_arch(machine)

        # Get platform tag from predefined values
        platform_tag = PLATFORM_TAGS.get((system, machine))
        if not platform_tag:
            # Use safer format for unknown platforms
            platform_tag = f"{system.replace('-', '_')}_{machine.replace('-', '_')}"

        # Set tag in format py3-none-{platform_tag}
        build_data["tag"] = f"py3-none-{platform_tag}"

        # Get binary filename for current platform
        binary_filename = get_bundled_tdlib_filename()
        if not binary_filename:
            # Skip wheel build for unsupported platforms
            print(f"Skipping wheel build for unsupported platform: {platform_tag}")
            build_data["skip"] = True
            return

        # Create target directory if it doesn't exist
        target_dir = Path("aiotdlib/tdlib")
        target_dir.mkdir(parents=True, exist_ok=True)

        # Clean target directory from binary files
        for ext in SYSTEM_LIB_EXTENSION.values():
            for f in target_dir.glob(f"*.{ext}"):
                f.unlink()

        # Look for binary file in possible locations
        source_file = None
        tdlib_dir = Path(__file__).parent / "tdlib"
        if tdlib_dir.exists():
            binary_path = tdlib_dir / binary_filename
            if binary_path.exists():
                source_file = binary_path

        if not source_file:
            # Skip wheel build if binary file not found
            print(f"Binary file {binary_filename} not found, skipping wheel build")
            build_data["skip"] = True
            return

        target_file = target_dir / binary_filename
        print(f"Copying {source_file} to {target_file}")
        shutil.copy2(source_file, target_file)

    def finalize(self, version, build_data, artifact_path):
        pass


def finalize(version, build_data, artifact_path):
    pass
