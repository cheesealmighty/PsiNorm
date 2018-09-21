--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

PsiNorm Persentil Hesaplay�c�

Copyright (C) 2017 Bilal Bahad�r Akbulut & Yavuz Ayhan

Bu program tek ba��na tan� koymak amac� g�tmemektedir. Sadece klinik ve ara�t�rma uygulamalar�nda kullan�c�ya kolayl�k sunmak i�in tasarlanm��t�r. Program�m�z herhangi bir garanti vermemektedir. T�m sorumluluk kullan�c�ya aittir.

Bu program �zg�r yaz�l�md�r: �zg�r Yaz�l�m Vakf� taraf�ndan yay�mlanan GNU Genel Kamu Lisans��n�n s�r�m 3 ya da (iste�inize ba�l� olarak) daha sonraki s�r�mlerinin h�k�mleri alt�nda yeniden da��tabilir ve/veya de�i�tirebilirsiniz.

Bu program, yararl� olmas� umuduyla da��t�lm�� olup, program�n B�R TEM�NATI YOKTUR; T�CARET�N�N YAPILAB�L�RL���NE VE �ZEL B�R AMA� ���N UYGUNLU�UNA dair bir teminat da vermez. Ayr�nt�lar i�in GNU Genel Kamu Lisans��na g�z at�n�z.

Bu programla birlikte GNU Genel Kamu Lisans��n�n bir kopyas�n� elde etmi� olman�z gerekir. E�er elinize ula�mad�ysa <http://www.gnu.org/licenses/> adresine bak�n�z.

Dr. Bilal Bahad�r Akbulut
�leti�im adresi: b.bahadirakbulut@gmail.com

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

1. Ba�lamadan �nce:
 Bu yaz�l�m Python 3.6.x - 32 bit �zerinden yaz�lm��t�r ve Windows konsolu �zerinden �al��maktad�r.
 
 Program�n verileri kaydedebilmesi i�in program�n y�netici olarak �al��t�r�lmas� gerekmektedir.

 Program�n �al��abilmesi i�in Visual C++ Redistributable Package gerekmektedir, gereken dosyalar 
program ile paketlenmi� olmak ile beraber, herhangi bir �ekilde "VCRuntime140.dll bulunamad�." 
uyar�s� al�n�r ise, �u adresten edinilebilir: 
https://support.microsoft.com/en-us/help/3179560/update-for-visual-c-2013-and-visual-c-redistributable-package

 Program �al��t�rd�r�ld���nda yaz� ve men�lerde kayma g�r�l�yor ise, Windows konsol ekran� 
gerekti�inden k���k olabilir. Bunun i�in pencerenin en �st�ne sa� t�klayarak se�enekler i�erisinden
ekran geni�li�i ve y�ksekli�i art�r�lmal�d�r.

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

2. Temel i�leyi�:
 - Program �al��t�r�ld���nda sizden kullan�c� ismini talep edecektir.
 - Bundan sonra hasta demografik bilgilerini talep edip, bu bilgileri daha sonra kullanmak �zere
 ge�ici belle�inde saklayacakt�r.
 - Bilgileri g�zden ge�irmeniz i�in bir f�rsat verilecek ve e�er de�i�tirmek istedi�iniz bir 
�ey varsa ge�ici belle�i temizleyip, en ba�tan program� �al��t�racakt�r.
 - E�er girdi�iniz verilerden emin iseniz, program sizi ana men�ye ta��yacakt�r.

