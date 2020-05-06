#!/usr/bin/env python3
import itertools
x = int(input())
l = [0, 1, 32, 243, 1024, 3125, 7776, 16807, 32768, 59049, 100000, 161051, 248832, 371293, 537824, 759375, 1048576, 1419857, 1889568, 2476099, 3200000, 4084101, 5153632, 6436343, 7962624, 9765625, 11881376, 14348907, 17210368, 20511149, 24300000, 28629151, 33554432, 39135393, 45435424, 52521875, 60466176, 69343957, 79235168, 90224199, 102400000, 115856201, 130691232, 147008443, 164916224, 184528125, 205962976, 229345007, 254803968, 282475249, 312500000, 345025251, 380204032, 418195493, 459165024, 503284375, 550731776, 601692057, 656356768, 714924299, 777600000, 844596301, 916132832, 992436543, 1073741824, 1160290625, 1252332576, 1350125107, 1453933568, 1564031349, 1680700000, 1804229351, 1934917632, 2073071593, 2219006624, 2373046875, 2535525376, 2706784157, 2887174368, 3077056399, 3276800000, 3486784401, 3707398432, 3939040643, 4182119424, 4437053125, 4704270176, 4984209207, 5277319168, 5584059449, 5904900000, 6240321451, 6590815232, 6956883693, 7339040224, 7737809375, 8153726976, 8587340257, 9039207968, 9509900499, 10000000000, 10510100501, 11040808032, 11592740743, 12166529024, 12762815625, 13382255776, 14025517307, 14693280768, 15386239549, 16105100000, 16850581551, 17623416832, 18424351793, 19254145824, 20113571875, 21003416576, 21924480357, 22877577568, 23863536599, 24883200000, 25937424601, 27027081632, 28153056843, 29316250624, 30517578125, 31757969376, 33038369407, 34359738368, 35723051649, 37129300000, 38579489651, 40074642432, 41615795893, 43204003424, 44840334375, 46525874176, 48261724457, 50049003168, 51888844699, 53782400000, 55730836701, 57735339232, 59797108943, 61917364224, 64097340625, 66338290976, 68641485507]
for comb in itertools.combinations_with_replacement(l, 2):
    if comb[0] - comb[1] == x:
        print(l.index(comb[0]), l.index(comb[1]))
        exit()
    elif comb[0] + comb[1] == x:
        print(l.index(comb[0]), -(l.index(comb[1])))
        exit()
    elif - comb[0] + comb[1] == x:
        print(-(l.index(comb[0])), -(l.index(comb[1])))
        exit()
    elif - comb[0] - comb[1] == x:
        print(-(l.index(comb[0])), l.index(comb[1]))
        exit() 