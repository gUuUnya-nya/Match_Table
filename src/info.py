from typing import NamedTuple
import model
#各大学の情報を入力させる関数
def enter_info(univName):
    print(univName + "の団体戦の順位を入力してください:")
    TeamRank = int(input())
    pairs = []
    count = 0
    while True:
        print("学内の順位順に選手の情報を入力してください")
        count += 1
        print("学内順位" + str(count) + "位のペアの情報を入力してください")
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
        schoolRank = count
        pair = model.Pair(backPlayer, frontPlayer, previousRankOfBack, previousRankOfFront, schoolRank)
        print(pair)
        pairs.append(pair)
        print(pairs)
    univ = model.Univ(univName, pairs, TeamRank)
    return univ