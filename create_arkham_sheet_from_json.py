#!/usr/bin/env python3

# TODO: add module description

import sys
from arkham_data import load_set
from arkham_sheets import create_spreadsheet_for_set

# from json
def main():
    if len(sys.argv) < 2:
        print("args: path of json file containing set data")
        return

    path = sys.argv[1]
    arkhamset = load_set(path)

    spreadsheet_url = create_spreadsheet_for_set(arkhamset)
    print('Spreadsheet URL: {0}'.format(spreadsheet_url))


if __name__ == '__main__':
    main()
