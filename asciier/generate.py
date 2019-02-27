#! usr/bin/env python3
"""
:
:  Utility for generating ASCII art given an input image.
:
:
"""
from asciier.ascii      import *
from asciier.luminosity import *



UPPER       = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER       = "abcdefghijklmnopqrstuvwxyz"
DIGIT       = "0123456789"
SYMBOL      = "~!@#$%^&*()_+`-=[]{}|\\:;\"'<>?,./"
#CHARACTERS  = UPPER + LOWER + DIGIT + SYMBOL
CHARACTERS  = SYMBOL
ITER_WIDTH  = 4
ITER_HEIGHT = 2
FONT_SIZE   = 99
INVERT      = True



def fn_GetNumValues(d_Dict: dict) -> int:
    """
    :
    :  Gets the total number of unique values from the given mapping.
    :
    :
    :  Args:
    :      dict d_Luminosity :
    :
    :  Returns:
    :      Number of unique values
    :
    :
    """
    return len(list(set(d_Dict.values())))



def fn_MapRange(l_List: iter, i_Range: int) -> dict:
    """
    :
    :  Evenly assigns a numerical value within a given range to each element of a list.
    :
    :
    :  Args:
    :      iter l_List  : List of items that will be mapped as values in the output dictionary
    :      int  i_Range : Maximum value for the range of numbers that will be mapped as keys in the output
    :
    :  Returns:
    :      Dictionary containing the above mapping
    :
    :
    """
    # Set up local containers
    # ...
    i_LenList = len(l_List)          # type: int
    i_M       = 0                    # type: int
    f_Step    = i_LenList / i_Range  # type: float
    f_N       = 0                    # type: float
    d_Output  = {}                   # type: dict

    # Step through list and populate output dictionary evenly
    # ...
    while f_N < i_LenList:
        try:
            i_Index = int(round(f_N))
            o_Item = l_List[i_Index]
            d_Output[i_M] = o_Item
            f_N += f_Step
            i_M += 1
        except IndexError:
            break

    return d_Output



def fn_CrossChain(d_Dict1: dict, d_Dict2: dict, b_Default: bool = False) -> dict:
    """
    :
    :  Maps keys in the first dictionary to values in the second dictionary. (In other words, the first dictionary's
    :  keys will be mapped to the second dictionary's values, for each value in the first that's a key in the second).
    :
    :  In case of hash misses in the second dictionary, supplying a "default" value may be enabled. If enabled, the
    :  default value will be taken as the "last" element of the second dictionary (that is, as though its entries
    :  were sorted in order of its keys).
    :
    :
    :  Args:
    :      dict d_Dict1   : Dictionary whose keys are to become keys in the output dictionary
    :      dict d_Dict2   : Dictionary whose values are to become values in the output dictionary
    :      bool b_Default : Whether to use a fallback value in place of "missing" values (default False)
    :
    :  Returns:
    :      Dictionary containing keys from the first dictionary mapped to values from the second dictionary
    :
    :
    """
    d_Output = {}

    # Supply default value if needed
    # ...
    if b_Default:
        v_Default = fn_SortByKey(d_Dict2)[-1]
    else:
        v_Default = None

    # Remap keys(1) to values(2)
    # ...
    for k1, v1 in d_Dict1.items():
        if v1 in d_Dict2:
            d_Output[k1] = d_Dict2[v1]
        elif b_Default:
            d_Output[k1] = v_Default

    return d_Output



def fn_ParallelChain(d_Dict1: dict, d_Dict2: dict, b_Default: bool = False) -> dict:
    """
    :
    :  Maps values in the first dictionary to values in the second dictionary. (In other words, the first dictionary's
    :  values will be mapped to the second dictionary's values, for each key in the first that's also a key in the
    :  second).
    :
    :  In case of hash misses in the second dictionary, supplying a "default" value may be enabled. If enabled, the
    :  default value will be taken as the "last" element of the second dictionary (that is, as though its entries were
    :  sorted in order of its keys).
    :
    :
    :  Args:
    :      dict d_Dict1   : Dictionary whose values are to become keys in the output dictionary
    :      dict d_Dict2   : Dictionary whose values are to become values in the output dictionary
    :      bool b_Default : Whether to use a fallback value in place of "missing" values (default False)
    :
    :  Returns:
    :      Dictionary containing values from the first dictionary mapped to values from the second dictionary
    :
    :
    """
    d_Output = {}

    # Supply default value if needed
    # ...
    if b_Default:
        v_Default = fn_SortByKey(d_Dict2)[-1]
    else:
        v_Default = None

    # Remap values(1) to values(2)
    # ...
    for k1, v1 in d_Dict1.items():
        if k1 in d_Dict2:
            d_Output[v1] = d_Dict2[k1]
        elif b_Default:
            d_Output[v1] = v_Default

    return d_Output



