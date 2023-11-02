import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="file to be read")
parser.add_argument("result_file", help="file to save result")
parser.add_argument(
   "count_lines", type=int, default=10, nargs="?", help="Number of lines to be copied, default 10"
)
parser.add_argument(
   "--append", action="store_const", const="a", default="w", help="append result to `result_file`", dest="append"
)

args = parser.parse_args()

def copy_lines(input_file, result_file, count_lines, write_mode):
    try:
        with open(input_file, 'r') as in_file, open(result_file, write_mode) as out_file:
            for line in in_file.readlines()[:count_lines]:
                out_file.write(line)
    except FileNotFoundError:
        print('File could not be found.')

copy_lines(args.input_file, args.result_file, args.count_lines, args.append)