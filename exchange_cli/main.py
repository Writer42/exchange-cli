import argparse
import asyncio

from .columns import print_text_in_columns


from .api import (
    get_currency_list,
    print_exchange_rate,
    print_excange_with_date_range
)


def parse():
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    symbols = subparser.add_parser("symbols", help="get all currency symbols")
    convert = subparser.add_parser(
        "convert", help="convert from one currency to another")
    history = subparser.add_parser(
        "history", help="show conversion rate for range of dates")

    convert.add_argument("--from", dest="from_symbols",
                        required=True, help="from currency code")
    convert.add_argument("--to", dest="to_symbols",
                        required=True, help="to currency code")
    convert.add_argument("amount", type=int, help="amount of currency to exchange")

    history.add_argument("--from", dest="from_symbols",
                        required=True, help="from currency code")
    history.add_argument("--date_from", required=True)
    history.add_argument("--date_to", required=True)
    history.add_argument("--to", dest="to_symbols",
                        required=True, help="to currency code")
    history.add_argument("amount", type=int, help="amount of currency to exchange")

    args = parser.parse_args()

    if args.command == "symbols":
        symbols_list = asyncio.run(get_currency_list())
        print_text_in_columns(symbols_list)
        

    elif args.command == "convert":
        asyncio.run(print_exchange_rate(
            args.from_symbols, args.to_symbols, args.amount))
    elif args.command == "history":
        asyncio.run(print_excange_with_date_range(args.date_from,
                    args.date_to, args.from_symbols, args.to_symbols, args.amount))
    else:
        parser.print_help()