def fn_SortByKey(d_Dict: dict) -> list:
    """
    :
    :  Returns a list of values in a dictionary in order of their keys.
    :
    :
    :  Args:
    :      dict d_Dict : An unsigned integer!
    :
    :  Returns:
    :      List of values sorted by key
    :
    :
    """
    return [y[1] for y in sorted([(k, v) for k, v in d_Dict.items()], key=lambda x: x[0])]



def fn_GenerateAscii(d_CoordToChar: dict) -> str:
    """
    :
    :  Generates an ASCII image string given characters mapped to (relative) rendering coordinates.
    :
    :
    :  Args:
    :      dict d_CoordToChar : Mapping from 2-tuple coordinates to string characters
    :
    :  Returns:
    :      ASCII image (or any other encoding really), separated by newlines
    :
    :
    """
    d_Ascii  = {}  # type: dict
    s_Output = ''  # type: str

    # Map images to x-y coordinates, splitting x- and y- into their own sub-dictionaries
    # ...
    for i2_Coord, s_Char in d_CoordToChar.items():
        i_X, i_Y = i2_Coord

        if i_X not in d_Ascii:
            d_Ascii[i_X] = {}

        if i_Y not in d_Ascii[i_X]:
            d_Ascii[i_X][i_Y] = s_Char

    # Sort the entries for each "row" of ASCII characters in the dictionary, then join them and concatenate the
    # resulting string
    # ...
    for i_X, d_X in d_Ascii.items():
        s_Output += ''.join(fn_SortByKey(d_X))
        s_Output += '\n'

    return s_Output



def fn_ProcessImage(
        s_FontFilename:  str,
        s_ImageFilename: str,
        s_CharacterSet:  str  = CHARACTERS,
        b_Invert:        bool = INVERT,
        i_Size:          int  = FONT_SIZE,
        i_IterWidth:     int  = ITER_WIDTH,
        i_IterHeight:    int  = ITER_HEIGHT,
        ):
    """
    :
    :  Loads an image and converts it to ASCII art, then prints it out.
    :
    :
    """
    # Load font and sort glyphs in order of luminosity
    # ...
    o_FreetypeFace = fn_LoadFont(s_FontFilename, i_Size)                      # type: freetype.Face
    s_Characters   = fn_SortGlyphs(o_FreetypeFace, s_CharacterSet, b_Invert)  # type: str

    # Load image and profile it for luminosity
    # ...
    o_Image         = fn_LoadImage(s_ImageFilename)                     # type: Image
    d_CoordToImage  = fn_Iterate2D(o_Image, i_IterWidth, i_IterHeight)  # type: dict
    d_CoordToLum    = fn_MapLuminosity2D(d_CoordToImage)                # type: dict
    i_NumLuminosity = fn_GetNumValues(d_CoordToLum)                     # type: int
    l_Luminosity    = list(set(d_CoordToLum.values()))                  # type: list

    # Relay a series of associative mappings, ending with characters mapped under relative coordinates
    # ...
    d_CharRange   = fn_MapRange(s_Characters, i_NumLuminosity)      # type: dict
    d_LumRange    = fn_MapRange(l_Luminosity, i_NumLuminosity)      # type: dict
    d_LumToChar   = fn_ParallelChain(d_LumRange, d_CharRange)       # type: dict
    d_ImageToLum  = fn_ParallelChain(d_CoordToImage, d_CoordToLum)  # type: dict
    d_ImageToChar = fn_CrossChain(d_ImageToLum, d_LumToChar, True)  # type: dict
    d_CoordToChar = fn_CrossChain(d_CoordToImage, d_ImageToChar)    # type: dict

    # Generate ASCII image using coordinates -> characters
    # ...
    s_Out = fn_GenerateAscii(d_CoordToChar)
    print(s_Out)





if __name__ == "__main__":
    fn_ProcessImage("../res/arial.ttf", "../res/nagatoro.png")
