--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

PsiNorm Persentil Hesaplayýcý

Copyright (C) 2017 Bilal Bahadýr Akbulut & Yavuz Ayhan

Bu program tek baþýna taný koymak amacý gütmemektedir. Sadece klinik ve araþtýrma uygulamalarýnda kullanýcýya kolaylýk sunmak için tasarlanmýþtýr. Programýmýz herhangi bir garanti vermemektedir. Tüm sorumluluk kullanýcýya aittir.

Bu program özgür yazýlýmdýr: Özgür Yazýlým Vakfý tarafýndan yayýmlanan GNU Genel Kamu Lisansý’nýn sürüm 3 ya da (isteðinize baðlý olarak) daha sonraki sürümlerinin hükümleri altýnda yeniden daðýtabilir ve/veya deðiþtirebilirsiniz.

Bu program, yararlý olmasý umuduyla daðýtýlmýþ olup, programýn BÝR TEMÝNATI YOKTUR; TÝCARETÝNÝN YAPILABÝLÝRLÝÐÝNE VE ÖZEL BÝR AMAÇ ÝÇÝN UYGUNLUÐUNA dair bir teminat da vermez. Ayrýntýlar için GNU Genel Kamu Lisansý’na göz atýnýz.

Bu programla birlikte GNU Genel Kamu Lisansý’nýn bir kopyasýný elde etmiþ olmanýz gerekir. Eðer elinize ulaþmadýysa <http://www.gnu.org/licenses/> adresine bakýnýz.

Dr. Bilal Bahadýr Akbulut
Ýletiþim adresi: b.bahadirakbulut@gmail.com

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

1. Baþlamadan önce:
 Bu yazýlým Python 3.6.x - 32 bit üzerinden yazýlmýþtýr ve Windows konsolu üzerinden çalýþmaktadýr.
 
 Programýn verileri kaydedebilmesi için programýn yönetici olarak çalýþtýrýlmasý gerekmektedir.

 Programýn çalýþabilmesi için Visual C++ Redistributable Package gerekmektedir, gereken dosyalar 
program ile paketlenmiþ olmak ile beraber, herhangi bir þekilde "VCRuntime140.dll bulunamadý." 
uyarýsý alýnýr ise, þu adresten edinilebilir: 
https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package

 Program çalýþtýrdýrýldýðýnda yazý ve menülerde kayma görülüyor ise, Windows konsol ekraný 
gerektiðinden küçük olabilir. Bunun için pencerenin en üstüne sað týklayarak seçenekler içerisinden
ekran geniþliði ve yüksekliði artýrýlmalýdýr.

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

2. Temel iþleyiþ:
 - Program çalýþtýrýldýðýnda sizden kullanýcý ismini talep edecektir.
 - Bundan sonra hasta demografik bilgilerini talep edip, bu bilgileri daha sonra kullanmak üzere
 geçici belleðinde saklayacaktýr.
 - Bilgileri gözden geçirmeniz için bir fýrsat verilecek ve eðer deðiþtirmek istediðiniz bir 
þey varsa geçici belleði temizleyip, en baþtan programý çalýþtýracaktýr.
 - Eðer girdiðiniz verilerden emin iseniz, program sizi ana menüye taþýyacaktýr.

