# Exchange Util

### Утилита содержит следующие функции:

- Получение списка валют
`exchange symbols`
- Конвертация из одной валюты в другую
`exchange convert --from USD --to EUR 100`
- История котировок за период
`exchange history --from USD --to EUR --date_from 20220101 --date_to 20220201 100`

### Стек: asyncio, aiohttp, argparser
