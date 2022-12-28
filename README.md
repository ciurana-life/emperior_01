# Emperior 01
Small python script for downloading stock data into a csv file.

## Prerequisites
- Python 3.6+
- [Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer)
- Then you need to install the dependencies `poetry install`
- You can also create a virtualenv and run `pip install .` if you don't want to use Poetry.

## How to run
The main command for running the code is:
```
poetry run python emperior_01/main.py -s <SYMBOL> -f <FROM_DATE> -t <TO_DATE>
```

A specific example to download TSLA from November 2018 to November 2019:
```
poetry run python emperior_01/main.py -s TSLA -f 2018-11-01 -t 2019-11-01
```

Setting `-o` will allow you to specify an output path for the file like this:
```
poetry run python emperior_01/main.py -s TSLA -f 2018-11-01 -t 2019-11-01 -o <PATH>
```

## Linting
```
poetry run black .; poetry run isort .
```

## TODO
- Tests