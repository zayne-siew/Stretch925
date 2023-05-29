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
        for key in ('bboxes', 'obj_attrs'):
            if key not in inputs:
                # One or more metadata inputs are missing
                self.logger.warning(error_msg.format(f"'{key}'"))

        # Get required inputs from pipeline
        img = inputs['img']
        img_height, img_width, *_ = img.shape
        all_ids = inputs.get('obj_attrs', {}).get('ids', [])
        bboxes = inputs.get('bboxes', [])
        max_angles = inputs.get('max_angle', {})
        min_angles = inputs.get('min_angle', {})
        reps = inputs.get('reps', {})

        # Handle the detection of each person
        scores = {}
        line_height = round(30 * _FONT_SCALE)  # height of each 'line' in pixels; 30 is arbitrary
        for curr_id, bbox in zip(all_ids, bboxes):

            # Obtain bounding box information
            x1, y1, x2, y2 = bbox
            x1, _ = obtain_keypoint(x1, y1, img_width, img_height)
            x2, y = obtain_keypoint(x2, y2, img_width, img_height)
            x = (x1 + x2) >> 1

            # Calculate the score
            max_angle = max_angles.get(curr_id, 0)
            min_angle = min_angles.get(curr_id, pi)
            score = max(min(max_angle - min_angle, pi), 0) / pi
            scores[curr_id] = round(score * reps.get(curr_id, 0) * 10)

            # Output the score
            message = '-' if max_angle < min_angle else f'{(score * 100):0.2f}%'
            display_text(img, x, y - 2 * line_height, f'Score: {message}',
                         (0, round(255 * score), round(255 * (1 - score))))
            display_text(img, x, y - line_height, f'Reps: {reps.get(curr_id, -1)}', (255, 255, 255))

        return {'scores': scores}


if __name__ == '__main__':
    pass