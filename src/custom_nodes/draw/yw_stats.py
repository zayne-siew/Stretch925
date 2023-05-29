"""Docstring for the yw_stats.py module

This module implements a custom draw Node class for handling the statistics of the Y-W stretch.

Usage
-----
This module should be part of a package that follows the file structure as specified by the
[PeekingDuck documentation](https://peekingduck.readthedocs.io/en/stable/tutorials/03_custom_nodes.html).

Navigate to the root directory of the package and run the following line on the terminal:

```
peekingduck run
```
"""

# pylint: disable=invalid-name, logging-format-interpolation

from math import pi
from typing import Any, Mapping, Optional

from peekingduck.pipeline.nodes.abstract_node import AbstractNode

from custom_nodes.draw.utils import _FONT_SCALE, display_text, obtain_keypoint


class Node(AbstractNode):

    def __init__(
            self,
            config: Optional[Mapping[str, Any]] = None,
            **kwargs
    ) -> None:
        """Initialises the custom Node class

        Parameters
        ----------
        config : dict, optional
            Node custom configuration

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments for instantiating the AbstractNode parent class
        """

        super().__init__(config, node_path=__name__, **kwargs)  # type: ignore

    def run(
            self,
            inputs: Mapping[str, Any]
    ) -> Mapping:

        # Initialise error message
        error_msg = 'The input dictionary does not contain the {} key.'

        # Check if required inputs are in pipeline
        if 'img' not in inputs:
            # There must be an image to display
            self.logger.error(error_msg.format("'img'"))
            return {}
        elif 'bboxes' not in inputs:
            # One or more metadata inputs are missing
            self.logger.warning(error_msg.format(f"'bboxes'"))

        # Get required inputs from pipeline
        img = inputs['img']
        img_height, img_width, *_ = img.shape
        bboxes = inputs.get('bboxes', [])
        max_angles = inputs.get('max_angle', {})
        min_angles = inputs.get('min_angle', {})
        reps = inputs.get('reps', {})

        # Handle the detection of each person
        line_height = round(30 * _FONT_SCALE)  # height of each 'line' in pixels; 30 is arbitrary
        for bbox, max_angle, min_angle, rep in zip(bboxes, max_angles, min_angles, reps):

            # Obtain bounding box information
            x1, y1, x2, y2 = bbox
            x, _ = obtain_keypoint(x1, y1, img_width, img_height)
            _, y = obtain_keypoint(x2, y2, img_width, img_height)

            # Calculate and output the score
            score = (max_angle - min_angle) / (90 * pi)
            display_text(img, x, y - 2 * line_height, f'Score: {(score * 100):0.2f}%',
                         (0, round(255 * score), round(255 * (1 - score))))
            display_text(img, x, y - line_height, f'Reps: {rep}', (255, 255, 255))

        return {}


if __name__ == '__main__':
    pass