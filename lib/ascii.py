#! usr/bin/env python3
"""
:
:  Font-based utility functions.
:
:
"""
import freetype




def fn_LoadFont(s_Filename: str, i_Size: int) -> freetype.Face:
    """
    :
    :  Loads a truetype/freetype font from file and sets its size.
    :
    :
    :  Args:
    :      str s_Filename : Filename (expected TTF font) to load
    :
    :  Returns:
    :      Freetype Face object
    :
    :
    """
    o_FreetypeFace = freetype.Face(s_Filename)  # type: freetype.Face
    fn_SetCharSize(o_FreetypeFace, i_Size)
    return o_FreetypeFace



def fn_SetCharSize(o_FreetypeFace: freetype.Face, i_Size: int) -> None:
    """
    :
    :  Sets character size for the given font face. (In-place).
    :
    :
    :  Args:
    :      freetype.Face o_FreetypeFace : Font face used to determine / set character size
    :      int           i_Size         : Target size of font face
    :
    :  Returns:
    :      None
    :
    :
    """
    o_FreetypeFace.set_char_size(i_Size)



def fn_SortGlyphs(o_FreetypeFace: freetype.Face, s_Chars: str, b_Invert: bool = False) -> list:
    """
    :
    :  Sorts glyphs based on pixel density.
    :
    :
    :  Args:
    :      freetype.Face o_FreetypeFace : Font face used to calculate pixel densities
    :      str           s_Chars        : Character set over which pixel densities will be taken
    :      bool          b_Invert       : Whether to invert pixel density mapping order (default False)
    :
    :  Returns
    :
    :
    """
    l_Output = []

    # Profile pixel density over character set
    # ...
    for c in s_Chars:
        o_FreetypeFace.load_char(c)
        b_Buffer = o_FreetypeFace.glyph.bitmap.buffer
        l_Output.append((sum(b_Buffer), c))

    # Sort output list by pixel density
    # ...
    l_Output = [y[1] for y in sorted(l_Output, key=lambda x: x[0])]

    # Optionally invert order
    # ...
    if b_Invert:
        l_Output = l_Output[::-1]

    # Return it
    # ...
    return l_Output

