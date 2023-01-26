import aiohttp
import asyncio
import sys

from .date import get_date_list


async def get_currency_list():
    url = 'https://api.exchangerate.host/latest'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_text = await response.json()
            currences = list(response_text["rates"].keys())
            return currences


async def print_excange_with_date_range(start_date, end_date, from_symbols, to_symbols, amount):

    async def get_excange(session, url, sem, params):
        async with sem:
            async with session.get(url, params=params) as response:
                response_json = await response.json()
                return response_json

    from_symbols = from_symbols.upper()
    to_symbols = to_symbols.upper()
    symbols_list = await get_currency_list()

    if from_symbols not in symbols_list or to_symbols not in symbols_list:
        print("Incorrect currency symbols, exiting...")
        sys.exit()

    try:
        date_list = get_date_list(start_date, end_date)
    except ValueError:
        print("Incorrect date input, exiting...")
        sys.exit()

    sem = asyncio.Semaphore(10)
    params = {"base": f"{from_symbols}",
              "symbols": f"{to_symbols}", "amount": f"{amount}"}

    async with aiohttp.ClientSession() as session:
        tasks = []
        for date in date_list:
            url = f"https://api.exchangerate.host/{date}"
            tasks.append(asyncio.ensure_future(
                get_excange(session, url, sem, params)))

        exchange_list = await asyncio.gather(*tasks)
        for item in exchange_list:
            exchange_date = item["date"].replace("-", ".")
            exchange_value = item["rates"][f"{to_symbols}"]
            print(
                f"{exchange_date} exchange rate from {amount} {from_symbols} to {to_symbols} = {exchange_value}")


async def print_exchange_rate(from_symbols="USD", to_symbols="RUB", amount=1):
    
    from_symbols = from_symbols.upper()
    to_symbols = to_symbols.upper()
    url = "https://api.exchangerate.host/convert/"
    params = {"from": f"{from_symbols}",
              "to": f"{to_symbols}", "amount": f"{amount}"}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response_json = await response.json()
            if not response_json["result"]:
                print("Incorrect currency symbols, exiting...")
                sys.exit()
            exchange_value = response_json["result"]
            print(
                f"Today exchange value from {amount} {from_symbols} to {to_symbols} = {exchange_value}")