Ana men�:
"""
|>=============================================|=====================================================<|
| D�KKAT >>> E�ER �IKMADAN �NCE 20 G�RMEZSEN�Z PROGRAM B�LG�LER� KAYDETMEDEN KAPANACAKTIR. <<< D�KKAT |
|     D�KKAT >>>       Program� kapatmak i�in "exit" yazman�z gerekmektedir."          <<< D�KKAT     |
|>=============================================|=====================================================<|    
|                                              |                                                      | 
|>=============================================|=====================================================<|
|A. Genel Bili�sel Tarama Testleri:            |B. Dikkat Testleri:                                   |
|(1)Mini Mental Test                    (-)    |(4)G�rsel ��itsel Say� Dizileri                (-)    |
|(2)Montreal Bili�sel De�erlendirme     (-)    |(14)Wechsler Zeka Testi-Sadece Say� Dizisi     (-)    |
|(3)3MS                                 (-)    |(19)Aylar� �leri-Geri Sayma                    (-)    |
|                                              |                                                      |
|>=============================================|=====================================================<|
|C. Bellek Testleri:                           |D.Y�netici ��lev Testleri:                            |
|(5)Art�r�lm�� �pu�lu Hat�rlama         (-)    |(8)�z S�rme                                    (-)    |
|(6)S�zel Bellek S�re�leri              (-)    |(9)Stroop                                      (-)    |
|(7)Rey Karma��k Fig�r                  (-)    |(10)Yeti�kin Wisconsin Kart E�leme             (-)    |
|                                              |(11)G�rsel S�zel Test                          (-)    |
|                                              |(12)Renkli �z S�rme                            (-)    |
|>=============================================|=====================================================<|
|E.Lisan Testleri:                             |F.G�rsel-Uzaysal ��lev Testleri:                      |
|(15)S�zel Ak�c�l�k                     (-)    |(7)Rey Karma��k Fig�r                          (-)    |
|(16)Semantik Ak�c�l�k                  (-)    |(17)Saat �izme                                 (-)    |
|                                              |(18)�izgi Y�n�n� Belirleme                     (-)    |
|>=============================================|=====================================================<|
|G.WAIS:                                       |                                                      |
|(13)Wechsler Zeka Testi                (-)    |                                                      |
|>=============================================|=====================================================<|
| Not: Girilmemi� testlerin yan�nda "(-)", girilmi� testlerin yan�nda "(+)" i�areti bulunmaktad�r.    |
|      E�er bir test iki defa girilmi� ise, yan�nda "(!+!)" i�areti bulunmaktad�r.                    |
|>=============================================|=====================================================<|
|                                              |                                                      |
|>=============================================|=====================================================<|
| D�KKAT >>> E�ER �IKMADAN �NCE 20 G�RMEZSEN�Z PROGRAM B�LG�LER� KAYDETMEDEN KAPANACAKTIR. <<< D�KKAT |
|     D�KKAT >>>       Program� kapatmak i�in "exit" yazman�z gerekmektedir."          <<< D�KKAT     |
|>=============================================|=====================================================<|


Girmek istedi�iniz testin numaras�n� giriniz. Kaydetmek i�in (20) giriniz:

L�TFEN D�KKAT: Test i�erisinde uygulamad���n�z veya olmayan de�erleri 999 olarak giriniz.

"""

- Burada �rnek test olarak olmas� a��s�ndan, 15 girer isek, bize "S�zel Ak�c�l�k" testinin puanlamas�n� soracakt�r.

"""
===================================
S�zel ak�c�l�k: 



'S' harfi i�in: 2


'A' harfi i�in: 3


'Z' harfi i�in: 999

"""

- �rnek olmas� a��s�ndan "Z harfi" basama��n�n yap�lamad��� varsay�larak "999" girilir ise, program bize �u �ekilde bir ��kt� verecektir:

"""
===================================
S�zel ak�c�l�k testinin sonu�lar�: 
'S' harfi i�in: Hastan�n puan�: 2.0, Hafif derecede bozulma. Z skoru: -1.94. 2-3 persentil
'A' harfi i�in: Hastan�n puan�: 3.0, Normal. Z skoru: -0.98. 16-17 persentil
'Z' harfi i�in: Bu basamak uygulanmam�� veya uygulanamam��t�r.
===================================
"""

- Program bu verileri hem ekrana ��kt� vermi� hem de arka planda daha sonra veritaban� ve rapora kay�t i�in ge�ici belle�ine alm��t�r.
- Girmek istedi�imiz t�m testleri girdi isek, "20" yazarak, bu hastaya ait bilgileri kaydetip rapor ve veritaban�na aktarabiliriz.

"""
Girmek istedi�iniz testin numaras�n� giriniz. Kaydetmek i�in (20) giriniz: 20

�u ana kadar yap�lanlar kaydedildi.
Program ba�tan ba�lat�l�yor.
"""

