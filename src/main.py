from typing import NamedTuple
import info
import model
import makePDF
def main():
    #入力を受け付ける
#以下入力がめんどくさいのでlistを作成しておく。入力関数はコメントアウト
#    univList = []
#    while True:
#        print("大学名を入力してください(終了する場合はexitと入力):")
#        univName = input()
#        if univName == "exit":
#            break
#        print("大学名:" + univName)
#        univList.append(info.enter_info(univName))
#ここまで
    #シード順にリストに格納する
    univList = [model.Univ(UnivName='東工大', Pairs=[model.Pair(BackPlayer='浜野', FrontPlayer='鈴木', PreviousRankOfBack=16, PreviousRankOfFront=4, SchoolRank=1, TeamRank=3, UnivName='東工大'), 
                                                  model.Pair(BackPlayer='長柄', FrontPlayer='渡辺', PreviousRankOfBack=16, PreviousRankOfFront=4, SchoolRank=2, TeamRank=3, UnivName='東工大'), 
                                                  model.Pair(BackPlayer='山中', FrontPlayer='松尾', PreviousRankOfBack=16, PreviousRankOfFront=8, SchoolRank=3, TeamRank=3, UnivName='東工大')], 
                                                  TeamRank=3), 
                model.Univ(UnivName='芝浦', Pairs=[model.Pair(BackPlayer='永井', FrontPlayer='三井', PreviousRankOfBack=16, PreviousRankOfFront=4, SchoolRank=1, TeamRank=2, UnivName='芝浦'), 
                                                 model.Pair(BackPlayer='unko', FrontPlayer='kasu', PreviousRankOfBack=16, PreviousRankOfFront=4, SchoolRank=2, TeamRank=2, UnivName='芝浦')], 
                                                 TeamRank=2)]
    list = info.define_seed(univList)
    print(list)
    #PDFを作成する
    makePDF.makePdf("test")
if __name__ == "__main__":
    main()