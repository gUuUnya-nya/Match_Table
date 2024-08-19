from typing import NamedTuple
from typing import List
class Pair(NamedTuple):
    BackPlayer: str
    FrontPlayer: str
    PreviousRankOfBack: int #後衛の順位
    PreviousRankOfFront: int #前衛の順位
    SchoolRank: int #学内の順位
    TeamRank: int #団体戦の順位
    UnivName: str #大学名
class Univ(NamedTuple):
    UnivName: str
    Pairs: List[Pair]
    TeamRank: int