- Bu geribildirimi ald� isek, program verileri kaydetmi� demektir. Yeni hastalara ge�ilebilir.
- Az �nce girdi�imiz hasta (se�eneklerde belirtti�imize g�re) Microsoft Excel veya CSV format�ndaki veritaban�na aktar�lm��t�r.
Ayn� zamanda, txt format�nda bir rapor olu�turulmu�tur.
- Bu a�amada e�er raporu g�rmek istiyor isek, daha �nceden belirlenmi� veri klas�r�nde sonu�lar� bulabiliriz.
Rapor ismi girdi�imiz veriler ve tarih �zerinden haz�rlanmaktad�r. Yani, az sonra g�rece�iniz raporun
dosya ismi, "Deneme-1-(2017-06-06)-Bilal Bahad�r Akbulut.txt" olacakt�r.
- Rapor �rne�i:
"""
Testi uygulayan: Bilal Bahad�r Akbulut
G�n�n tarihi: 2017-06-06
Saat: 12:07:36
Hastan�n ismi: Deneme Hastas�
Hastan�n kodu: Deneme-1
Hastan�n ya��: 65
Hastan�n cinsiyeti: Erkek
Hastan�n toplam e�itim y�l�: 5
=============================================


===================================
S�zel ak�c�l�k testinin sonu�lar�: 
'S' harfi i�in: Hastan�n puan�: 2.0, Hafif derecede bozulma. Z skoru: -1.94. 2-3 persentil
'A' harfi i�in: Hastan�n puan�: 3.0, Normal. Z skoru: -0.98. 16-17 persentil
'Z' harfi i�in: Bu basamak uygulanmam�� veya uygulanamam��t�r.
===================================


===================================================================                
�NEML� UYARILAR:
    
1) Bir tak�m hasta gruplar� i�in norm de�erleri bulunmad���nda, en yak�n gruba g�re hesaplanm��t�r.
Limitleri olan testler a�a��daki �ekildedir:

 > G�rsel ��itsel Say� Dizileri: 13 <= Ya�

 > S�zel Bellek S�re�leri: 15 <= Ya� VEYA E�itim <= 19

 > Rey Karma��k Fig�r: 17 <= Ya� <= 82

 > �z s�rme: 50 <= Ya�

 > Stroop: 5 <= E�itim <= 8 VE 20 <= Ya� <=74
           8 <= E�itim VE 20 <= Ya� <= 82

 > Yeti�kin Wisconsin Kart E�leme: 5 <= E�itim VE 20 <= Ya� <= 72
                                   12 <= E�itim VE 20 <= Ya� <= 78

 > G�rsel S�zel test: 20 <= Ya� <= 100
 
 > Renkli �z S�rme: 20 <= Ya� <= 100
 
 > S�zel Ak�c�l�k: 5 <= E�itim VEYA 15 <= Ya�
 
 > Semantik Ak�c�l�k: 5 <= E�itim VEYA 15 <= Ya�
 
 > �izgi Y�n�n� Belirleme: 5 <= E�itim <= 8 VE 20 <= Ya� <= 74
                           9 <= E�itim <= 11 VE 20 <= Ya� <= 76
                           12 <= E�itim VE 20 <= Ya� <= 73

2) Testlerin sonu�lar�nda bildirilen s�zl� yorumlar, normalin 1 standart deviasyon(SD) uza��
normal, 1-2 SD aral��� hafif bozulma, 2-3 SD aral��� orta derecede bozulma, 3 SD'den uzakta olan
sonu�lar a��r derecede bozulma olarak yorumlanm��t�r.

===================================================================
Kaynak�a:
********************************

===================================================================
"""

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------

3. Se�enekler
Program bir veri ��kt�s�yla ilgili olarak bir tak�m se�enekler sunmaktad�r. Bu se�enekler program�n y�klendi�i klas�r i�erisinde "settings" adl� dosya
�zerinden d�zenlenebilir.

Program ile beraber paketlenen konfig�rasyon dosyas�ndaki se�enekler �u �ekildedir:
excel_name = benimdosyam.xlsx
Program�n Excel ��kt�s�n�n ismini d�zenler. Yukar�da belirtilen formatta olacak �ekilde herhangi bir �ey olabilir. T�rk�e karakter kullan�lmamas� tavsiye edilir.
 "-" ve "_" d���nda �zel karakter kullan�lmamas� tavsiye edilir.
excel_output_subjectNames = True
Excel dosyas�na denek isimlerinin ��kt�s� yap�l�p yap�lmama durumunun bildirir.
G�venlik kayg�lar� a��s�ndan eklenmi�tir.

auto_run = True/False
Program�n her seferinde otomatik ba�tan ba�lama sistemini kapat�r.
Her i�lem bitiminde kendili�inden program kapanacakt�r.

output_csv = True/False ('True' ise csv dosyalar� olu�turulur, 'False' ise olu�turulmaz.)
output_txt = True/False ('True' ise txt dosyas� olu�turulur, 'False' ise olu�turulmaz.)
output_excel = True/False ('True' ise excel dosyas� olu�turulur, 'False' ise olu�turulmaz.)

