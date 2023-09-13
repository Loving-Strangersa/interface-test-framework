from _pytest.monkeypatch import MonkeyPatch

from KeywordDriven.api import Data


class Env(object):
    pass


e = Env()


def clear_env():
    values = dict(e.__dict__.items())
    for key, value in values.items():
        if key.startswith("step_"):
            delattr(e, key)


monkeypatch = MonkeyPatch()


def fresh_parse_data(func):
    def function(*args):
        result = func(*args)
        params = []
        for index in range(len(args)):
            if isinstance(args[index], dict):
                for key, value in args[index].items():
                    if key[0] == "!":
                        pass
                        # {key[1:]:}

        e.__setattr__(func.__name__, result)
        return result

    return function


if __name__ == '__main__':
    setattr(Data, "case_data", {"a": {"b": 1}})
    # print(fresh_parse_data("a b"))
