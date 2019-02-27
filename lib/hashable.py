#! usr/bin/env python3
"""
:
:  Container class for a PIL Image. Allows image data to be hashable.
:
:
"""
from PIL import Image
import uuid



class HashableImage:
    """
    :
    :  Hashable PIL Image container. Enables PIL image data to be used as dictionary keys.
    :
    :
    :  Attrs:
    :      Image image : Image object
    :      UUID  _hash : Uniquely hashable element
    :
    :
    """
    __slots__ = [
        "image",
        "_hash",
        ]

    def __init__(self, image: Image):
        self.image = image         # type: Image
        self._hash = uuid.uuid4()  # type: uuid.UUID

    @property
    def size(self) -> (int, int):
        """
        :
        :  Gets size (i.e. width and height) of the contained image object.
        :
        :
        """
        return self.image.size

    def __hash__(self):
        """
        :
        :  Returns hash(self).
        :
        :
        """
        return hash(self._hash)

    def convert(self, mode: str) -> Image:
        """
        :
        :  Implements Image.convert(). Note that this returns a PIL Image, not a HashableImage.
        :
        :
        """
        return self.image.convert(mode)

    def crop(self, rect: (int, int, int, int)):
        """
        :
        :  Implements Image.crop(). Note that this returns another HashableImage, not a PIL Image.
        :
        :
        """
        return HashableImage(self.image.crop(rect))

    def load(self):
        """
        :
        :  Returns pixel access data for the contained image object.
        :
        :
        """
        return self.image.load()

