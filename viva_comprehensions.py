import enum
import math
from typing import List, Dict, Set, Callable



class Parity(enum.Enum):
    ODD = 0
    EVEN = 1


def gen_list(start: int, stop: int, parity: Parity) -> List[int]:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param start:
    :param stop:
    :param parity:
    :return:
    """
    return [parity.EVEN if x % 2== 0 else parity.ODD for x in range(start, stop)]
    # returns even if x is even else false for x in range of start to stop


def gen_dict(start: int, stop: int, strategy: Callable) -> Dict:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.


    :param start:
    :param stop:
    :param strategy:
    :return:
    """
    return {x: strategy(x) for x in range(start, stop)}
    # the key is x, which is an integer in range of start to stop
    # the value is the return of calling the function strategy on x

def gen_set(val_in: str) -> Set:
    """
    Oh no some evil developer decided not to write docstrings. Maybe you can use the test cases to decipher
    what this method was supposed to do. Hey if you do, maybe you could do some good in this world by
    updating this here docstring to something useful.

    :param val_in:
    :return:
    """
    return {letter.upper() for letter in val_in if letter == letter.lower()}
    # make the letter uppercase if the letter in val_in is lowercase
