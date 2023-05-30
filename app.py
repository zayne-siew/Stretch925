"""Docstring for the app.py module

This module implements a Flask server to post score data to a localhost port.
It serves to interface between the Python and Next.js sections of the project.

Usage
-----
This file can be run on the terminal:

```
python app.py
```
"""

from collections import defaultdict
import logging
import os

from flask import Flask, jsonify


# Define constants
app = Flask(__name__)
logger = logging.getLogger(__name__)
PATH = 'tmp.txt'


@app.route('/', methods=['POST'])
def post_scores():
    """
    Posts the total sum of all scores recorded per each person ID to the localhost
    """

    scores = defaultdict(int)

    # Read from temp file
    with open(PATH, 'r', encoding='utf-8') as file:
        for line in file.readlines()[:-1]:
            curr_id, score = map(int, line.split(':'))
            scores[curr_id] = max(scores[curr_id], score)

    # Delete the temp file
    try:
        os.remove(PATH)
    except FileNotFoundError:
        logger.warning("Expected to delete file at filepath %s but file was not found", PATH)

    # Post the final score, calculated as the total sum of all the scores
    # (assuming that only one user was in front of the camera)
    return jsonify(score=sum(scores.items()))


if __name__ == '__main__':
    app.run()
