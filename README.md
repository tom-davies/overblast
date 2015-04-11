# OverBLAST

A tool (written in Python) to find an an ancestral version of a gene product, then search for that product's presence in mammals.
This is intended to find an analogue of the product that has a similar sequence but a different function within the same original species.

## Prerequisites ##
In order to use OverBLAST, the following prerequesites are required. UNIX/OSX users can use the easy_install tool included with python, and Windows users can obtain installers from the links included.

- [Biopython](http://biopython.org)
        sudo easy_install -f http://biopython.org/DIST/ biopython
- [PrettyTable](https://code.google.com/p/prettytable/)
        sudo easy_install prettytable

## Using the Tool ##
The tool can be started from the command line by simply using

    python ./overblast.py
