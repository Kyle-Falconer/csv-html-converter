CSV to HTML CLI Utility
=======================

A simple CLI utility for converting CSV to an HTML table. CSV input can be provided as either a file argument or from the clipboard.

## Setup:

As an optional recommended step, first set up either a [virtual environment](https://docs.python.org/3/library/venv.html) or something like [Anaconda](https://www.anaconda.com/) to create a python sandbox (use only one of these methods, not both):

```
# with virtual environments in Python 3.7+
python3 -m venv csvenv
source csvenv/bin/activate
```

```
# with Anaconda:
conda create -n csvutil python=3.8
conda activate csvutil
```

Once a virtual environment is created, install the requirements:

```
# using Python 3.x
pip install -r requirements.txt
```

## Usage:

```
python csv-html.py --file=~/Downloads/test.csv

# or to use the contents of the clipboard:

python csv-html.py
```
