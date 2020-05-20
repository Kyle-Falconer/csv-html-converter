import pandas as pd
import argparse
import xerox
import os
from pandas.errors import ParserError

parser = argparse.ArgumentParser(description='Convert Tab-delimited table to HTML table.')
parser.add_argument('--file',  type=str,
                    help='the path to the CSV file to convert')


TEMP_FILENAME=os.path.join(os.getcwd(), 'csv_clipboard_temp.csv')

def convertToHtml(filepath):
    try:
        df = pd.read_csv(filepath, sep="\t")
    except ParserError as pe:
        print(f"Invalid CSV format: {pe}")
        return
    print(df.to_html(na_rep='', float_format='{0:.2f}'.format).replace(r'<td>nan</td>', "<td></td>"))

def writeToTempFile(fileText):
    with open(TEMP_FILENAME, 'w') as f:
        print(fileText, file=f)

if __name__ == '__main__':
    args = parser.parse_args()
    filepath = args.file

    if filepath is None:
        writeToTempFile(xerox.paste())
        filepath=TEMP_FILENAME
    convertToHtml(TEMP_FILENAME)
    os.remove(TEMP_FILENAME)
