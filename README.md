# Range generator

Generate a simple ranges with your terminal.

## Requirements

- Python (python3 as python or as python3 in your PATH)
- Python Module: cli-app

## Installing

First install the dependencies, if your python3 is in the
PATH as python3, use pip3 else use pip

```sh
pip install cli-app # or pip3 install cli-app
```

Then install the app with curl:

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/range-generator/main/install.py | python # or python3
# ...
```

## Uninstalling

To uninstall use:

```sh
curl -sL https://raw.githubusercontent.com/AlphaTechnolog/range-generator/main/uninstall.py | python # or python3
```

## Using

To get help use:

```sh
range --help
```

To generate a range starting in 1 and ending in 10 use:

```sh
range gen-number
```

To specify an end and start fields use the -s / --start and -e / --end
flags, use:

```sh
range gen-number -s 10 -e 100
10 ... 100
range gen-number -s 4
4 ... 10
range gen-number -e 3
1 ... 3
```

To generate an alphabetic range starting in 'a' and ending in 'z', use:

```sh
range gen-alphabet
```

To specify an end and start fields use the -s / --start and -e / --end
flags, use:

```sh
range gen-alphabet -s d -e w
d ... w
range gen-alphabet -s d
d ... z
range gen-alphabet -e d
a ... d
```

## Enjoy

Thanks for use range to generate a simple ranges with your terminal!
