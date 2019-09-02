# -----------------------------
# Example 1: Swapping Variables
# -----------------------------

customer_1 = {"first_name": "John", "last_name": "Smith"}


def swap_names_bad(customer):
    temp = customer["first_name"]
    customer["first_name"] = customer["last_name"]
    customer["last_name"] = temp


def swap_names_good(customer):
    customer["first_name"], customer["last_name"] = (
        customer["last_name"],
        customer["first_name"],
    )


# If Python didn't allow us to do the trick in `swap_names_good`, we
# could still adhere to the "keep core logic obvious" idea in the
# following way:


def swap_names_alternative(customer):
    swap_dict_values(customer, "first_name", "last_name")


def swap_dict_values(dict_, key1, key2):
    temp = dict_[key1]
    dict_[key1] = dict_[key2]
    dict_[key2] = temp


# ---------------------------
# Example 2: Context Managers
# ---------------------------

from contextlib import contextmanager
import logging

# This import is just hypothetical - we postulate the existence of a
# `database` package that offers an API `get_user_by_id` that takes a
# user ID and returns some kind of data about that user. If the user
# isn't found then an `ItemNotFoundError` is raised.
from database import get_user_by_id, ItemNotFoundError

logger = logging.getLogger(__name__)


def get_user_data_bad(user_id):
    logger.debug("Retrieving user %s from database", user_id)
    try:
        user_data = get_user_by_id(user_id)
    except ItemNotFoundError:
        logger.warning("User ID %s was not found", user_id)
    except Exception:
        logger.critical("Error for user %s", user_id, exc_info=True)
    else:
        logger.debug("Retrieved user ID %s from database", user_id)


def get_user_data_good(user_id):
    with db_logger(user_id, "user", logger):
        user_data = get_user_by_id(user_id)


@contextmanager
def db_logger(artifact_id, artifact_type, logger):
    logger.debug("Retrieving %s %s from database", artifact_type, artifact_id)
    try:
        yield
    except ItemNotFoundError:
        logger.warning("%s ID %s was not found", artifact_type, artifact_id)
    except Exception:
        logger.critical("Error for %s %s", artifact_type, artifact_id, exc_info=True)
    else:
        logger.debug("Retrieved %s ID %s from database", artifact_type, artifact_id)
