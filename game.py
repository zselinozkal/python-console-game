def tablo_yazdir(liste, tablo_genisligi, harf): # tabloyu yazdıran fonksiyon
    print(end="    ")
    for a in range(tablo_genisligi): # harfleri yazdıran döngü
        print(harf[a], end="   ")
    print("")
    print("   ", end="")
    print("--- " * tablo_genisligi)
    for i in range(tablo_genisligi): # listeyi ve tablonun sol tarafındaki sayıları yazdıran döngü
        print(i + 1, end=" | ")
        for n in range(tablo_genisligi):
            print(liste[i][n], end=" | ")

        print(i + 1)
        print("   ", end="")
        print("--- " * tablo_genisligi)
    print(end="    ")
    for b in range(tablo_genisligi):
        print(harf[b], end="   ")


def oyun(liste, tablo_genisligi, harf, harf_konum, tas1, tas2, tas1_sayi, tas2_sayi): # taşların hareketlerinin kodlandığı fonksiyon
    sayac = 0
    print("")
    print("Oyuna hoşgeldiniz!")
    oyun_bitti = "hayır"
    while True:
        try:
            while oyun_bitti == "hayır":
                if sayac % 2 == 0: # oyuncu sırasını belirliyoruz
                    tas = tas1
                    rakip_tas = tas2
                    oyuncu_sira = 1
                    rakip_oyuncu_sira = 2
                else:
                    tas = tas2
                    rakip_tas = tas1
                    oyuncu_sira = 2
                    rakip_oyuncu_sira = 1
                hata1 = "var"
                hata2 = "var"
                hata3 = "var"
                hata4 = "var"
                hata5 = "var"
                hata = "var"
                oyuncu = input(f"{oyuncu_sira}. oyuncu({tas}) taşı hangi konumdan hangi konuma oynatmak istiyorsunuz?(örn:1A 2A)")
                oyuncu = list(oyuncu)
                oyuncu[1] = oyuncu[1].upper() # harf_konum'da harfler büyük olarak tanımlandığı için bu bölüm inputa girilen küçük harfleri büyütüyor.
                oyuncu[4] = oyuncu[4].upper()
                index1 = int(oyuncu[0])   # değişkenlere inputun indexlerini atıyoruz
                index2 = harf_konum[oyuncu[1]]
                index4 = int(oyuncu[3])
                index5 = harf_konum[oyuncu[4]]

                while hata != "yok":
                    index1 = int(oyuncu[0])
                    index2 = harf_konum[oyuncu[1]]
                    index4 = int(oyuncu[3])
                    index5 = harf_konum[oyuncu[4]]
                    if index1 != index4 and index2 != index5: # çapraz ilerlemenin kontrolü
                        print("Çapraz ilerleyemezsiniz. Lütfen tekrar deneyiniz.")
                        hata1 = "var"
                    else:
                        hata1 = "yok"
                    if liste[index4 - 1][index5 - 1] != " ": # dolu olan yere ilerlememenin kontrolü
                        print("O konumda taş olduğu için ilerleyemezsiniz. Lütfen tekrar deneyiniz.")
                        hata2 = "var"
                    else:
                        hata2 = "yok"
                    if index1 == index4: # taşın üstünden yatay atlama yapılıyor mu kontrolü
                        if index5 > index2:
                            if index5 - index2:
                                hata3 = "yok"
                            for i in range(index2, index5-1):
                                if liste[index1 - 1][i] != " ":
                                    print("Yolunuzda taş var ilerleyemezsiniz!")
                                    hata3 = "var"
                                    break
                                else:
                                    hata3 = "yok"
                        elif index5 < index2:
                            if index2 - index5 == 1:
                                hata3 = "yok"
                            for i in range(index5, index2 - 1):
                                if liste[index1 - 1][i] != " ":
                                    print("Yolunuzda taş var ilerleyemezsiniz!")
                                    hata3 = "var"
                                    break
                                else:
                                    hata3 = "yok"
                    if index2 == index5: # taşın üstünden dikey atlama yapılıyor mu kontrolü
                        if index4 > index1:
                            if index4 - index1 == 1:
                                hata3 = "yok"
                            for i in range(index1 - 1, index4 -2):
                                if liste[i + 1][index2-1] != " ":
                                    print("Yolunuzda taş var ilerleyemezsiniz!")
                                    hata3 = "var"
                                    break
                                else:
                                    hata3 = "yok"
                        elif index4 < index1:
                            if index1-index4 == 1:
                                hata3 = "yok"
                            for i in range(index4, index1 -1):
                                if liste[i][index2 - 1] != " ":
                                    print("yolunuzda taş var ilerleyemezsiniz!")
                                    hata3 = "var"
                                    break
                                else:
                                    hata3 = "yok"
                    if liste[index1-1][index2-1] == " ":
                        print("Girdiğiniz başlangıç konumunda taş yok!") # başlangıç konumunda taş var mı kontrol
                        hata4 = "var"
                    else:
                        hata4 = "yok"
                    if liste[index1-1][index2-1] == rakip_tas:
                        print("Sadece kendi taşınızı oynatabilirsiniz!")
                        hata5 = "var"
                    else:
                        hata5 = "yok"
                    if hata1 == "yok" and hata2 == "yok" and hata3 == "yok" and hata4 == "yok" and hata5 == "yok":
                        # eğer hiçbir hata yok ise hata değişkeni "yok"a eşitleniyor
                        hata = "yok"
                    if hata != "yok":
                        oyuncu = (input(f"{oyuncu_sira}. oyuncu({tas}) taşı hangi konumdan hangi konuma oynatmak istiyorsunuz?(örn:1A 2A)"))
                        oyuncu = list(oyuncu)
                        oyuncu[1] = oyuncu[1].upper()
                        oyuncu[4] = oyuncu[4].upper()

                liste[index1 - 1][index2 - 1] = " " # ilk girilen konumdaki taş boşluğa dönüştürülüyor
                liste[index4 - 1][index5 - 1] = tas # son girilen konumdaki boşluk taşa dönüştürülüyor

                if tablo_genisligi - 1 >= index5 + 1: # yatay kilitlemeler
                    if liste[index4 - 1][index5 - 1] == liste[index4 - 1][index5 + 1] and liste[index4 - 1][index5] == rakip_tas:
                        liste[index4 - 1][index5] = " "
                        print(f"{rakip_oyuncu_sira}. oyuncunun {index4}{harf[index5]} konumundaki taşı oyundan çıktı.")
                if index5 - 3 >= 0:
                    if liste[index4 - 1][index5 - 1] == liste[index4 - 1][index5 - 3] and liste[index4 - 1][index5 - 2] == rakip_tas:
                        liste[index4 - 1][index5 - 2] = " "
                        print(f"{rakip_oyuncu_sira}. oyuncunun {index4}{harf[index5-2]} konumundaki taşı oyundan çıktı.")

                if tablo_genisligi - 1 >= index4 + 1: # dikey kilitlemeler
                    if liste[index4 - 1][index5 - 1] == liste[index4 + 1][index5 - 1] and liste[index4][index5 - 1] == rakip_tas:
                        liste[index4][index5 - 1] = " "
                        print(f"{rakip_oyuncu_sira}. oyuncunun {index4 +1}{harf[index5-1]} konumundaki taşı oyundan çıktı.")
                if index4 - 3 >= 0:
                    if liste[index4 - 1][index5 - 1] == liste[index4 - 3][index5 - 1] and liste[index4 - 2][index5 - 1] == rakip_tas:
                        liste[index4 - 2][index5 - 1] = " "
                        print(f"{rakip_oyuncu_sira}. oyuncunun {index4 - 1}{harf[index5 - 1]} konumundaki taşı oyundan çıktı.")

                if index4 - 1 == 0: # köşedeki kilitleme durumları
                    if index5 - 1 == 1:
                        if liste[1][0] == tas and liste[0][0] == rakip_tas:
                            liste[0][0] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun 1A konumundaki taşı oyundan çıktı.")
                    elif index5 - 1 == tablo_genisligi - 2:
                        if liste[1][tablo_genisligi - 1] == tas and liste[0][tablo_genisligi - 1] == rakip_tas:
                            liste[0][tablo_genisligi - 1] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun 1{harf[tablo_genisligi - 1]} konumundaki taşı oyundan çıktı")
                if index4 - 1 == 1:
                    if index5 - 1 == 0:
                        if liste[0][1] == tas and liste[0][0] == rakip_tas:
                            liste[0][0] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun 1A konumundaki taşı oyundan çıktı")
                    elif index5 - 1 == tablo_genisligi - 1:
                        if liste[0][tablo_genisligi - 2] == tas and liste[0][tablo_genisligi - 1] == rakip_tas:
                            liste[0][tablo_genisligi - 1] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun 1{harf[tablo_genisligi - 1]} konumundaki taşı oyundan çıktı")
                if index4 - 1 == tablo_genisligi - 2:
                    if index5 - 1 == 0:
                        if liste[tablo_genisligi - 1][1] == tas and liste[tablo_genisligi - 1][0] == rakip_tas:
                            liste[tablo_genisligi - 1][0] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun {tablo_genisligi-1}A konumundaki taşı oyundan çıktı")
                    elif index5 - 1 == tablo_genisligi - 1:
                        if liste[tablo_genisligi - 1][tablo_genisligi - 2] == tas and liste[tablo_genisligi - 1][tablo_genisligi - 1] == rakip_tas:
                            liste[tablo_genisligi - 1][tablo_genisligi - 1] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun {tablo_genisligi-1}{harf[tablo_genisligi - 1]} konumundaki taşı oyundan çıktı")
                if index4 - 1 == tablo_genisligi - 1:
                    if index5 - 1 == 1:
                        if liste[tablo_genisligi - 2][0] == tas and liste[tablo_genisligi - 1][0] == rakip_tas:
                            liste[tablo_genisligi - 1][0] = " "
                            print(f"{rakip_oyuncu_sira}. oyuncunun {tablo_genisligi-1}A konumundaki taşı oyundan çıktı")
                    elif index5 - 1 == tablo_genisligi - 2:
                        if liste[tablo_genisligi - 2][tablo_genisligi - 1] == tas and liste[tablo_genisligi - 1][tablo_genisligi - 1] == rakip_tas:
                            liste[tablo_genisligi - 1][tablo_genisligi - 1] = " "
                            print(f"{rakip_oyuncu_sira} oyuncunun {tablo_genisligi-1}{harf[tablo_genisligi - 1]} konumundaki taşı oyundan çıktı")

                tablo_yazdir(liste, tablo_genisligi, harf)
                print("")
                for a in range(tablo_genisligi): # oyunun bittiğini anlamak için kontrol
                    for s in liste[a]:
                        if s == tas1:
                            tas1_sayi.append(s)
                for b in range(tablo_genisligi):
                    for k in liste[b]:
                        if k == tas2:
                            tas2_sayi.append(k)
                if len(tas1_sayi) == 1 or len(tas1_sayi) == 0:
                    oyun_bitti = "evet"
                    print("OYUN BİTTİ")
                    print("KAZANAN 2. OYUNCU")

                elif len(tas2_sayi) == 1 or len(tas2_sayi) == 0:
                    oyun_bitti = "evet"
                    print("OYUN BİTTİ")
                    print("KAZANAN 1. OYUNCU")

                else:
                    oyun_bitti = "hayır"
                    sayac += 1
                tas1_sayi = []
                tas2_sayi = []
            break
        except ValueError: # try exceptler
            print("Hatalı giriş. Lütfen 1B 4B gibi girişler yapınız.")
        except KeyError:
            print("Hatalı giriş. Lütfen 1B 4B gibi girişler yapınız.")
        except IndexError:
            print("Hatalı giriş. Lütfen 1B 4B gibi girişler yapınız.")


