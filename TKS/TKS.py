bir_1 = "AACEDECEDBAC"
bir_2 = "CCEECDAECDBD"
bir_3 = "ECABDDDEEDEE"
bir_4 = "ADECCEACBDDA"
bir_5 = "ECDEDAEEAECB"
iki_1 = "EDCCBEAACCBA"
iki_2 = "EAAAEABCACAE"
iki_3 = "ADCACCBAACBE"
iki_4 = "EBDCADACECAB"
iki_5 = "BAEDBCBAEACA"
iki_6 = "EAAACBCCABBD"
uc_1 = "AEDABDBBBCDC"
uc_2 = "AAEEEDBAACCD"
uc_3 = "ECBECDACEEBA"
uc_4 = "EDABDDEAEDAC"
uc_5 = "CECDAEBECDCD"
uc_6 = "EDEDCDEBDCDC"
uc_7 = "ECEACCEBBEBE"
osym_1 = "EDBAAACACCDEDDED"
sarmal_1 = "BEAEBAEBAADBEDDE"
dort_1 = "ABCEEBADDAAE"
dort_2 = "DADDCCDBBEAB"
dort_3 = "DBDBDDBCBEBB"
dort_4 = "CCACBBABBDDE"
dort_5 = "ABCCDBCCAABD"
dort_6 = "BDBECBBBCECB"
dort_7 = "EBCCCCBEBEAB"
dort_8 = "ADCCACBABCDD"
bes_1 = "DAEBEDBAEAED"
bes_2 = "BDABDAADBDDA"
bes_3 = "ABCEBDDEAABE"
bes_4 = "DEEDDCADEECB"
osym_2 = "CCBCBCEACCAECAADBC"
sarmal_2 = "CCEBACEACDAACCDABEEA"
bes_5 = "CBECEEDBDCCC"
bes_6 = "ADBACDBCADCA"
bes_7 = "DACDEABDEABB"
bes_8 = "CABCADCECADD"
bes_9 = "DECDDEEEECEE"
sim1_1 = "ABEDDCEBCD"
sim1_2 = "DECABABCD"
sim1_3 = "CDBDDEDBEA"
sim1_4 = "ECDCABECAE"
sim1_5 = "CEDECCDDDE"
sim1_6 = "EBDCCDE"
sim2_1 = "ECEBEACACCBCAABCCBEAE"
sim2_2 = "AABCBCDCDACBABDDCDADA"
sim2_3 = "ADDDDBCCEECBDECADDCC"
sim2_4 = "EEDBACEADBDBDCBDEDCDE"
sim2_5 = "BDBACDDCCAACCDEABDCAC"
sim2_6 = "EBBECCABCCAADECEBAECDBC"
sim2_7 = "CAEADBBDBEDBBCEBCBCACC"
sim2_8 = "DBBCCADCADACBEADEDECDB"
sim2_9 = "EBAEBDCDADBECBEBAADADD"
sim2_10 = "CADBDEBBEECCBABBBCBDC"
sim2_11 = "BDABAECBCACCDABCABDADA"
sim2_12 = "ECAEEADDBEBCDAECBEADDB"
sim2_13 = "ECACDEEBEDDDCDEEEBDEDAB"
sim2_14 = "DBAAACCBBABCBCADBDDBEBA"
sim2_15 = "AADDDBAAEDBCAAECBCAABB"
sim2_16 = "EBCDABBADEDBDABDCBDDBCB"
sim2_17 = "CEACEACBCCBBEADBAAEABCB"
sim2_18 = "DECADBCDCEBEEABBACBCEAB"
sim2_19 = "DEEEBCAACEBAACCBEABCDCA"
sim2_20 = "DBECABBEDEDDCDDCBEAAADC"
yanlislar = open("yanlislar.txt","a")
kayit = open("kayitlar.txt","a")
while True:
    sayfa = input("Kaçıncı Sayfayı Kontrol Ediceksin: ")
    while True:
        dk = input("Kaç Dakikada Bitirdin: ")
        yanlislar.write("----------------------------------\n")
        kayit.write("----------------------------\n")
        if sayfa == "9":
            yanlislar.write("       1.Ünite----1.Test\n")
            kayit.write("     1.Ünite------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bir_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bir_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bir_1[s] + "\n")
                            elif bir_1[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(bir_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "12":
            yanlislar.write("       1.Ünite----2.Test\n")
            kayit.write("     1.Ünite------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bir_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bir_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bir_2[s] + "\n")
                            elif bir_2[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(bir_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "15":
            yanlislar.write("       1.Ünite----3.Test\n")
            kayit.write("     1.Ünite------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bir_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bir_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bir_3[s] + "\n")
                            elif bir_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bir_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "19":
            yanlislar.write("       1.Ünite----4.Test\n")
            kayit.write("     1.Ünite------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bir_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bir_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bir_4[s] + "\n")
                            elif bir_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bir_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "22":
            yanlislar.write("       1.Ünite----5.Test\n")
            kayit.write("     1.Ünite------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bir_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bir_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bir_5[s] + "\n")
                            elif bir_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bir_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "27":
            yanlislar.write("       2.Ünite----1.Test\n")
            kayit.write("     2.Ünite------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_1[s] + "\n")
                            elif iki_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "30":
            yanlislar.write("       2.Ünite----2.Test\n")
            kayit.write("     2.Ünite------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_2[s] + "\n")
                            elif iki_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "33":
            yanlislar.write("       2.Ünite----3.Test\n")
            kayit.write("     2.Ünite------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_3[s] + "\n")
                            elif iki_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "36":
            yanlislar.write("       2.Ünite----4.Test\n")
            kayit.write("     2.Ünite------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_4[s] + "\n")
                            elif iki_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "40":
            yanlislar.write("       2.Ünite----5.Test\n")
            kayit.write("     2.Ünite------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_5[s] + "\n")
                            elif iki_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "44":
            yanlislar.write("       2.Ünite----6.Test\n")
            kayit.write("     2.Ünite------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(iki_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if iki_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + iki_6[s] + "\n")
                            elif iki_6[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(iki_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "49":
            yanlislar.write("       3.Ünite----1.Test\n")
            kayit.write("     3.Ünite------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_1[s] + "\n")
                            elif uc_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "52":
            yanlislar.write("       3.Ünite----2.Test\n")
            kayit.write("     3.Ünite------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_2[s] + "\n")
                            elif uc_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "55":
            yanlislar.write("       3.Ünite----3.Test\n")
            kayit.write("     3.Ünite------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_3[s] + "\n")
                            elif uc_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "59":
            yanlislar.write("       3.Ünite----4.Test\n")
            kayit.write("     3.Ünite------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_4[s] + "\n")
                            elif uc_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "63":
            yanlislar.write("       3.Ünite----5.Test\n")
            kayit.write("     3.Ünite------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_5[s] + "\n")
                            elif uc_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "67":
            yanlislar.write("       3.Ünite----6.Test\n")
            kayit.write("     3.Ünite------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_6[s] + "\n")
                            elif uc_6[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "70":
            yanlislar.write("       3.Ünite----7.Test\n")
            kayit.write("     3.Ünite------7.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(uc_7):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if uc_7[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + uc_7[s] + "\n")
                            elif uc_7[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(uc_7):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "73":
            yanlislar.write("       ÖSYM------1.Test\n")
            kayit.write("     ÖSYM------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(osym_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if osym_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + osym_1[s] + "\n")
                            elif osym_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(osym_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "77":
            yanlislar.write("       Sarmal----1.Test\n")
            kayit.write("     Sarmal------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sarmal_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sarmal_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sarmal_1[s] + "\n")
                            elif sarmal_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sarmal_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "83":
            yanlislar.write("       4.Ünite----1.Test\n")
            kayit.write("     4.Ünite------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_1[s] + "\n")
                            elif dort_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "86":
            yanlislar.write("       4.Ünite----2.Test\n")
            kayit.write("     4.Ünite------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_2[s] + "\n")
                            elif dort_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "89":
            yanlislar.write("       4.Ünite----3.Test\n")
            kayit.write("     4.Ünite------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_3[s] + "\n")
                            elif dort_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "92":
            yanlislar.write("       4.Ünite----4.Test\n")
            kayit.write("     4.Ünite------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_4[s] + "\n")
                            elif dort_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "95":
            yanlislar.write("       4.Ünite----5.Test\n")
            kayit.write("     4.Ünite------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_5[s] + "\n")
                            elif dort_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "98":
            yanlislar.write("       4.Ünite----6.Test\n")
            kayit.write("     4.Ünite------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_6[s] + "\n")
                            elif dort_6[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "101":
            yanlislar.write("       4.Ünite----7.Test\n")
            kayit.write("     4.Ünite------7.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_7):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_7[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_7[s] + "\n")
                            elif dort_7[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_7):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "104":
            yanlislar.write("       4.Ünite----8.Test\n")
            kayit.write("     4.Ünite------8.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(dort_8):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if dort_8[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + dort_8[s] + "\n")
                            elif dort_8[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(dort_8):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "109":
            yanlislar.write("       5.Ünite----1.Test\n")
            kayit.write("     5.Ünite------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_1[s] + "\n")
                            elif bes_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "112":
            yanlislar.write("       5.Ünite----2.Test\n")
            kayit.write("     5.Ünite------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_2[s] + "\n")
                            elif bes_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "115":
            yanlislar.write("       5.Ünite----3.Test\n")
            kayit.write("     5.Ünite------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_3[s] + "\n")
                            elif bes_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "118":
            yanlislar.write("       5.Ünite----4.Test\n")
            kayit.write("     5.Ünite------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_4[s] + "\n")
                            elif bes_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "121":
            yanlislar.write("       ÖSYM------2.Test\n")
            kayit.write("     ÖSYM--------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(osym_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if osym_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + osym_2[s] + "\n")
                            elif osym_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(osym_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "126":
            yanlislar.write("       Sarmal----2.Test\n")
            kayit.write("     Sarmal------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sarmal_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sarmal_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sarmal_2[s] + "\n")
                            elif sarmal_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sarmal_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "131":
            yanlislar.write("       5.Ünite----5.Test\n")
            kayit.write("     5.Ünite------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_5[s] + "\n")
                            elif bes_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "134":
            yanlislar.write("       5.Ünite----6.Test\n")
            kayit.write("     5.Ünite------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_6[s] + "\n")
                            elif bes_6[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "138":
            yanlislar.write("       5.Ünite----7.Test\n")
            kayit.write("     5.Ünite------7.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_7):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_7[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_7[s] + "\n")
                            elif bes_7[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_7):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "141":
            yanlislar.write("       5.Ünite----8.Test\n")
            kayit.write("     5.Ünite------8.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_8):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_8[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_8[s] + "\n")
                            elif bes_8[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_8):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "144":
            yanlislar.write("       5.Ünite----9.Test\n")
            kayit.write("     5.Ünite------9.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(bes_9):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if bes_9[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + bes_9[s] + "\n")
                            elif bes_9[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(bes_9):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "147":
            yanlislar.write("       1_Sim----1.Test\n")
            kayit.write("     1_Sim------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_1[s] + "\n")
                            elif sim1_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "150":
            yanlislar.write("       1_Sim----2.Test\n")
            kayit.write("     1_Sim------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_2[s] + "\n")
                            elif sim1_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "154":
            yanlislar.write("       1_Sim----3.Test\n")
            kayit.write("     1_Sim------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_3[s] + "\n")
                            elif sim1_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "157":
            yanlislar.write("       1_Sim----4.Test\n")
            kayit.write("     1_Sim------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_4[s] + "\n")
                            elif sim1_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "160":
            yanlislar.write("       1_Sim----5.Test\n")
            kayit.write("     1_Sim------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_5[s] + "\n")
                            elif sim1_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "165":
            yanlislar.write("       1_Sim----6.Test\n")
            kayit.write("     1_Sim------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim1_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim1_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim1_6[s] + "\n")
                            elif sim1_6[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim1_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "170":
            yanlislar.write("       2_Sim----1.Test\n")
            kayit.write("     2_Sim------1.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_1):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_1[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_1[s] + "\n")
                            elif sim2_1[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_1):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "175":
            yanlislar.write("       2_Sim----2.Test\n")
            kayit.write("     2_Sim------2.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_2):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_2[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_2[s] + "\n")
                            elif sim2_2[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_2):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "180":
            yanlislar.write("       2_Sim----3.Test\n")
            kayit.write("     2_Sim------3.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_3):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_3[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_3[s] + "\n")
                            elif sim2_3[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_3):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "185":
            yanlislar.write("       2_Sim----4.Test\n")
            kayit.write("     2_Sim------4.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_4):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_4[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_4[s] + "\n")
                            elif sim2_4[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_4):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "190":
            yanlislar.write("       2_Sim----5.Test\n")
            kayit.write("     2_Sim------5.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_5):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_5[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_5[s] + "\n")
                            elif sim2_5[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_5):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "196":
            yanlislar.write("       2_Sim----6.Test\n")
            kayit.write("     2_Sim------6.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_6):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_6[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_6[s] + "\n")
                            elif sim2_6[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_6):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "202":
            yanlislar.write("       2_Sim----7.Test\n")
            kayit.write("     2_Sim------7.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_7):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_7[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_7[s] + "\n")
                            elif sim2_7[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_7):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "208":
            yanlislar.write("       2_Sim----8.Test\n")
            kayit.write("     2_Sim------8.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_8):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_8[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_8[s] + "\n")
                            elif sim2_8[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_8):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "214":
            yanlislar.write("       2_Sim----9.Test\n")
            kayit.write("     2_Sim------9.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_9):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_9[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_9[s] + "\n")
                            elif sim2_9[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_9):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "220":
            yanlislar.write("       2_Sim----10.Test\n")
            kayit.write("     2_Sim------10.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_10):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_10[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_10[s] + "\n")
                            elif sim2_10[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_10):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "225":
            yanlislar.write("       2_Sim----11.Test\n")
            kayit.write("     2_Sim------11.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_11):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_11[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_11[s] + "\n")
                            elif sim2_11[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_11):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "231":
            yanlislar.write("       2_Sim----12.Test\n")
            kayit.write("     2_Sim------12.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_12):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_12[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_12[s] + "\n")
                            elif sim2_12[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_12):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "237":
            yanlislar.write("       2_Sim----13.Test\n")
            kayit.write("     2_Sim------13.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_13):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_13[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_13[s] + "\n")
                            elif sim2_13[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_13):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "243":
            yanlislar.write("       2_Sim----14.Test\n")
            kayit.write("     2_Sim------14.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_14):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_14[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_14[s] + "\n")
                            elif sim2_14[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_14):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "249":
            yanlislar.write("       2_Sim----15.Test\n")
            kayit.write("     2_Sim------15.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_15):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_15[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_15[s] + "\n")
                            elif sim2_15[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_15):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "255":
            yanlislar.write("       2_Sim----16.Test\n")
            kayit.write("     2_Sim------1.T6est\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_16):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_16[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_16[s] + "\n")
                            elif sim2_16[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_16):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "261":
            yanlislar.write("       2_Sim----17.Test\n")
            kayit.write("     2_Sim-----17.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_17):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_17[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_17[s] + "\n")
                            elif sim2_17[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_17):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "267":
            yanlislar.write("       2_Sim----18.Test\n")
            kayit.write("     2_Sim------18.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_18):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_18[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_18[s] + "\n")
                            elif sim2_18[s] == cb[s]:
                                d+=1
                            elif cb[s] == " ":
                                b+=1
                            s+=1
                            if s == len(sim2_18):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "273":
            yanlislar.write("       2_Sim----19.Test\n")
            kayit.write("     2_Sim------19.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_19):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_19[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_19[s] + "\n")
                            elif sim2_19[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_19):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        elif sayfa == "279":
            yanlislar.write("       2_Sim----20.Test\n")
            kayit.write("     2_Sim------20.Test\n")
            while True:
                c_b = input("Cevap Anahtarını Giriniz:")
                cb = c_b.upper()
                a = 0
                c = 0
                while True:
                    if len(cb) == len(sim2_20):
                        for i in list(cb):
                            if i == "A" or i == "B" or i == "C" or i == "D" or i == "E" or i == " ":
                                a = 1
                                continue
                            else:
                                print("Cevap Anahtarında Sadece A,B,C,D,E Veya Boşluk Olabilir...")
                                c = 5
                                break
                        s = 0
                        b = 0
                        d = 0
                        y = 0
                        n = 0
                        while a == 1:
                            if sim2_20[s] != cb[s]:
                                if cb[s] == " ":
                                    b+=1
                                else:
                                    y+=1
                                    yanlislar.write((" "*3) + str(s+1) + ".Soru Yanlış      Cevabı:" + sim2_20[s] + "\n")
                            elif sim2_20[s] == cb[s]:
                                d+=1
                            s+=1
                            if s == len(sim2_20):
                                break
                        n = d - y/4
                        if c !=5:
                            print("Toplam " + dk + " Dakikada " + str(s) + " Kadar Soru Çözmüşsün.")
                            print("Net Sayın:" + str(n) + "\nDoğru Sayın:" + str(d) + "\nYanlış Sayın:" + str(y) + "\nBoş Sayın:" + str(b))
                            kayit.write((" "*7) + "Toplam Soru:" + str(s) + "\n" + (" "*7) + "Toplam Süre:" + dk + "\n" + (" "*7) + "Net Sayın:" + str(n)  + "\n" + (" "*7) + "Doğru Sayın:" + str(d) + "\n" + (" "*7) + "Yanlış Sayın:" + str(y) + "\n" + (" "*7) + "Boş Sayın:" + str(b) + "\n")
                            exit()
                        break
                    else:
                        print("Soru Sayısını Fazladan Veya Eksik Girmeyin...")
                        break
        else:
            print("Hatalı Sayfa Numarası Girdiniz.Tekrar Deneyiniz...")
            break
    #27/08/2021-04:30 p.m  ---  28/08/2021-04:11 a.m                               
    #Maked BY Kamil
    #Toplam 3107 Satır Kod Vardır..
    #Toplam 146.151 Tane Harf Vardır...
    #Amaç:Soru Kontrol Eden Bir Kod Geliştirme.
    #Ek Fikir-1:Kayıtları Karşılaştıran Bir Sistem.
    #Ek Fikir-2:Haftada Bir Kayıtları Hocaya Mail Olarak Atma. 
    #Sonuç:Program Hatasız Çalışıyor