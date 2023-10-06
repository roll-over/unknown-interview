import json
from pathlib import Path
from typing import Dict


def get_json_data(file_name: str) -> Dict:
    """
    Read the content of the json file.

    Parameters: file_name: name of the json file with fixture.
    Returns: data from fixture.
    """
    file_path = Path(__file__).parent.parent.joinpath("fixtures").joinpath(file_name)

    with open("{path}.json".format(path=file_path), "r") as read_file:
        return json.load(read_file)
