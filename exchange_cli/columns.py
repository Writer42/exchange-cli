from rich import print
from rich.columns import Columns


def print_text_in_columns(text_list):

    columns = Columns(text_list)
    print(columns)