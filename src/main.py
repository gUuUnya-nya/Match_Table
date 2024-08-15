from typing import NamedTuple
import info
import model
def main():
    #入力を受け付ける
    univList = []
    while True:
        print("大学名を入力してください(終了する場合はexitと入力):")
        univName = input()
        if univName == "exit":
            break
        print("大学名:" + univName)
        univList.append(info.enter_info(univName))
    #シード順にリストに格納する
    list = info.define_seed(univList)
    print(list)
if __name__ == "__main__":
    main()