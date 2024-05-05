# Bu benim notlarım
metin = 'Bugün ÇOMÜ Makine öğrenmesi dersinin ilk günü...'
sonuc = 968*256
print(metin)
print(sonuc)
# Değişken tipleri
# int : tam sayıların tutulduğu veri tipidir.
sayi = 10
print(type(sayi))
print(sayi)

# str : metinsel ifadelerin tutulduğu veri tipidir.
a = '123456'
print(type(a))
print(a)

# float : ondalıklı sayıların tutulduğu veri tipidir.
ondalik = 12.56
print(type(ondalik))
print(ondalik)

# bool : Doğruluk değeri taşıyan veri tipidir. sadece 2 değer alır (True, False)
dogru = True
yanlis = False
print(type(dogru))
print(type(yanlis))
print(dogru)
print(yanlis)

# list : Dizi veya liteleri temsil eden veri tipidir. Çeşitli veri tiplerini içerebilir.
meyveler = ['Elma','Armut','Kiraz','Kayısı','Üzüm']
liste = ['Elma','Armut','Kiraz','Kayısı','Üzüm', 1 , 2 , 3 , 4 , True , True , False, False]

print(type(meyveler))
print(meyveler)

print(type(liste))
print(liste)
# set : Bir listede benzersiz elemanların olmasını istiyorsak set kullanmamız gerekir.
unique_numbers = {1,1,2,2,3,3,4,4,5,5}
print(type(unique_numbers))
print(unique_numbers)
# tuple : Değiştirilemez sıralı veri tipidir.
colors = ('Red', 'Yellow', 'Black', 'White')
print(type(colors))
print(colors)

# dict (sözlük): anahtar - değer çiftlerini temsil eden veri tipidir.
# kisiler sözlüğünde ilk anahtar verisi kişinin adı , değer verisi ise yaşını temsil etmektedir.
kisiler = {'Ahmet': 25, 'Gamze': 23, 'Veli': 24}
print(type(kisiler))
print(kisiler)

# Bu benim notlarım
metin = 'Bugün ÇOMÜ Makine öğrenmesi dersinin ilk günü...'
sonuc = 968*256
print(metin)
print(sonuc)
# Değişken tipleri
# int : tam sayıların tutulduğu veri tipidir.
sayi = 10
print(type(sayi))
print(sayi)

# str : metinsel ifadelerin tutulduğu veri tipidir.
a = '123456'
print(type(a))
print(a)

# float : ondalıklı sayıların tutulduğu veri tipidir.
ondalik = 12.56
print(type(ondalik))
print(ondalik)

# bool : Doğruluk değeri taşıyan veri tipidir. sadece 2 değer alır (True, False)
dogru = True
yanlis = False
print(type(dogru))
print(type(yanlis))
print(dogru)
print(yanlis)

# list : Dizi veya liteleri temsil eden veri tipidir. Çeşitli veri tiplerini içerebilir.
meyveler = ['Elma','Armut','Kiraz','Kayısı','Üzüm']
liste = ['Elma','Armut','Kiraz','Kayısı','Üzüm', 1 , 2 , 3 , 4 , True , True , False, False]

print(type(meyveler))
print(meyveler)

print(type(liste))
print(liste)
# set : Bir listede benzersiz elemanların olmasını istiyorsak set kullanmamız gerekir.
unique_numbers = {1,1,2,2,3,3,4,4,5,5}
print(type(unique_numbers))
print(unique_numbers)
# tuple : Değiştirilemez sıralı veri tipidir.
colors = ('Red', 'Yellow', 'Black', 'White')
print(type(colors))
print(colors)

# dict (sözlük): anahtar - değer çiftlerini temsil eden veri tipidir.
# kisiler sözlüğünde ilk anahtar verisi kişinin adı , değer verisi ise yaşını temsil etmektedir.
kisiler = {'Ahmet': 25, 'Gamze': 23, 'Veli': 24}
print(type(kisiler))
print(kisiler)

# str veri tipi  ile alakalı işe yarayacak fonksiyonlar.
yazi = 'Bu dersimizde string ile alakjalı örnekler yapacağız.'
# len : verilen metinsel ifadenin kaç karakterli olduğunu gösterir

kac_karakterli = len(yazi)
print('verilen metin ', kac_karakterli, ' karakterlidir.')

# lower : verilen metindeki tüm karakterleri küçük harfe çevirir
m1 = 'MERHABALAR BEN ÖMER'
lower_text = m1.lower()
print(lower_text)

# upper : verilen metindeki tüm karakterleri büyük harfe çevirir.
m2 = 'merhabalar'
upper_text = m2.upper()
print(upper_text)

# capitalize : Verilen metindeki ilk harfi büyük yazar.
m3 = 'selamlar'
capitalize_text = m3.capitalize()
print(capitalize_text)

#count : metinde verilen ve içinde kaç tane ilgili metnin geçtiğini bulan fonksiyondur.
m4 = 'Benim bildiğim programlama dilleri Java, Python , Javascript, Python , Python'
print('Yukarıda verilen metinde kaç adet Python kelimesi geçmiştir : ', m4.count('Python'))
# replace : verilen metinde değişmesini istediğimiz durumlar
print(yazi.replace('alakjalı','alakalı'))

