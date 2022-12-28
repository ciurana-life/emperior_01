import argparse
import os

import yfinance as yf
from helpers import cprint, validate_date_format
from time_series.fb_prophet import main as prophet

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--symbol", type=str)
    parser.add_argument("-f", "--from_date", type=str)
    parser.add_argument("-t", "--to_date", type=str)
    parser.add_argument("-o", "--output", type=str, default=".")
    parser.add_argument("-tf", "--time_frame", type=bool)
    args = parser.parse_args()

    # [1] Check all the args passed are correctly formated.
    args_has_err = False

    if not args.symbol:
        cprint("symbol is required", "R")
        args_has_err = True

    if not args.from_date:
        cprint("from_date is required", "R")
        args_has_err = True

    if not validate_date_format(args.from_date):
        cprint("from_date has an invalid format, please use YYYY-MM-DD", "R")
        args_has_err = True

    if not args.to_date:
        cprint("to_date is require", "R")
        args_has_err = True

    if not validate_date_format(args.to_date):
        cprint("to_date has an invalid format, please use YYYY-MM-DD", "R")
        args_has_err = True

    if args_has_err:
        return False

    # [2] Define a file name given the args and check if the file exists or not.
    output_file_name = f"{args.symbol}_{args.from_date}_{args.to_date}.csv"
    output_file_path = os.path.join(args.output, output_file_name)
    if os.path.exists(output_file_path):
        cprint(f"a file at {output_file_path} already exists", "R")
        return False

    # [3] Download and write to file.
    data = yf.download(args.symbol, args.from_date, args.to_date)
    with open(output_file_path, "w") as output_file:
        output_file.write(data.to_csv())

    cprint(f"Data was saved at {output_file_path} :)", "G")

    # [4] Save prediction images if we need to.
    if args.time_frame:
        prophet(output_file_path)
        cprint(f"Images where generated", "G")

    return True


if __name__ == "__main__":
    cprint("Running...", "G")
    main()
