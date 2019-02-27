#! usr/bin/env python3
import argparse
from src import *



DESCRIPTION  = "Customizable ASCII art generator. Requires PIL and FreeType."
HELP_FONT    = "set input font file (.ttf)"
HELP_IMAGE   = "set input image file"
HELP_WIDTH   = "set pixel width for subregions"
HELP_HEIGHT  = "set pixel height for subregions"
HELP_SIZE    = "set font size"
HELP_REVERSE = "invert luminosity mapping"
HELP_CHARS   = "set character set"
HELP_OUTPUT  = "set output file (.txt)"



class CommandLine:
    def __init__(self):
        o_Parser = argparse.ArgumentParser(description=DESCRIPTION)

        o_Parser.add_argument("-f", dest="Font filename",     help=HELP_FONT,    required=True,  default='', )
        o_Parser.add_argument("-i", dest="Image filename",    help=HELP_IMAGE,   required=True,  default='',)
        o_Parser.add_argument("-x", dest="Subregion width",   help=HELP_WIDTH,   required=False, default=ITER_WIDTH,)
        o_Parser.add_argument("-y", dest="Subregion height",  help=HELP_HEIGHT,  required=False, default=ITER_HEIGHT,)
        o_Parser.add_argument("-s", dest="Font size",         help=HELP_SIZE,    required=False, default=FONT_SIZE,)
        o_Parser.add_argument("-c", dest="Character set",     help=HELP_CHARS,   required=False, default=CHARACTERS,)
        o_Parser.add_argument("-o", dest="Output file",       help=HELP_OUTPUT,  required=False, default='',)
        o_Parser.add_argument("-r", dest="Invert luminosity", help=HELP_REVERSE, required=False, default=False,)

        ns_Arguments    = o_Parser.parse_args()  # type: argparse.Namespace
        s_FontFilename  = ns_Arguments.font      # type: str
        s_ImageFilename = ns_Arguments.image     # type: str
        s_IterWidth     = ns_Arguments.width     # type: str
        s_IterHeight    = ns_Arguments.height    # type: str
        s_Size          = ns_Arguments.size      # type: str
        s_Reverse       = ns_Arguments.reverse   # type: str
        s_Output        = ns_Arguments.output    # type: str
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
            s_Output,
            s_Chars,
            b_Reverse,
            i_Size,
            i_IterWidth,
            i_IterHeight
            )



if __name__ == "__main__":
    args = CommandLine()
