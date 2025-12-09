import sys
from reformatter_core import reformat_excel
from gui.main import run_gui

if __name__ == "__main__":
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    formatted = reformat_excel(input_file, output_file)
    run_gui(formatted)
