#Vucüt Kitle Endeksi
#VKE = vucüt ağırlığı(kg)/boyun karesi(metre)
print("Vucüt kitle endeksi hesapla")
print("***************************\n")

boy = int(input("Lutfen boyunuzu giriniz(cm)."))
kilo = int(input("Lutfen kilonuzu giriniz(kg)."))

boy2 = boy/100 #Boy cm olarak girilmişti. Onu metreye çeviriyoruz.
vke = kilo/(boy2*boy2)
print("\nSizin vucüt kütle endeksiniz", vke)
if vke<18.49:
    print("Zayıfsın, kilo almalısın.")
elif vke>18.49 and vke<24.99:
    print("Gayet iyi durumdasın.")
else:
    print("Kilolusun, diyet yapmalısın.")
          
