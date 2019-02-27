#! usr/bin/env python3
"""
:
:  Image processing utility functions.
:
:
"""
from PIL import Image, ImageStat, PyAccess
from .hashable import HashableImage



def fn_LoadImage(s_Filename: str) -> HashableImage:
    """
    :
    :  Opens an image at the given filename, applies a corrective transformation, then stores it in a HashableImage.
    :
    :
    :  Args:
    :      str s_Filename : Filename for the image
    :
    :  Returns:
    :      HashableImage object (wraps PIL Image, which is normally unhashable).
    :
    :
    """
    # Open image at filename
    # ...
    o_Image1 = Image.open(s_Filename)

    # Flip horizontally and rotate 90 degrees clockwise (correction)
    # ...
    i_W, i_H = o_Image1.size
    o_Image2 = Image.new("RGBA", (i_H, i_W))
    o_Image1 = o_Image1.transpose(Image.FLIP_LEFT_RIGHT)
    o_Image1 = o_Image1.rotate(90, expand=True)
    o_Image2.paste(o_Image1, (0,0))

    # Wrap in HashableImage
    # ...
    return HashableImage(o_Image2)



def fn_GetBrightness(o_Image: Image) -> float:
    """
    :
    :  Gets RMS pixel brightness of a PIL image object.
    :
    :
    :  Args:
    :      Image o_Image : Image to get brightness
    :
    :  Returns:
    :      Root mean squared pixel brightness
    :
    :
    """
    o_Image = o_Image.convert('L')
    return int(round(ImageStat.Stat(o_Image).rms[0]))



def fn_GetSubsurface(o_Image: Image, i_X: int, i_Y: int, i_W: int, i_H: int) -> Image:
    """
    :
    :  Returns subregion on an image.
    :
    :
    :  Args:
    :      Image o_Image :
    :      int   i_X     :
    :      int   i_Y     :
    :      int   i_W     :
    :      int   i_H     :
    :
    :  Returns:
    :      Subsurface on the image
    :
    :
    """
    return o_Image.crop((i_X, i_Y, i_X + i_W, i_Y + i_H))



def fn_GetPixelData(o_Image: Image) -> PyAccess:
    """
    :
    :  Returns pixel access object for the given Image.
    :
    :
    :  Args:
    :      o_Image Image : PIL image object
    :
    :  Returns:
    :      PyAccess pixel access object
    :
    :
    """
    return o_Image.load()



def fn_Iterate2D(o_Image: Image, i_W: int, i_H: int) -> dict:
    """
    :
    :  Iterates over an image in "blocks" of size (i_W, i_H). Returns subsurfaces of each block as mapped to
    :  "coordinates" (relative / unit-based X-Y positions).
    :
    :
    :  Args:
    :      Image o_Image : PIL image object
    :      int   i_W     : Pixel width of subregion chunks
    :      int   i_H     : Pixel height of subregion chucks
    :
    :  Returns:
    :      Dictionary mapping block coordinates to subregions on the original image.
    :
    :
    """
    i_FullW, i_FullH = o_Image.size  # type: (int, int)
    i_NumX           = 0             # type: int
    i_NumY           = 0             # type: int
    d_Output         = {}            # type: dict

    for i_X in range(0, i_FullW, i_W):
        for i_Y in range(0, i_FullH, i_H):
            d_Output[i_NumX, i_NumY] = fn_GetSubsurface(o_Image, i_X, i_Y, i_W, i_H)
            i_NumY += 1
        i_NumX += 1

    return d_Output



def fn_MapLuminosity2D(d_Images: dict) -> dict:
    """
    :
    :  Calculates and maps luminosity across a 2D array of images.
    :
    :
    :  Args:
    :      dict d_Images : Mapping from 2-tuple coordinates to PIL Images
    :
    :  Returns:
    :      Dictionary mapping 2-tuple coordinates to image luminosities
    :
    :
    """
    d_Output = {}

    for i2_Coord, o_Image in d_Images.items():
        d_Output[i2_Coord] = fn_GetBrightness(o_Image)

    return d_Output
