from typing import NamedTuple
import model
def enter_info(univName):
    print("check")
    print(univName + "の団体戦の順位を入力してください:")
    TeamRank = int(input())
    pairs = list[model.Pair]
    while True:
        print("後衛の名前を入力してください(終了する場合はexit):")
        backPlayer = input()
        if backPlayer == "exit":
            break
        print("後衛の前回の順位を入力してください:")
        previousRankOfBack = int(input())
        print("前衛の名前を入力してください:")
        frontPlayer = input()
        print("前衛の前回の順位を入力してください:")
        previousRankOfFront = int(input())
        print("ペアの学内順位を入力してください:")
        schoolRank = int(input())
        pair = model.Pair(backPlayer, frontPlayer, previousRankOfBack, previousRankOfFront, schoolRank)
        pairs.append(pair)
    univ = model.Univ(univName, pairs, TeamRank)
    return univ