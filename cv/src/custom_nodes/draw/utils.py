"""Docstring for the draw/utils.py script

This script contains constants and other miscellaneous functions
for the rest of the scripts in the draw module to use.

Usage
-----
This script is not meant to be used independently.
"""

# pylint: disable=invalid-name, logging-format-interpolation

from typing import Tuple

import cv2


"""Type-hinting alias for coordinates"""  # pylint: disable=pointless-string-statement
Coord = Tuple[int, int]


"""Define font properties for display purposes"""  # pylint: disable=pointless-string-statement

"""Defines the font family for display purposes"""  # pylint: disable=pointless-string-statement
_FONT_FACE = cv2.FONT_HERSHEY_SIMPLEX  # pylint: disable=no-member

"""Defines the font scale for display purposes"""  # pylint: disable=pointless-string-statement
_FONT_SCALE = 1

"""Defines the font thickness for display purposes"""  # pylint: disable=pointless-string-statement
_FONT_THICKNESS = 2


def display_text(
        img,
        abs_x: int,
        abs_y: int,
        text: str,
        font_colour: Tuple[int, int, int],
        *,
        font_face: int = _FONT_FACE,
        font_scale: float = _FONT_SCALE,
        font_thickness: int = _FONT_THICKNESS
) -> None:
    """Displays text at a specified coordinate on top of the displayed image

    Parameters
    ----------
    img
        The image to display
    abs_x : int
        Absolute x-coordinate to display the text at
    abs_y : int
        Absolute y-coordinate to display the text at
    text : str
        Text to display
    font_colour : tuple of ints
        Colour of the text to display, specified in BGR format

    Other Parameters
    ----------------
    font_face : int, default=`_FONT_FACE`
        Font type of the text to display.

        Limited to a subset of Hershey Fonts as
        [supported by OpenCV](https://stackoverflow.com/questions/371910008/load-truetype-font-to-opencv).
    font_scale : float
        Relative size of the text to display
    font_thickness : int
        Relative thickness of the text to display
    """

    cv2.putText(  # pylint: disable=no-member
        img=img,
        text=text,
        org=(abs_x, abs_y),
        fontFace=font_face,
        fontScale=font_scale,
        color=font_colour,
        thickness=font_thickness
    )


def obtain_keypoint(
        rel_x: float,
        rel_y: float,
        img_width: int,
        img_height: int
) -> Coord:
    """Obtains the coordinates of a detected PoseNet keypoint on a given image

    Parameters
    ----------
    rel_x : float
        Relative horizontal position of the coordinate; \\( 0 \\le x_{rel} \\le 1 \\)
    rel_y : float
        Relative vertical position of the coordinate; \\( 0 \\le y_{rel} \\le 1 \\)
    img_width : int
        Width of the image in pixels
    img_height : int
        Height of the image in pixels

    Returns
    -------
    `Coord`
        Absolute coordinate \\( (x_{abs}, y_{abs}) \\) on the image;
        \\( 0 \\le x_{abs} \\le width \\) and \\( 0 \\le y_{abs} \\le height \\).
    """

    return round(rel_x * img_width), round(rel_y * img_height)


if __name__ == '__main__':
    pass