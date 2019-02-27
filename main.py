#! usr/bin/env python3
import sys, argparse
from asciier import *



DESCRIPTION = "Description"
HELP_HELP   = "Example: Help argument"
HELP_INPUT  = "Example"
HELP_IMAGE  = "Example"
HELP_WIDTH  = "Ex"
HELP_HEIGHT = "Ex"
HELP_SIZE   = "Size"
HELP_REVERSE = "EX"
HELP_CHARS   = "Ch"



class CommandLine:
    def __init__(self):
        o_Parser = argparse.ArgumentParser(description=DESCRIPTION)

        o_Parser.add_argument("-H", "--Help",    help=HELP_HELP,    required=False, default='',)
        o_Parser.add_argument("-f", "--font",    help=HELP_INPUT,   required=True,  default='',)
        o_Parser.add_argument("-i", "--image",   help=HELP_IMAGE,   required=True,  default='',)
        o_Parser.add_argument("-w", "--width",   help=HELP_WIDTH,   required=False, default=ITER_WIDTH,)
        o_Parser.add_argument("-x", "--height",  help=HELP_HEIGHT,  required=False, default=ITER_HEIGHT,)
        o_Parser.add_argument("-s", "--size",    help=HELP_SIZE,    required=False, default=FONT_SIZE,)
        o_Parser.add_argument("-r", "--reverse", help=HELP_REVERSE, required=False, default=False,)
        o_Parser.add_argument("-c", "--chars",   help=HELP_CHARS,   required=False, default=CHARACTERS,)

        ns_Arguments    = o_Parser.parse_args()  # type: argparse.Namespace
        s_FontFilename  = ns_Arguments.font      # type: str
        s_ImageFilename = ns_Arguments.image     # type: str
        s_IterWidth     = ns_Arguments.width     # type: str
        s_IterHeight    = ns_Arguments.height    # type: str
        s_Size          = ns_Arguments.size      # type: str
        s_Reverse       = ns_Arguments.reverse   # type: str
        s_Chars         = ns_Arguments.chars     # type: str
        i_IterWidth     = int(s_IterWidth)       # type: int
        i_IterHeight    = int(s_IterHeight)      # type: int
        i_Size          = int(s_Size)            # type: int
        b_Reverse       = False                  # type: bool

        try:
            i_Reverse = int(s_Reverse)
            b_Reverse = bool(i_Reverse)
        except ValueError:
            s_Reverse = s_Reverse.lower()
            if 'f' in s_Reverse:
                b_Reverse = False
            elif 't' in s_Reverse:
                b_Reverse = True

        fn_ProcessImage(
            s_FontFilename,
            s_ImageFilename,
            s_Chars,
            b_Reverse,
            i_Size,
            i_IterWidth,
            i_IterHeight
            )




def main():
    l_Args = sys.argv
    s_FontFilename = l_Args[1]
    s_ImageFilename = l_Args[2]
    fn_ProcessImage(s_FontFilename, s_ImageFilename)






if __name__ == "__main__":
    args = CommandLine()
