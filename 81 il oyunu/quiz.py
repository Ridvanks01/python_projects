pattern = "-------------------------------------------------"
temp = True

print( pattern + "\n       81 İL BİLGİ YARIŞMASINA HOŞGELDİNİZ!\n" + pattern)


while(temp):
    
    answer = input("\nZorluk Seviyesini Seçiniz\n\n1.Kolay (10 soru - 2 şık)\n2.Orta  (15 soru - 3 şık)\n3.Zor   (20 soru - 4 şık)\n0.Çıkış\n\nNot: Bütün sorularda 0 a basarak çıkış yapabilirsiniz\n\nCevabınız: ")
    if answer == "1":
    
        print("Kolay Modu Seçtiniz!")
        
        temp = False

    elif answer == "2":
    
        print("Orta Modu Seçtiniz!")
        
        temp = False
        
    elif answer == "3":
    
        print("Zor Modu Seçtiniz!")
        
        temp = False
        
    elif answer == "0":
        
        print("Oyun Bitti...\n")
        
        temp = False
        
        quit    
        
    else:
    
        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")