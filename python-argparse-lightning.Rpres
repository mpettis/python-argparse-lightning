Python argparse
========================================================
author: Matt Pettis
date: 2015-10-08

matthew.pettis@gmail.com

https://github.com/mpettis

Painful Example
========================================================

<font size=6>

    $ ./unhelpful-script.py --maybe-this-switch-works
    Runtime error
    Stacktrace:
        Line 56: Your fibble is krazaweked.

</font>


Example help
========================================================

<font size=6>

    $ ./ex-argparse.py --help
    usage: ex-argparse.py [-h] [--optarg OPTARG] [-f] posarg
    
    Description of the overall program.
    
    positional arguments:
      posarg           A mandatory, positional argument
    
    optional arguments:
      -h, --help       show this help message and exit
      --optarg OPTARG  An optional argument
      -f, --flag       Just a flag

</font>


Example usages
========================================================

<font size=6>

    $ ./ex-argparse.py --optarg matt -f 5
    Namespace(flag=True, optarg='matt', posarg=5)
    
    $ ./ex-argparse.py --optarg matt 5
    Namespace(flag=False, optarg='matt', posarg=5)
    
    $ ./ex-argparse.py 5
    Namespace(flag=False, optarg=None, posarg=5)
    
    $ ./ex-argparse.py
    usage: ex-argparse.py [-h] [--optarg OPTARG] [-f] posarg
    ex-argparse.py: error: too few arguments 

</font>


What is argparse?
========================================================
incremental: true

- A module for easy parsing of command line switches.


Why use argparse?
========================================================
incremental: true

- You can use python scripts like other shell utilities.
- Switches are a well-known API.
- Help output format is of a well-known format.
- Allows you to make configurable tools.
- Those tools can interact with other tools.
- Is a way to make you think about simple API design.
- Similarly structured packages are used in other languages.


Example code
========================================================

<font size=6>

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
    
    print args

</font>


Questions?
========================================================

And thank you!

Matt Pettis

matthew.pettis@gmail.com

https://github.com/mpettis
