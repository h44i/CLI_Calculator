import argparse
import sys

from toolkit.calculator import evaluate
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def main():
    parser = argparse.ArgumentParser(prog="toolkit")
    subparsers = parser.add_subparsers(dest="command")

    calc_parser = subparsers.add_parser(
        "calc",
        help="вычислить арифметическое выражение",
    )
    calc_parser.add_argument("EXPRESSION", type=str)

    convert_parser = subparsers.add_parser(
        "convert",
        help="конвертировать единицы измерения",
    )
    convert_parser.add_argument("VALUE", type=float)
    convert_parser.add_argument(
        "--from", dest="from_unit", metavar="UNIT", required=True
    )
    convert_parser.add_argument("--to", dest="to_unit", metavar="UNIT", required=True)

    args = parser.parse_args()

    try:
        if args.command == "calc":
            result = evaluate(args.EXPRESSION)
            print(result)

        elif args.command == "convert":
            result = convert(args.VALUE, args.from_unit, args.to_unit)
            print(result)

    except ToolkitError as e:
        print(e, file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()
