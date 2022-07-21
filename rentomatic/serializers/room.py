import json
import dataclasses


class RoomJsonEncoder(json.JSONEncoder):
    def default(self, o):
        # provide a custom encoder subclass to serialize dataclasses
        # see https://docs.python.org/3/library/json.html#json.JSONEncoder.default  # noqa
        try:
            new_dict = {}
            if dataclasses.is_dataclass(o):
                new_dict = dataclasses.asdict(o)

                # UUID code is not directly JSON serialisable
                new_dict['code'] = str(o.code)
            return new_dict
        except TypeError:
            pass
