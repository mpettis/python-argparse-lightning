#!/usr/bin/env python

    #### See: https://docs.python.org/2/howto/argparse.html
import argparse
from pprint import pprint

    ### Create an argument parser
parser = argparse.ArgumentParser(description="Description of the overall program.")

    ### Set up arguments to be taken
parser.add_argument("posarg", type=int,
        help="A mandatory, positional argument")
parser.add_argument("--optarg",
        help="An optional argument")
parser.add_argument("-f", "--flag", action="store_true",
        help="Just a flag")

    ### Parse the arguments
args = parser.parse_args()


    ### Pring out the arguments
pprint(args)