# startswith : verilen metinde istenilen şekilde başlıyor mu sorusunu sorar.
m5 = 'Python Çok güzel bir dildir.'
print('m5 değişkenindei metin Py ile başlıyor mu : ', m5.startswith('Py'))
# endswith : verilen metinde istenilen şekilde bitiyor mu sorusunu sorar
print('m5 değişkeninde ki metin Py ile bitiyor mu : ',m5.endswith('Py'))
print('m5 değişkeninde ki metin dir. ile bitiyor mu : ',m5.endswith('dir.'))

#strip : Stringin  başındaki ve sonundaki boşukları temizler
m6 = '                              Selam                                             '
print(m6)
print(m6.strip())

# find : Belirtilen kelimeyi bulur ve ilk indexini gösterir
m7 = 'Bugün hava çok güzeldi bende dışarıya çıktım.'
print(m7.find('çok'))

# join : bir liste veya tuple içindeki elemanları belirli kurala göre birleştirir.
kelimeler = ['Benim en sevdiğim diller', 'Python', 'Java', 'c#', 'JavaScript']
joined_text = ' -'.join(kelimeler)
print(joined_text)

# format : metinsel ifadelerin içerisinde bazen değişkenlerin değerini eklemek gerekebilir bunun için format yöntemi kullanuılır.

ad = 'Furkan'
soyad = 'Oğuz'
yas = 35
# 1. Yöntem
formatted_text = 'Benim adım {}  Soyadım {} yaşım {} '.format(ad,soyad,yas)
print(formatted_text)

# 2. Yöntem
formatted_text1 = f'Benim adım {ad} Soyadım {soyad} yaşım {yas}'
print(formatted_text1)

# kullanıcıdan isim , soyisim ve yaşı aldıktan sonra ekran çıktısı olarak verilen metni büyük harfle yazdırınız.

#name = input('Lütfen adınızı giriniz : ')
#surname = input('Lütfen soyadınızı giriniz :')
#age = input('Lütfen yaşınızı giriniz :')
#text = f'Adınız : {name.upper()}, Soyadınız : {surname.upper()}, Yaşınız : {age}'
#print(text)

# Aritmetik operatörler
# Toplama operatörü : +

sayi1 = 10
sayi2 = 10.54

metin1 = 'Bugün ders konumuz '
metin2 = 'Operatörler'

toplam = sayi1 + sayi2
print(toplam)

metin3 = metin1 + metin2
print(metin3)

# çarpma operatörü : *
carpim = sayi1 * sayi2
print(carpim)

metin4 = metin1 * 2
print(metin4)

# bölme operatörü : /
bolme = sayi1 / sayi2
print(bolme)

# çıkarma operatörü : -
cikarma = sayi1 - sayi2
print(cikarma)

# kulanıcıdan 2 tane sayı aldıktan sonra 4 işlem sonucunu ekrana çıktı olarak veriniz.

#number1 = int(input('Lütfen 1. sayıyı giriniz : '))
#number2 = int(input('Lütfen 2. sayıyı giriniz : '))

#sum = number1 + number2
#divide = number1 / number2
#difference = number1 - number2
#multiply = number1 * number2

#print(f'{number1} + {number2} = {sum}')
#print(f'{number1} / {number2} = {divide}')
#print(f'{number1} - {number2} = {difference}')
#print(f'{number1} * {number2} = {multiply}')

# Karşılaştırma operatörleri
# <(KÜÇÜKTÜR) , >(BÜYÜKTÜR) , <= (KÜÇÜK EŞİTTİR), >=(BÜYÜK EŞİTTİR) , ==(EŞİT MİDİR) , !=(EŞİT DEĞİL MİDİR)

x = 3 < 6  #True
y = 4 > 6 # False
z = 3 == 3 #True
t = 3 != 5 #True
a = 3 >= 3 # True
b = 2 != 2 #False
c = 1 <= 15 #True
d = -25 == 25 #False
print(x, y, z, t, a, b, c, d)

# Mantıksal operatörler ve , veya
# ve : her iki koşul sağlandığında True döner (and)
# veya : her iki koşuldan sadece birinin doğru olması durumunda True döner.

case1 = 3 < 5 and 5 == 5
case2 =  4==5 and 6!=7

case3 = 5==1 or 5>=-13
case4 = 6!=7 or 8<9

print(case1, case2, case3, case4)

# if else blokları
# Kullanıcıdan yaşını aldıktan sonra eğer 18 yaşından küçük ise ehliyet alamazsınız yazısı aksi takdirde ehliyet alabilirsiniz yazısı ekrana veriniz.

age = int(input('Lütfen yaşınızı giriniz :'))

if age >= 18:
    print('Ehliyet alabilirsiniz 18 yaşından büyük veya eşitsiniz')
else:
    print('Ehliyet alamazsınız reşit değilsiniz.')