"""Docstring for the lat_stretch.py module

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

from math import pi
from typing import Any, Mapping, Optional

from peekingduck.pipeline.nodes.abstract_node import AbstractNode

from custom_nodes.dabble.utils import (
    Coord,
    ERROR_OUTPUT,
    KP_LEFT_ELBOW,
    KP_LEFT_SHOULDER,
    KP_LEFT_WRIST,
    KP_LEFT_HIP,
    KP_RIGHT_ELBOW,
    KP_RIGHT_SHOULDER,
    KP_RIGHT_WRIST,
    KP_RIGHT_HIP,
    angle_between_vectors_in_rad,
    obtain_keypoint
)


class Node(AbstractNode):

    _SETUP, _REST, _LEAN = range(3)

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
        self.curr_pos = {}
        self.max_angle = {}
        self.min_angle = {}
        self.reps = {}

    def is_leaning(
            self,
            id: Any,
            left_elbow: Optional[Coord],
            left_shoulder: Optional[Coord],
            left_wrist: Optional[Coord],
            left_hip: Optional[Coord],
            right_elbow: Optional[Coord],
            right_shoulder: Optional[Coord],
            right_wrist: Optional[Coord],
            right_hip: Optional[Coord]
    ) -> bool:

        # Check if keypoints are defined
        if left_shoulder is None or \
                left_hip is None or \
                right_shoulder is None or \
                right_hip is None:
            return False

        # Initialize coordinates
        left_shoulder_x, left_shoulder_y = left_shoulder
        right_shoulder_x, right_shoulder_y = right_shoulder
        left_hip_x, left_hip_y = left_hip
        right_hip_x, right_hip_y = right_hip

        # Calculate relevant vectors
        left_shoulder_hip_vec = (
            left_shoulder_x - left_hip_x,
            left_shoulder_y - left_hip_y
        )
        right_shoulder_hip_vec = (
            right_shoulder_x - right_hip_x,
            right_shoulder_y - right_hip_y
        )
        left_right_hip_vec = (
            right_hip_x - left_hip_x,
            right_hip_y - left_hip_y
        )
        right_left_hip_vec = (
            left_hip_x - right_hip_x,
            left_hip_y - right_hip_y
        )

        # Calculate the angle between left shoulder to left hip
        left_angle = angle_between_vectors_in_rad(
            *left_shoulder_hip_vec,
            *left_right_hip_vec
        )
        # Calculate the angle between right shoulder to right hip
        right_angle = angle_between_vectors_in_rad(
            *right_shoulder_hip_vec,
            *right_left_hip_vec
        )
        if left_angle == ERROR_OUTPUT or right_angle == ERROR_OUTPUT:
            # Needs debugging
            self.logger.warning(
                'Either one or both the calculated angles has returned an error.' +
                f'\nAngle calculated between left shoulder to left hip {left_shoulder_hip_vec} ' +
                f'and left hip to right hip {left_right_hip_vec} is {left_angle} radians.' +
                f'\nAngle calculated between right shoulder to right hip {right_shoulder_hip_vec} ' +
                f'and right hip to left hip {right_left_hip_vec} is {right_angle} radians.'
            )

        # Sanity check for posture
        # Check that the arms are raised, if defined
        if (left_elbow and left_elbow[1] > left_shoulder_y) or \
                (left_wrist and left_wrist[1] > left_shoulder_y) or \
                (right_elbow and right_elbow[1] > right_shoulder_y) or \
                (right_wrist and right_wrist[1] > right_shoulder_y):
            self.logger.info(
                'Either left or right arm is not in a valid position.' +
                f'\nleft_elbow: {left_elbow}, left_wrist: {left_wrist}, right_elbow: {right_elbow}, right_wrist: {right_wrist}'
            )
            return False

        # Check if either side has crossed the threshold for leaning
        sway_threshold = 25 * pi / 180  # 25 deg
        rest_threshold = 5 * pi / 180  # 5 deg
        if self.curr_pos[id] != self._SETUP:
            angle = max(abs(right_angle - pi / 2), abs(left_angle - pi / 2))
            self.max_angle[id] = max(self.max_angle[id], angle)
            self.min_angle[id] = min(self.min_angle[id], angle)
        angle_diff = abs(left_angle - right_angle)
        return angle_diff >= sway_threshold if self.curr_pos[id] == self._REST else angle_diff <= rest_threshold

    def run(
            self,
            inputs: Mapping[str, Any]
    ) -> Mapping[str, Mapping]:
        """Returns the dictionary of lat stretches for each given pose

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
            return {
                'max_angle': {},
                'min_angle': {},
                'reps': {}
            }
        for key in ('keypoints', 'obj_attrs'):
            if key not in inputs:
                # One or more metadata inputs are missing
                self.logger.warning(error_msg.format(f"'{key}'"))

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
                keypoint_list[KP_LEFT_ELBOW],
                keypoint_list[KP_LEFT_SHOULDER],
                keypoint_list[KP_LEFT_WRIST],
                keypoint_list[KP_LEFT_HIP],
                keypoint_list[KP_RIGHT_ELBOW],
                keypoint_list[KP_RIGHT_SHOULDER],
                keypoint_list[KP_RIGHT_WRIST],
                keypoint_list[KP_RIGHT_HIP]
            )

            # Update the relevant IDs
            if curr_id not in self.curr_pos:
                self.curr_pos[curr_id] = self._SETUP
                self.max_angle[curr_id] = 0
                self.min_angle[curr_id] = pi / 2
                self.reps[curr_id] = 0
            if self.curr_pos[curr_id] == self._REST and self.is_leaning(curr_id, *relevant_keypoints):
                self.curr_pos[curr_id] = self._LEAN
            elif self.curr_pos[curr_id] != self._REST and self.is_leaning(curr_id, *relevant_keypoints):
                self.reps[curr_id] += self.curr_pos[curr_id] == self._LEAN
                self.curr_pos[curr_id] = self._REST

        return {
            'max_angle': self.max_angle,
            'min_angle': self.min_angle,
            'reps': self.reps
        }


if __name__ == '__main__':
    pass