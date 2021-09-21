import argparse

from .generator import (
    Generator,
    LIBRARY_ROOT_PATH,
)


def main():
    arg_parser = argparse.ArgumentParser(description="Python TDLib functions and types aiotdlib_generator")
    arg_parser.add_argument(
        "-o",
        dest="destination",
        required=False,
        help="Output directory",
        default=f"{LIBRARY_ROOT_PATH}/aiotdlib/api"
    )
    args = arg_parser.parse_args()
    Generator(args.destination).generate()


if __name__ == '__main__':
    main()
