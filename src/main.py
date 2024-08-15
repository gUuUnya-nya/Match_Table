from typing import NamedTuple
import inputinfo
import model
def main():
    univList = []
    while True:
        print("大学名を入力してください(終了する場合はexitと入力):")
        univName = input()
        if univName == "exit":
            break
        print("大学名:" + univName)
        univList.append(inputinfo.enter_info(univName))
        print(univList)
if __name__ == "__main__":
    main()