Ana menü:
"""
|>=============================================|=====================================================<|
| DÝKKAT >>> EÐER ÇIKMADAN ÖNCE 20 GÝRMEZSENÝZ PROGRAM BÝLGÝLERÝ KAYDETMEDEN KAPANACAKTIR. <<< DÝKKAT |
|     DÝKKAT >>>       Programý kapatmak için "exit" yazmanýz gerekmektedir."          <<< DÝKKAT     |
|>=============================================|=====================================================<|    
|                                              |                                                      | 
|>=============================================|=====================================================<|
|A. Genel Biliþsel Tarama Testleri:            |B. Dikkat Testleri:                                   |
|(1)Mini Mental Test                    (-)    |(4)Görsel Ýþitsel Sayý Dizileri                (-)    |
|(2)Montreal Biliþsel Deðerlendirme     (-)    |(14)Wechsler Zeka Testi-Sadece Sayý Dizisi     (-)    |
|(3)3MS                                 (-)    |(19)Aylarý Ýleri-Geri Sayma                    (-)    |
|                                              |                                                      |
|>=============================================|=====================================================<|
|C. Bellek Testleri:                           |D.Yönetici Ýþlev Testleri:                            |
|(5)Artýrýlmýþ Ýpuçlu Hatýrlama         (-)    |(8)Ýz Sürme                                    (-)    |
|(6)Sözel Bellek Süreçleri              (-)    |(9)Stroop                                      (-)    |
|(7)Rey Karmaþýk Figür                  (-)    |(10)Yetiþkin Wisconsin Kart Eþleme             (-)    |
|                                              |(11)Görsel Sözel Test                          (-)    |
|                                              |(12)Renkli Ýz Sürme                            (-)    |
|>=============================================|=====================================================<|
|E.Lisan Testleri:                             |F.Görsel-Uzaysal Ýþlev Testleri:                      |
|(15)Sözel Akýcýlýk                     (-)    |(7)Rey Karmaþýk Figür                          (-)    |
|(16)Semantik Akýcýlýk                  (-)    |(17)Saat Çizme                                 (-)    |
|                                              |(18)Çizgi Yönünü Belirleme                     (-)    |
|>=============================================|=====================================================<|
|G.WAIS:                                       |                                                      |
|(13)Wechsler Zeka Testi                (-)    |                                                      |
|>=============================================|=====================================================<|
| Not: Girilmemiþ testlerin yanýnda "(-)", girilmiþ testlerin yanýnda "(+)" iþareti bulunmaktadýr.    |
|      Eðer bir test iki defa girilmiþ ise, yanýnda "(!+!)" iþareti bulunmaktadýr.                    |
|>=============================================|=====================================================<|
|                                              |                                                      |
|>=============================================|=====================================================<|
| DÝKKAT >>> EÐER ÇIKMADAN ÖNCE 20 GÝRMEZSENÝZ PROGRAM BÝLGÝLERÝ KAYDETMEDEN KAPANACAKTIR. <<< DÝKKAT |
|     DÝKKAT >>>       Programý kapatmak için "exit" yazmanýz gerekmektedir."          <<< DÝKKAT     |
|>=============================================|=====================================================<|


Girmek istediðiniz testin numarasýný giriniz. Kaydetmek için (20) giriniz:

LÜTFEN DÝKKAT: Test içerisinde uygulamadýðýnýz veya olmayan deðerleri 999 olarak giriniz.

"""

- Burada örnek test olarak olmasý açýsýndan, 15 girer isek, bize "Sözel Akýcýlýk" testinin puanlamasýný soracaktýr.

"""
===================================
Sözel akýcýlýk: 



'S' harfi için: 2


'A' harfi için: 3


'Z' harfi için: 999

"""

- Örnek olmasý açýsýndan "Z harfi" basamaðýnýn yapýlamadýðý varsayýlarak "999" girilir ise, program bize þu þekilde bir çýktý verecektir:

"""
===================================
Sözel akýcýlýk testinin sonuçlarý: 
'S' harfi için: Hastanýn puaný: 2.0, Hafif derecede bozulma. Z skoru: -1.94. 2-3 persentil
'A' harfi için: Hastanýn puaný: 3.0, Normal. Z skoru: -0.98. 16-17 persentil
'Z' harfi için: Bu basamak uygulanmamýþ veya uygulanamamýþtýr.
===================================
"""

- Program bu verileri hem ekrana çýktý vermiþ hem de arka planda daha sonra veritabaný ve rapora kayýt için geçici belleðine almýþtýr.
- Girmek istediðimiz tüm testleri girdi isek, "20" yazarak, bu hastaya ait bilgileri kaydetip rapor ve veritabanýna aktarabiliriz.

"""
Girmek istediðiniz testin numarasýný giriniz. Kaydetmek için (20) giriniz: 20

Þu ana kadar yapýlanlar kaydedildi.
Program baþtan baþlatýlýyor.
"""

