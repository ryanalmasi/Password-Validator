from passwordvalidate import *
tests = ['1Q#awb0!','NP6;B*ZB6Y~K','qO8RoewCdVqfCFQd','$1JFKOJT=','~JF3~,VM0,<NQF UH','8UD^R0SOIT','mG,7>NW#F'," ",'v/4cgb]t;p:4r/3|m{>^?d;*!33','(4mA(L>%D','w+Mhs}FVEqjDFfyv$-zT;',"srk[y$|jhci&>'|qjo",'7{QTN]QBC?IKDSE[YPVC2Q','i!oWbEdb;yxp@eX.xsnno','j2zatczvhwcxtgHJg','IEV:YBY9`$E@POQDTHC%2Z<',"{g@1c!'<cra}y","L3HY`20J2'9QCKGE","4$sN!sF]YUguzwW4]D(km3","9bT?l2h[fHVJ","9c,A2P3K~y#LK0ziJAdDQ}N","=bI8SsW6D-c@;w4K[w76*=3D","]F1mk?ZsBAl^vi$HeF'$#+m[AwC","c]c8ff+-9p?)kb~",")M3wm@.f9wmB1~%F","4x*I5CtwZ=gm^?D-)?<N15%E>I5","!c7B","[xY8UEw7bEQW&","4;tB&:&|.nOaSHPu","B;d6pjk1'#a]x","i3","N)M?L/.`=H||QK;ILXGB<","r]1KGutZ=+T","~mQ74#yz>e(JS_p","uu8SueDvalo","2>WkMv","m0DdSDlTGqe4nyDv1Uq3O0","z3dzbmqqpjluk^",".ypGWk(a","3#%CnrNW;o","Kq:31rMhVJFrzA!X{V.?^uHIt~!","g?-gjpzb&xd1u}0|e[fvddp.cu","RMVR1HERAEKV","7d?Km>].B}Z5~G-1P8%AK*+f","7)eo5v'k;kxoeohol>","9X","<qr:6(jthj^io@bmnf&ey",".4Eh6 HA7fY","4p$Me-uN4UGNGFs[UF[","}8PYBDU|$<~ODOUM_,!$4"]
expected = ['Invalid','Insecure','Insecure','Insecure','Invalid','Insecure','Invalid','Invalid','Insecure','Secure','Insecure','Insecure','Insecure','Invalid','Insecure','Invalid','Invalid','Insecure','Secure','Secure','Invalid','Invalid','Invalid','Insecure','Invalid','Secure','Invalid','Secure','Secure','Invalid','Invalid','Insecure','Secure','Invalid','Insecure','Invalid','Insecure','Insecure','Insecure','Invalid','Secure','Insecure','Insecure','Secure','Insecure','Invalid','Invalid','Invalid','Secure',"Insecure"]
pass_count = 0
fail_count = 0
failed = []
failed_index = []
for test in tests:
    if validate(test) == expected[tests.index(test)]:
        pass_count += 1
        print('Pass')
    else:
        fail_count += 1
        print('Fail')
        failed_index.append(tests.index(test))
        failed.append(test)
print("Passed:",str(pass_count))
print("Failed:",str(fail_count))

for i in range(len(failed)):
    print('Failed test #' + str(failed_index[i]) + ' which was ' + "'" + failed[i] + "'")