csv_path = "csv dosyalar�n�n kaydedilece�i adres" 
txt_path = "txt dosyalar�n�n kaydedilece�i adres"
excel_path = "excel dosyalar�n�n kaydedilece�i adres"
Default olmas� halinde bilgisayar ��kt�lar� program�n bulundu�u klas�r�n i�inde
"Results" isimli bir klas�r olu�turarak oraya yerle�tirir. 

E�er ��kt� klas�r�n� de�i�tirmek isterseniz adresin yaz�lma format� �u �ekilde olmal�d�r:
csv_path = C:/Users/BenimBilgisayar�m/Desktop/data/csv/
txt_path = C:/Users/BenimBilgisayar�m/Desktop/raporlar/
veya
csv_path = C:/csv_depo/
txt_path = C:/Users/BenimBilgisayar�m/Desktop/
gibi.

--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------
4. Yazarlar:
Dr. Bilal Bahad�r Akbulut � Kodlama & Tasar�m
Do�. Dr. Yavuz Ayhan � Proje Dan��man�
--------------------------------------------------------------------------------------------------------
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////////////////////
--------------------------------------------------------------------------------------------------------
5. Bilgilendirme ve Referanslar
Program yaz�l�rken kullan�lan Python 3.6.x, ilgili k�t�phaneleri ve program kaynak kodundan �al��t�r�labilir hale 
getirilirken kullan�lan cx_freeze Python mod�l� a��k kaynakl� yaz�l�mlard�r.

Program i�inde kullan�lan n�ropsikiyatrik testlerin T�rk toplumuna uyarlanma �al��malar� �u gruplar taraf�ndan yap�lm��t�r:
>Cangoz, B., Karakoc, E., & Selekler, K. (2009). Trail Making Test: normative data for Turkish elderly population by age, sex and education. J Neurol Sci, 283(1-2), 73-78. doi: 10.1016/j.jns.2009.02.313

>Cang�z B, K. E., Selekler K (2006 ). Saat �izme Testi�nin T�rk yeti�kin ve ya�l� �rneklemi �zerindeki norm belirleme, ge�erlik ve g�venirlik �al��malar�. . T�rk Geriatri Dergisi,, 9 (3), 136-142. 

>Karaka�, S., Erdo�an Bakar, E., Do�utepe Din�er, E. (2013). B�LNOT Bataryas� El Kitab�: N�ropsikolojik Testlerin Yeti�kinler i�in Ara�t�rma ve Geli�tirme �al��malar�: B�LNOT- Yeti�kin (Cilt I-II) 

>Keskinoglu, P., Ucku, R., Yener, G., Yaka, E., Kurt, P., & Tunca, Z. (2009). Reliability and validity of revised Turkish version of Mini Mental State Examination (rMMSE-T) in community-dwelling educated and uneducated elderly. Int J Geriatr Psychiatry, 24(11), 1242-1250. doi: 10.1002/gps.2252

>Kudiaki, C., & Aslan, A. (2008). Executive functions in a Turkish sample: associations with demographic variables and normative data. Appl Neuropsychol, 15(3), 194-204. doi: 10.1080/09084280802324416

>Saka, E., Mihci, E., Topcuoglu, M. A., & Balkan, S. (2006). Enhanced cued recall has a high utility as a screening test in the diagnosis of Alzheimer's disease and mild cognitive impairment in Turkish people. Arch Clin Neuropsychol, 21(7), 745-751. doi: 10.1016/j.acn.2006.08.007

>Selekler, K. C., B, Ulu�, S. . (2010). Montreal Bili�sel De�erlendirme �l�e�i'nin (MOB�D) Hafif Bili�sel Bozukluk ve Alzheimer Hastalar�n� ay�rdedebilme g�c�n�n incelenmesi. T�rk Geriatri Dergisi,, 13(3), 166-171. 

>Tanor, O. (2006). �ktem S�zel Bellek S�re�leri Testi. Ankara: T�rk Psikologlar Derne�i.

>Teng, E. L., & Chui, H. C. (1987). The Modified Mini-Mental State (3MS) examination. J Clin Psychiatry, 48(8), 314-318. 

>Varan E, Tanor O, Gurvit H (2007) Rey Karma��k Fig�r Testi ve Tan�ma Uygulamas� (RKFT-T): Bir Yeti�kin T�rk �rneklemi �zerinde Norm Belirleme �al��mas�.  Turk J Neurol. 2007; 13(6): 387-394