- Bu geribildirimi aldý isek, program verileri kaydetmiþ demektir. Yeni hastalara geçilebilir.
- Az önce girdiðimiz hasta (seçeneklerde belirttiðimize göre) Microsoft Excel veya CSV formatýndaki veritabanýna aktarýlmýþtýr.
Ayný zamanda, txt formatýnda bir rapor oluþturulmuþtur.
- Bu aþamada eðer raporu görmek istiyor isek, daha önceden belirlenmiþ veri klasöründe sonuçlarý bulabiliriz.
Rapor ismi girdiðimiz veriler ve tarih üzerinden hazýrlanmaktadýr. Yani, az sonra göreceðiniz raporun
dosya ismi, "Deneme-1-(2017-06-06)-Bilal Bahadýr Akbulut.txt" olacaktýr.
- Rapor örneði:
"""
Testi uygulayan: Bilal Bahadýr Akbulut
Günün tarihi: 2017-06-06
Saat: 12:07:36
Hastanýn ismi: Deneme Hastasý
Hastanýn kodu: Deneme-1
Hastanýn yaþý: 65
Hastanýn cinsiyeti: Erkek
Hastanýn toplam eðitim yýlý: 5
=============================================


===================================
Sözel akýcýlýk testinin sonuçlarý: 
'S' harfi için: Hastanýn puaný: 2.0, Hafif derecede bozulma. Z skoru: -1.94. 2-3 persentil
'A' harfi için: Hastanýn puaný: 3.0, Normal. Z skoru: -0.98. 16-17 persentil
'Z' harfi için: Bu basamak uygulanmamýþ veya uygulanamamýþtýr.
===================================


===================================================================                
ÖNEMLÝ UYARILAR:
    
1) Bir takým hasta gruplarý için norm deðerleri bulunmadýðýnda, en yakýn gruba göre hesaplanmýþtýr.
Limitleri olan testler aþaðýdaki þekildedir:

 > Görsel Ýþitsel Sayý Dizileri: 13 <= Yaþ

 > Sözel Bellek Süreçleri: 15 <= Yaþ VEYA Eðitim <= 19

 > Rey Karmaþýk Figür: 17 <= Yaþ <= 82

 > Ýz sürme: 50 <= Yaþ

 > Stroop: 5 <= Eðitim <= 8 VE 20 <= Yaþ <=74
           8 <= Eðitim VE 20 <= Yaþ <= 82

 > Yetiþkin Wisconsin Kart Eþleme: 5 <= Eðitim VE 20 <= Yaþ <= 72
                                   12 <= Eðitim VE 20 <= Yaþ <= 78

 > Görsel Sözel test: 20 <= Yaþ <= 100
 
 > Renkli Ýz Sürme: 20 <= Yaþ <= 100
 
 > Sözel Akýcýlýk: 5 <= Eðitim VEYA 15 <= Yaþ
 
 > Semantik Akýcýlýk: 5 <= Eðitim VEYA 15 <= Yaþ
 
 > Çizgi Yönünü Belirleme: 5 <= Eðitim <= 8 VE 20 <= Yaþ <= 74
                           9 <= Eðitim <= 11 VE 20 <= Yaþ <= 76
                           12 <= Eðitim VE 20 <= Yaþ <= 73

2) Testlerin sonuçlarýnda bildirilen sözlü yorumlar, normalin 1 standart deviasyon(SD) uzaðý
normal, 1-2 SD aralýðý hafif bozulma, 2-3 SD aralýðý orta derecede bozulma, 3 SD'den uzakta olan
sonuçlar aðýr derecede bozulma olarak yorumlanmýþtýr.

===================================================================
Kaynakça:
********************************

===================================================================
"""

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

3. Seçenekler
Program bir veri çýktýsýyla ilgili olarak bir takým seçenekler sunmaktadýr. Bu seçenekler programýn yüklendiði klasör içerisinde "settings" adlý dosya
üzerinden düzenlenebilir.

Program ile beraber paketlenen konfigürasyon dosyasýndaki seçenekler þu þekildedir:
excel_name = benimdosyam.xlsx
Programýn Excel çýktýsýnýn ismini düzenler. Yukarýda belirtilen formatta olacak þekilde herhangi bir þey olabilir. Türkçe karakter kullanýlmamasý tavsiye edilir.
 "-" ve "_" dýþýnda özel karakter kullanýlmamasý tavsiye edilir.
excel_output_subjectNames = True
Excel dosyasýna denek isimlerinin çýktýsý yapýlýp yapýlmama durumunun bildirir.
Güvenlik kaygýlarý açýsýndan eklenmiþtir.

auto_run = True/False
Programýn her seferinde otomatik baþtan baþlama sistemini kapatýr.
Her iþlem bitiminde kendiliðinden program kapanacaktýr.

output_csv = True/False ('True' ise csv dosyalarý oluþturulur, 'False' ise oluþturulmaz.)
output_txt = True/False ('True' ise txt dosyasý oluþturulur, 'False' ise oluþturulmaz.)
output_excel = True/False ('True' ise excel dosyasý oluþturulur, 'False' ise oluþturulmaz.)

