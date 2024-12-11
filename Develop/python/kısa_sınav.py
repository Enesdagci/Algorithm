""" --- 27. Soru --- """
"""def asal(num):
    if num < 2:
        return False
    for number in range(2,int(num ** 0.5)+1):
        if num % number == 0:
            return False
    return True

def aralik(num_1,num_2):
    asal_sayilar= []
    for sayi in range(num_1,num_2+1):
        if asal(sayi):
            asal_sayilar.append(sayi)
    return asal_sayilar

sayi_1 = int(input("Birinci Sayı: "))
sayi_2 = int(input("İkinci Sayı: "))

asal_sayilar = aralik(sayi_1,sayi_2)

print("Asal Sayılar: ", asal_sayilar)
"""

""" Örnek 1:
Birbirinden farklı olarak verilen iki adet sayıdan, büyük olanı bulup gösteren algoritma ve akış diyagramını tasarlayınız.
"""
#sayi_1 = int(input("Birinci sayı: "))
#sayi_2 = int(input("İkinci sayı: "))

#if sayi_1 < sayi_2:
#    print(f"En büyük sayı {sayi_2}")
#else:
#    print(f"En büyük sayı {sayi_1}")
    
#vize_not = int(input("Vize notunu giriniz.: "))
#final_not = int(input("Final notunu giriniz.: "))

#ortalama = vize_not * 0.4 + final_not * 0.8
#print("Ortalamanınz: ",ortalama)

#sayi = int(input("Sayıyı giriniz.: "))
#if sayi == 0:
#    print("Sayı 0'a eşittir.")
#elif sayi < 0:
#    print("Sayı negatif bir sayı.")
#elif sayi > 0:
#    print("Sayı pozitif bir sayı.")

for sayac in range(10):
    print("Enes")