def main():
    devam = "e"
    while devam == "e" or devam == "E":
        a = "a"
        while a == "a":
            try:
                tablo_genisligi = int(input("Oyun tablosunun genişliği kaç kare olsun? "))
                a = "b"
                while tablo_genisligi < 4 or tablo_genisligi > 8:  # tablo genişliği kopntrol
                    print("tablo genişliği 4x4 ve 8x8 arasında olmalıdır.")
                    tablo_genisligi = int(input("Oyun tablosunun genişliği kaç kare olsun? "))
            except ValueError:
                print("Integer girmediniz. Tekrar deneyin!")
                a = "a"
        liste = []
        harf_konum = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        harf = ["A", "B", "C", "D", "E", "F", "G", "H"]
        tas1_sayi = []
        tas2_sayi = []
        for i in range(tablo_genisligi):
            list_2 = [" "] * tablo_genisligi
            liste.append(list_2)
        hata = "var"
        tas1 = input("1. oyuncu için taş: ")
        while hata != "yok": # taşlar düzgün girilmiş mi kontrol
            if len(tas1) > 1 or len(tas1) == 0:
                print("Taşınız 1 karakterden fazla ya da az olamaz! Tekrar deneyin.")
                hata1 = "var"
            else:
                hata1 = "yok"
            if tas1 == " ":
                print("Boşluğu karakter olarak kullanamazsınız! Tekrar deneyin.")
                hata2 = "var"
            else:
                hata2 = "yok"
            if hata1 == "yok" and hata2 == "yok":
                hata = "yok"
            if hata != "yok":
                tas1 = input("1. oyuncu için taş: ")
        hata = "var"
        tas2 = input("2. oyuncu için taş: ")
        while hata != "yok":
            if len(tas2) > 1 or len(tas2) == 0:
                print("Taşınız 1 karakterden fazla ya da az olamaz! Tekrar deneyin.")
                hata1 = "var"
            else:
                hata1 = "yok"
            if tas2 == " ":
                print("Boşluğu karakter olarak kullanamazsınız! Tekrar deneyin.")
                hata2 = "var"
            else:
                hata2 = "yok"
            if tas1 == tas2:
                print("Oyuncu 1 ile aynı taşı giremezsiniz! Tekrar deneyin.")
                hata3 = "var"
            else:
                hata3 = "yok"
            if hata1 == "yok" and hata2 == "yok" and hata3 == "yok":
                hata = "yok"
            if hata != "yok":
                tas2 = input("2. oyuncu için taş: ")

        for i in range(tablo_genisligi): # ikili liste oluşturma
            liste[0][i] = tas2
            liste[tablo_genisligi - 1][i] = tas1
        tablo_yazdir(liste, tablo_genisligi, harf)
        oyun(liste, tablo_genisligi, harf, harf_konum, tas1, tas2, tas1_sayi, tas2_sayi)
        devam = input("devam etmek istiyor musunuz?(e/E/h/H): ")

main()