csv_path = "csv dosyalarýnýn kaydedileceði adres" 
txt_path = "txt dosyalarýnýn kaydedileceði adres"
excel_path = "excel dosyalarýnýn kaydedileceði adres"
Default olmasý halinde bilgisayar çýktýlarý programýn bulunduðu klasörün içinde
"Results" isimli bir klasör oluþturarak oraya yerleþtirir. 

Eðer çýktý klasörünü deðiþtirmek isterseniz adresin yazýlma formatý þu þekilde olmalýdýr:
csv_path = C:/Users/BenimBilgisayarým/Desktop/data/csv/
txt_path = C:/Users/BenimBilgisayarým/Desktop/raporlar/
veya
csv_path = C:/csv_depo/
txt_path = C:/Users/BenimBilgisayarým/Desktop/
gibi.

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------
4. Yazarlar:
Dr. Bilal Bahadýr Akbulut – Kodlama & Tasarým
Doç. Dr. Yavuz Ayhan – Proje Danýþmaný
--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------
5. Bilgilendirme ve Referanslar
Program yazýlýrken kullanýlan Python 3.6.x, ilgili kütüphaneleri ve program kaynak kodundan çalýþtýrýlabilir hale 
getirilirken kullanýlan cx_freeze Python modülü açýk kaynaklý yazýlýmlardýr.

Program içinde kullanýlan nöropsikiyatrik testlerin Türk toplumuna uyarlanma çalýþmalarý þu gruplar tarafýndan yapýlmýþtýr:
>Cangoz, B., Karakoc, E., & Selekler, K. (2009). Trail Making Test: normative data for Turkish elderly population by age, sex and education. J Neurol Sci, 283(1-2), 73-78. doi: 10.1016/j.jns.2009.02.313

>Cangöz B, K. E., Selekler K (2006 ). Saat Çizme Testi’nin Türk yetiþkin ve yaþlý örneklemi üzerindeki norm belirleme, geçerlik ve güvenirlik çalýþmalarý. . Türk Geriatri Dergisi,, 9 (3), 136-142. 

>Karakaþ, S., Erdoðan Bakar, E., Doðutepe Dinçer, E. (2013). BÝLNOT Bataryasý El Kitabý: Nöropsikolojik Testlerin Yetiþkinler için Araþtýrma ve Geliþtirme Çalýþmalarý: BÝLNOT- Yetiþkin (Cilt I-II) 

>Keskinoglu, P., Ucku, R., Yener, G., Yaka, E., Kurt, P., & Tunca, Z. (2009). Reliability and validity of revised Turkish version of Mini Mental State Examination (rMMSE-T) in community-dwelling educated and uneducated elderly. Int J Geriatr Psychiatry, 24(11), 1242-1250. doi: 10.1002/gps.2252

>Kudiaki, C., & Aslan, A. (2008). Executive functions in a Turkish sample: associations with demographic variables and normative data. Appl Neuropsychol, 15(3), 194-204. doi: 10.1080/09084280802324416

>Saka, E., Mihci, E., Topcuoglu, M. A., & Balkan, S. (2006). Enhanced cued recall has a high utility as a screening test in the diagnosis of Alzheimer's disease and mild cognitive impairment in Turkish people. Arch Clin Neuropsychol, 21(7), 745-751. doi: 10.1016/j.acn.2006.08.007

>Selekler, K. C., B, Uluç, S. . (2010). Montreal Biliþsel Deðerlendirme Ölçeði'nin (MOBÝD) Hafif Biliþsel Bozukluk ve Alzheimer Hastalarýný ayýrdedebilme gücünün incelenmesi. Türk Geriatri Dergisi,, 13(3), 166-171. 

>Tanor, O. (2006). Öktem Sözel Bellek Süreçleri Testi. Ankara: Türk Psikologlar Derneði.

>Teng, E. L., & Chui, H. C. (1987). The Modified Mini-Mental State (3MS) examination. J Clin Psychiatry, 48(8), 314-318. 

>Varan E, Tanor O, Gurvit H (2007) Rey Karmaþýk Figür Testi ve Tanýma Uygulamasý (RKFT-T): Bir Yetiþkin Türk Örneklemi Üzerinde Norm Belirleme Çalýþmasý.  Turk J Neurol. 2007; 13(6): 387-394
