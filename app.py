from collections import defaultdict
import logging
import os

from flask import Flask, jsonify


# Define constants
app = Flask(__name__)
logger = logging.getLogger(__name__)
path = 'tmp.txt'


@app.route('/', methods=['POST'])
def get_scores():
    scores = defaultdict(int)

    # Read from temp file
    with open(path, 'r') as file:
        for line in file.readlines()[:-1]:
            curr_id, score = map(int, line.split(':'))
            scores[curr_id] = max(scores[curr_id], score)
    
    # Delete the temp file
    try:
        os.remove(path)
    except FileNotFoundError:
        logger.warning(f'Expected to delete file at filepath {path} but file was not found')
    
    # Post the final score, calculated as the total sum of all the scores
    # (assuming that only one user was in front of the camera)
    return jsonify(score=sum(scores.items()))


if __name__ == '__main__':
    app.run()