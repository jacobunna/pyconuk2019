# -------------------------------------
# Example 1: Prefer Built-In Exceptions
# -------------------------------------


class UserNotFound(Exception):
    pass


def get_user_bad(user_id):
    all_users = get_all_users()
    if user_id not in all_users:
        raise UserNotFound(user_id)
    return all_users[user]


def get_user_good(user_id):
    all_users = get_all_users()
    if user_id not in all_users:
        raise ValueError(user_id)
    return all_users[user_id]


# ----------------------------------
# Example 2: Do you need that class?
# ----------------------------------

from collections import namedtuple


class TimeDuration:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_seconds(self):
        return (self.end_time - self.start_time).total_seconds()


TimeDuration = namedtuple("TimeDuration", ["start_time", "end_time"])


def get_seconds(duration):
    return (duration.end_time - duration.start_time).total_seconds()
