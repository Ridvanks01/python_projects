pattern = "--------------------------------------------------"

print( pattern + "\n  TC KİMLİK NO DOĞRULAMA PROGRAMINA HOŞGELDİNİZ!\n" + pattern)

while True:
    
    tc = str(input("\nTC Kimlik Numaranızı Giriniz: \nCevabınız: "))
    
    if len(tc)>11 or len(tc)<11 or tc.startswith("0"):
        
        if tc.startswith("0"):
            print(pattern + "\nTC Kimlik Numarası \"0\" İle Başlayamaz!")
            
        elif len(tc)>11:
            print(pattern + "\nTC Kimlik Numarası \"11\" Haneden Büyük Olamaz!")
            
        else:
            print(pattern + "\nTC Kimlik Numarası \"11\" Haneden Küçük Olamaz!")
        
    else:
        
        firstSumFor10 = int(tc[0]) + int(tc[2]) + int(tc[4]) + int(tc[6]) + int(tc[8])
        secondSumFor10 = int(tc[1]) + int(tc[3]) + int(tc[5]) + int(tc[7])
        thirtSumFor11 = 0
        
        for i in range(0,10):
            thirtSumFor11 = thirtSumFor11 + int(tc[i])
        
        calculationFor10 = ((firstSumFor10 * 7) - secondSumFor10) % 10
        calculationFor11 = thirtSumFor11 % 10
        
        if calculationFor10 == int(tc[9]) and calculationFor11 == int(tc[10]):
            
            print("Girilen TC Kimlik Numarası Geçerlidir!")
            
            break
        
        else:
            print("Girilen TC Kimlik Numarası Geçersizdir!")
            
            break