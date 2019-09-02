# -----------------------
# Example 1: Enumerations
# -----------------------

from enum import Enum

customer_1 = {"first_name": "John", "last_name": "Smith"}


def swap_names_bad(customer):
    if "first_name" not in customer or "last_name" not in customer:
        return False
    customer["first_name"], customer["last_name"] = (
        customer["last_name"],
        customer["first_name"],
    )
    return True


class Status(Enum):
    SUCCESS = 1
    FAILURE = 2


def swap_names_good(customer):
    if "first_name" not in customer or "last_name" not in customer:
        return Status.FAILURE
    customer["first_name"], customer["last_name"] = (
        customer["last_name"],
        customer["first_name"],
    )
    return Status.SUCCESS


# --------------
# Example 2: SQL
# --------------

# To find out more, visit https://www.sqlalchemy.org/.
import sqlalchemy


def get_nickname_bad(user_id):
    sql = f"SELECT `nickname` FROM `users` " f"WHERE `user_id` = {user_id}"
    # Execute SQL and return nickname


def get_nickname_good(user_id):
    users = sqlalchemy.Table(
        "users",
        sqlalchemy.MetaData(),
        sqlalchemy.Column("user_id", sqlalchemy.Integer),
        sqlalchemy.Column("nickname", sqlalchemy.String),
    )
    sql = sqlalchemy.sql.select([users.c.nickname]).where(users.c.user_id == user_id)
    # Execute SQL and return nickname


# -----------------------
# Example 3: Named Tuples
# -----------------------

from collections import namedtuple


def get_lat_lon(city_name):
    # Work out what the city's latitude and longitude are
    return lat, lon


lat_lon = get_lat_lon("London")
print(f"Latitude: {lat_lon[0]}, longitude: {lat_lon[1]}")

LatLonPair = namedtuple("LatLonPair", ["lat", "lon"])


def get_lat_lon(city_name):
    # Work out what the city's latitiude and longitude are
    return LatLonPair(lat, lon)


lat_lon = get_lat_lon("London")
print(f"Latitude: {lat_lon.lat}, longitude: {lat_lon.lon}")


# ---------------------
# Example 4: File paths
# ---------------------

from pathlib import Path

file_path_bad = "/" + "/".join(folders) + "/" + file
file_path_good = Path("/", *folders, file)


# --------------------
# Example 5: Datetimes
# --------------------

from datetime import timedelta

seconds_bad = 14
seconds_good = timedelta(seconds=14)
