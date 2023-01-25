# Exchange Util



### Задача: Реализовать консольную утилиту для взаимодействия со сторонним сервисом https://exchangerate.host/#/#docs

### Утилита должна содержать следующие функции:

- Получение списка валют
cmd symbols

- Конвертация из одной валюты в другую
cmd convert –from USD –to EUR 100
- История котировок за период
cmd history –from USD –to EUR –data_from 20220101 –date_to 20220201 100
(для этой команды использовать метод апи Historical rates, Time-series data не использовать)
Получение истории котировок параллельно с ограничением по количеству параллельных запросов.
Запросы не должны отправляться все сразу, если у нас количество дней 300, то одновременно исполняются только 10, остальные в это время ожидают своей очереди

### Стек: asyncio, aiohttp, argparser
### Алгоритм работы:
- Пользователь запускает программу с необходимыми параметрами
- Программа парсит параметры
- В зависимости от введенных параметров выполняет необходимую функцию
- После выполнения программа выводит результат пользователю в консоль
