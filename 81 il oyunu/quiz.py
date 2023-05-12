import random

pattern = "-------------------------------------------------"

cities = ["Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"]

trues = 0
falses = 0

print( pattern + "\n       81 İL BİLGİ YARIŞMASINA HOŞGELDİNİZ!\n" + pattern)


while True:
       
    diff = input("\nZorluk Seviyesini Seçiniz\n\n1.Kolay (10 soru - 2 şık)\n2.Orta  (15 soru - 3 şık)\n3.Zor   (20 soru - 4 şık)\n0.Çıkış\n\nNot: Bütün sorularda 0 a basarak çıkış yapabilirsiniz\n\nCevabınız: ")
    
    if diff == "1":
    
        print("Kolay Modu Seçtiniz!\n")
        
        for i in range(10):
            
            randomNumber = random.randint(1,81)
            
            option1 = cities[randomNumber-1]
            option2 = cities[random.randint(0,80)]
            
            while option1 == option2:
                
                option2 = cities[random.randint(0,80)]
                
                if option1 != option2:
                    
                    break
                        
            
            optionOrder = random.randint(1,2)            
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
            
                if optionOrder == 1:
                    
                    answer = input("A." + option1 + "\n" + "B." + option2 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")   
                    
                else:
                    
                    answer = input("A." + option2 + "\n" + "B." + option1 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
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
         
        print(pattern + "\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses) + "\n" + pattern)
                   
        break
                

    elif diff == "2":
    
        print("Orta Modu Seçtiniz!\n")
        
        for i in range(15):
            
            randomNumber = random.randint(1,81)
            
            option1 = cities[randomNumber-1]
            option2 = cities[random.randint(0,80)]
            option3 = cities[random.randint(0,80)]
            
            while option1 == option2 or option1 == option3 or option2 == option3:
                
                option2 = cities[random.randint(0,80)]
                option3 = cities[random.randint(0,80)]
                
                if option1 != option2 and option1 != option3 and option2 != option3:
                    
                    break
            
            optionOrder = random.randint(1,3) 
            
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
                
                if optionOrder == 1:
                    
                    answer = input("A." + option1 + "\n" + "B." + option2 + "\n" + "C." + option3 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")   
                    
                    
                elif optionOrder == 2:
                    
                    answer = input("A." + option2 + "\n" + "B." + option1 + "\n" + "C." + option3 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")
                
                
                else:
                    
                    answer = input("A." + option2 + "\n" + "B." + option3 + "\n" + "C." + option1 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
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
                        
                     
        print(pattern + "\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses) + "\n" + pattern)
              
        break
  
  
    elif diff == "3":
    
        print("Zor Modu Seçtiniz!\n")
           
        for i in range(20):
            
            randomNumber = random.randint(1,81)
            
            option1 = cities[randomNumber-1]
            option2 = cities[random.randint(0,80)]
            option3 = cities[random.randint(0,80)]
            option4 = cities[random.randint(0,80)]
            
            while option1 == option2 or option1 == option3 or option1 == option4 or option2 == option3 or option2 == option4 or option3 == option4:
                
                option2 = cities[random.randint(0,80)]
                option3 = cities[random.randint(0,80)]
                option4 = cities[random.randint(0,80)]
                
                if option1 != option2 and option1 != option3 and option1 != option4 and option2 != option3 and option2 != option4 and option3 != option4:
                    
                    break
            
            optionOrder = random.randint(1,4)
            
            while True:
                
                print(pattern + "\n\n" + str(i + 1) + ".Soru: " + str(randomNumber) + " Plaka kodlu ilimiz aşağıdakilerden hangisidir?\n")
            
                if optionOrder == 1:
                    
                    answer = input("A." + option1 + "\n" + "B." + option2 + "\n" + "C." + option3 + "\n" + "D." + option4 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                    
                    elif answer == "D" or answer == "d":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")   
                    
                    
                elif optionOrder == 2:
                    
                    answer = input("A." + option2 + "\n" + "B." + option1 + "\n" + "C." + option3 + "\n" + "D." + option4 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "D" or answer == "d":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                        
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")
                        
                
                elif optionOrder == 3:
                    
                    answer = input("A." + option2 + "\n" + "B." + option3 + "\n" + "C." + option1 + "\n" + "D." + option4 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Doğru Cevap!")
                    
                        trues = trues + 1
                    
                        break
                
                    elif answer == "D" or answer == "d":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                        
                    elif answer == "0":
                
                        print("Oyun Bitti...\n")
        
                        quit
                        break
                    
                    else:
                        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")
                
                
                else:
                    
                    answer = input("A." + option2 + "\n" + "B." + option3 + "\n" + "C." + option4 + "\n" + "D." + option1 + "\n\nCevabınız: ")
                    
                    if answer == "A" or answer == "a":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                
                    elif answer == "B" or answer == "b":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
                        falses = falses + 1
                    
                        break
                    
                    elif answer == "C" or answer == "c":
                        
                        print("\n" + "Yanlış Cevap! " + str(randomNumber) + " plaka kodlu ilimiz " + cities[randomNumber - 1])
                    
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
                        
            
        print(pattern + "\nDoğru Sayısı: " + str(trues))
        print("Yanlış Sayısı: " + str(falses) + "\n" + pattern)
                
        break
        
        
    elif diff == "0":
        
        print("Oyun Bitti...\n")
        
        quit    
        
        break
        
        
    else:
    
        print(pattern + "\n*Lütfen Geçerli Bir Cevap Giriniz!*")