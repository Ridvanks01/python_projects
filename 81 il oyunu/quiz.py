import random

pattern = "-------------------------------------------------"

answers = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

trues = 0
falses = 0

print( pattern + "\n       81 İL BİLGİ YARIŞMASINA HOŞGELDİNİZ!\n" + pattern)


while True:
       
    diff = input("\nZorluk Seviyesini Seçiniz\n\n1.Kolay (10 soru - 2 şık)\n2.Orta  (15 soru - 3 şık)\n3.Zor   (20 soru - 4 şık)\n0.Çıkış\n\nNot: Bütün sorularda 0 a basarak çıkış yapabilirsiniz\n\nCevabınız: ")
    
    if diff == "1":
    
        print("Kolay Modu Seçtiniz!\n")
        
        for i in range(10):
            
            randomNumber = random.randint(1,81)
            
            option1 = answers[random.randint(0,80)]
            option2 = answers[randomNumber-1]
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
            
                answer = input("A." + option1 + "\n" + "B." + option2 + "\n\nCevabınız: ")
            
                if answer == "A" or answer == "a":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
                
                elif answer == "B" or answer == "b":
                    print("\n" + "Doğru Cevap!")
                    
                    trues = trues + 1
                    
                    break
                
                elif answer == "0":
                
                    print("Oyun Bitti...\n")
        
                    quit
                    break
                
                else:
                    print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")     
         
        print("\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses))
                   
        break
                

    elif diff == "2":
    
        print("Orta Modu Seçtiniz!\n")
        
        for i in range(15):
            
            randomNumber = random.randint(1,81)
            
            option1 = answers[random.randint(0,80)]
            option2 = answers[random.randint(0,80)]
            option3 = answers[randomNumber-1]
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
            
                answer = input("A." + option1 + "\n" + "B." + option2 + "\n" + "C." + option3 + "\n\nCevabınız: ")
            
                if answer == "A" or answer == "a":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
                
                elif answer == "B" or answer == "b":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
                
                elif answer == "C" or answer == "c":
                    print("\n" + "Doğru Cevap!")
                    
                    trues = trues + 1
                    
                    break
                
                elif answer == "0":
                
                    print("Oyun Bitti...\n")
        
                    quit
                    break
                
                else:
                    print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")
                     
        print("\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses))
              
        break
  
  
    elif diff == "3":
    
        print("Zor Modu Seçtiniz!\n")
           
        for i in range(20):
            
            randomNumber = random.randint(1,81)
            
            option1 = answers[random.randint(0,80)]
            option2 = answers[random.randint(0,80)]
            option3 = answers[random.randint(0,80)]
            option4 = answers[randomNumber-1]
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
            
                answer = input("A." + option1 + "\n" + "B." + option2 + "\n" + "C." + option3 + "\n" + "D." + option4 + "\n\nCevabınız: ")
            
                if answer == "A" or answer == "a":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
                
                elif answer == "B" or answer == "b":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
                
                elif answer == "C" or answer == "c":
                    print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + answers[randomNumber - 1])
                    
                    falses = falses + 1
                    
                    break
            
                elif answer == "D" or answer == "d":
                    print("\n" + "Doğru Cevap!")
                    
                    trues = trues + 1
                    
                    break
                
                elif answer == "0":
                
                    print("Oyun Bitti...\n")
                
                    quit    
                
                    break
                
                else:
                    print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")    
            
        print("\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses))
                
        break
        
        
    elif diff == "0":
        
        print("Oyun Bitti...\n")
        
        quit    
        
        break
        
        
    else:
    
        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")