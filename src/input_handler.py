import json


class InputHandler:
    def read_json(self, data):
        if isinstance(data, str):
            return json.loads(data)
        return data

    def read_file(self, filepath):
        with open(filepath, "r") as f:
            return json.load(f)
