from functools import wraps

from _pytest.monkeypatch import MonkeyPatch


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
    @wraps(func)
    def function(*args, **kwargs):
        result = func(*args, **kwargs)
        e.__setattr__(func.__name__, result)
        return result

    return function


# def fresh_parse_data(func):
#     wraps(func)
#
#     def function(*args):
#         result = func(*args)
#         e.__setattr__(func.__name__, result)
#         return result
#
#     return function


def get_env_data(name):
    result = e.__getattribute__(name)
    return result


if __name__ == '__main__':
    setattr(Env, "case_data", {"a": {"b": 1}})
    # print(fresh_parse_data("a b"))
