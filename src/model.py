from typing import NamedTuple
class Pair(NamedTuple):
    BackPlayer: str
    FrontPlayer: str
    PreviousRankOfBack: int
    PreviousRankOfFront: int
    SchoolRank: int
class Univ(NamedTuple):
    UnivName: str
    Pairs: list[Pair]
    TeamRank: int