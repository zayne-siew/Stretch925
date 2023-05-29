"""Docstring for the yw_stretch.py module

This module implements a custom dabble Node class for analysing a given pose.

Usage
-----
This module should be part of a package that follows the file structure as specified by the
[PeekingDuck documentation](https://peekingduck.readthedocs.io/en/stable/tutorials/03_custom_nodes.html).

Navigate to the root directory of the package and run the following line on the terminal:

```
peekingduck run
```
"""

# pylint: disable=logging-format-interpolation

from collections import defaultdict
from math import pi
from typing import Any, Mapping, Optional, Tuple

from peekingduck.pipeline.nodes.abstract_node import AbstractNode

from custom_nodes.dabble.utils import (
    Coord,
    ERROR_OUTPUT,
    KP_LEFT_ELBOW,
    KP_LEFT_SHOULDER,
    KP_LEFT_WRIST,
    KP_RIGHT_ELBOW,
    KP_RIGHT_SHOULDER,
    KP_RIGHT_WRIST,
    angle_between_vectors_in_rad,
    obtain_keypoint
)


class Node(AbstractNode):

    _SETUP, _W, _Y = range(3)

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

        # Implement trackers
        self.curr_pos = defaultdict(lambda: self._SETUP)
        self.max_angle = defaultdict(lambda: pi / 2)
        self.min_angle = defaultdict(lambda: pi)
        self.reps = defaultdict(int)

    def _helper(
            self,
            left_shoulder: Optional[Coord],
            left_elbow: Optional[Coord],
            left_wrist: Optional[Coord],
            right_shoulder: Optional[Coord],
            right_elbow: Optional[Coord],
            right_wrist: Optional[Coord]
    ) -> Tuple[float, float]:
        
        # Check if keypoints are defined
        if left_shoulder is None or \
                left_elbow is None or \
                left_wrist is None or \
                right_shoulder is None or \
                right_elbow is None or \
                right_wrist is None:
            return ERROR_OUTPUT, ERROR_OUTPUT

        # Obtain coordinates
        left_shoulder_x, left_shoulder_y = left_shoulder
        right_shoulder_x, right_shoulder_y = right_shoulder
        left_elbow_x, left_elbow_y = left_elbow
        right_elbow_x, right_elbow_y = right_elbow
        left_wrist_x, left_wrist_y = left_wrist
        right_wrist_x, right_wrist_y = right_wrist

        # Calculate relevant vectors
        left_shoulder_elbow_vec = (
            left_shoulder_x - left_elbow_x,
            left_shoulder_y - left_elbow_y
        )
        left_wrist_elbow_vec = (
            left_wrist_x - left_elbow_x,
            left_wrist_y - left_elbow_y
        )
        right_shoulder_elbow_vec = (
            right_shoulder_x - right_elbow_x,
            right_shoulder_y - right_elbow_y
        )
        right_wrist_elbow_vec = (
            right_wrist_x - right_elbow_x,
            right_wrist_y - right_elbow_y
        )

        # Calculate angle made between the left shoulder, left elbow, and left wrist
        left_angle = angle_between_vectors_in_rad(
            *left_shoulder_elbow_vec,
            *left_wrist_elbow_vec
        )
        # Calculate angle made between the right shoulder, right elbow, and right wrist
        right_angle = angle_between_vectors_in_rad(
            *right_shoulder_elbow_vec,
            *right_wrist_elbow_vec
        )
        if left_angle == ERROR_OUTPUT or right_angle == ERROR_OUTPUT:
            # Needs debugging
            self.logger.warning(
                'Either one or both the calculated angles has returned an error.' +
                f'\nAngle calculated between left shoulder to left elbow {left_shoulder_elbow_vec} ' +
                f'and left wrist to left elbow {left_wrist_elbow_vec} is {left_angle} radians.' +
                f'\nAngle calculated between right shoulder to right elbow {right_shoulder_elbow_vec} ' +
                f'and right wrist to right elbow {right_wrist_elbow_vec} is {right_angle} radians.'
            )

        return left_angle, right_angle

    def is_y_pose(
            self,
            id: Any,
            left_shoulder: Optional[Coord],
            left_elbow: Optional[Coord],
            left_wrist: Optional[Coord],
            right_shoulder: Optional[Coord],
            right_elbow: Optional[Coord],
            right_wrist: Optional[Coord]
    ) -> bool:

        # Sanity check for input
        left_angle, right_angle = self._helper(left_shoulder, left_elbow, left_wrist, right_shoulder, right_elbow, right_wrist)
        if left_angle == ERROR_OUTPUT or right_angle == ERROR_OUTPUT:
            return False
        
        # Obtain coordinates
        left_shoulder_x, left_shoulder_y = left_shoulder
        right_shoulder_x, right_shoulder_y = right_shoulder
        left_elbow_x, left_elbow_y = left_elbow
        right_elbow_x, right_elbow_y = right_elbow
        left_wrist_x, left_wrist_y = left_wrist
        right_wrist_x, right_wrist_y = right_wrist

        # Sanity check for posture
        left_valid = left_shoulder_x <= left_elbow_x <= left_wrist_x and left_wrist_y <= left_elbow_y <= left_shoulder_y
        right_valid = right_wrist_x <= right_elbow_x <= right_shoulder_x and right_wrist_y <= right_elbow_y <= right_shoulder_y
        if not (left_valid and right_valid):
            return False
        
        threshold = 150 * pi / 180  # 150 deg
        if self.curr_pos[id] != self._SETUP:
            ave_angle = (left_angle + right_angle) / 2
            self.max_angle[id] = max(self.max_angle[id], ave_angle)
            self.min_angle[id] = min(self.min_angle[id], ave_angle)
        return left_angle >= threshold and right_angle >= threshold

    def is_w_pose(
            self,
            id: Any,
            left_shoulder: Optional[Coord],
            left_elbow: Optional[Coord],
            left_wrist: Optional[Coord],
            right_shoulder: Optional[Coord],
            right_elbow: Optional[Coord],
            right_wrist: Optional[Coord]
    ) -> bool:

        # Check if keypoints are defined
        if left_shoulder is None or \
                left_elbow is None or \
                left_wrist is None or \
                right_shoulder is None or \
                right_elbow is None or \
                right_wrist is None:
            return False

        # Sanity check for input
        left_angle, right_angle = self._helper(left_shoulder, left_elbow, left_wrist, right_shoulder, right_elbow, right_wrist)
        if left_angle == ERROR_OUTPUT or right_angle == ERROR_OUTPUT:
            return False
        
        # Obtain coordinates
        left_shoulder_x, _ = left_shoulder
        right_shoulder_x, _ = right_shoulder
        left_elbow_x, left_elbow_y = left_elbow
        right_elbow_x, right_elbow_y = right_elbow
        left_wrist_x, left_wrist_y = left_wrist
        right_wrist_x, right_wrist_y = right_wrist

        # Sanity check for posture
        left_valid = left_shoulder_x <= left_elbow_x <= left_wrist_x and left_wrist_y <= left_elbow_y
        right_valid = right_wrist_x <= right_elbow_x <= right_shoulder_x and right_wrist_y <= right_elbow_y
        if not (left_valid and right_valid):
            return False

        threshold = 120 * pi / 180  # 120 deg
        if self.curr_pos[id] != self._SETUP:
            ave_angle = (left_angle + right_angle) / 2
            self.max_angle[id] = max(self.max_angle[id], ave_angle)
            self.min_angle[id] = min(self.min_angle[id], ave_angle)
        return left_angle <= threshold and right_angle <= threshold

    def run(
            self,
            inputs: Mapping[str, Any]
    ) -> Mapping[str, Mapping[int, int]]:
        """Returns the dictionary of folded arms for each given pose

        Parameters
        ----------
        inputs : dict
            Dictionary with the following keys:

            - 'img' - given image to be displayed
            - 'keypoints' - keypoints from PoseNet model
            - 'obj_attrs' - to obtain tracking IDs from PoseNet model

        Returns
        -------
        dict
            Dictionary with the following keys:

            - 'max_angle' - maximum obtained angle from current run
            - 'min_angle' - minimum obtained angle from current run
            - 'reps' - number of repetitions of current run
        """

        # Initialise error message
        error_msg = 'The input dictionary does not contain the {} key.'

        # Check if required inputs are in pipeline
        if 'img' not in inputs:
            # There must be an image to display
            self.logger.error(error_msg.format("'img'"))
            return {'arms_folded': {}}  # type: ignore
        elif 'keypoints' not in inputs:
            self.logger.warning(error_msg.format("'keypoints'"))

        # Get required inputs from pipeline
        height, width, *_ = inputs['img'].shape
        all_ids = inputs.get('obj_attrs', {}).get('ids', [])
        all_keypoints = inputs.get('keypoints', [])

        # Handle the detection of each person
        for curr_id, keypoints in zip(all_ids, all_keypoints):

            # Store and display PoseNet keypoints
            keypoint_list = [
                obtain_keypoint(
                    *keypoint.tolist(),
                    img_width=width,
                    img_height=height
                ) \
                for keypoint in keypoints
            ]
            relevant_keypoints = (
                keypoint_list[KP_LEFT_SHOULDER],
                keypoint_list[KP_LEFT_ELBOW],
                keypoint_list[KP_LEFT_WRIST],
                keypoint_list[KP_RIGHT_SHOULDER],
                keypoint_list[KP_RIGHT_ELBOW],
                keypoint_list[KP_RIGHT_WRIST]
            )

            # Update the relevant IDs
            if self.curr_pos[curr_id] == self._W and self.is_y_pose(curr_id, *relevant_keypoints):
                self.curr_pos[curr_id] = self._Y
            elif self.curr_pos[curr_id] != self._W and self.is_w_pose(curr_id, *relevant_keypoints):
                self.reps[curr_id] += self.curr_pos[curr_id] == self._Y
                self.curr_pos[curr_id] = self._W

        return {
            'max_angle': self.max_angle,
            'min_angle': self.min_angle,
            'pos': self.curr_pos,
            'reps': self.reps
        }


if __name__ == '__main__':
    pass