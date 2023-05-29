from typing import Any, Mapping, Optional

from peekingduck.pipeline.nodes.abstract_node import AbstractNode


class Node(AbstractNode):

    def __init__(
            self,
            config: Optional[Mapping[str, Any]] = None,
            **kwargs
    ) -> None:

        super().__init__(config, node_path=__name__, **kwargs)  # type: ignore

    def run(
            self,
            inputs: Mapping[str, Any]
    ) -> Mapping:
        
        # Obtain the scores of each person detected
        scores = inputs.get('scores', {})

        # Store the scores in a temporary file
        with open('../tmp.txt', 'a+') as file:
            for curr_id, score in scores.items():
                file.write(f'{curr_id}:{score}\n')
        
        return {}


if __name__ == '__main__':
    pass