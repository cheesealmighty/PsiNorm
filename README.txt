Versiyon 1.9.0:

1. Bütün testlerin verileri JSON dosyalarına taşındı. 
 1.a) Gelecekte test normlarının yazılımın kendisinde değişiklik yapılmadan değiştirilmesine imkan sağlayacaktır.
 1.b) Wechsler testinin hesaplanması konvansiyonel (Z skor üzerinden) olmadığı için, veriler taşındı, fakat yazılım içindeki yorumlayıcısı değişmedi.
 1.c) CCT testi iki parçalı ve farklı norm aralıkları üzerinden olduğu için, veriler taşındı, fakat yazılım içinde özel yorumlayıcı eklendi.

2. Test seçim ekranı (mainMenu()) grafik arayüz ile değiştirildi. 
 2.a) Test seçim ekranı otomatik olarak documents/psinorm/data/cogs/menuData.json üzerinden otomatik hazırlanıyor.
 2.b) Bu şekilde ana menüden istenilen testler çıkarılabilir, yeni testler eklenebilir.
 
3. Bütün testlerin kendi yorumlayıcıları tek bir taslak altında toplandı.
 3.a) Bu sayede kullanıcılar istedikleri testleri ekleyip çıkarabilecek.
 3.b) Taslak hem Z skoru, hem cutOff usulü testleri yorumlayabilir. 
 3.c) Taslağa basit aritmetik desteği eklendi. Basit aritmetik burada: +, -, *, / anlamına gelmektedir. Örnek: Trailmaking testinde B+A, B-A gibi.
  
4. Mümkün olan tüm menülerde <TAB> ve <ENTER> tuşları ile hareket etme imkanı sağlandı. Bu şekilde kullanıcılar fareyi kullanmadan test girişi yapabilecek.

5. Hasta notları giriş sistemi iyileştirildi. 
 5.a) Kaydetmeden çıkış yaparken uyarı.
 5.b) Kaydet tuşuna basınca geri bildirim.
 
6. Excel sütun bilgileri JSON dosyasına taşındı. Yeni test eklemede önemli bu.
 
7. Genel olarak tüm program data dosyaları Documents'teki Psinorm klasörüne taşındı. Bu kullanıcının erişimini kolaylaştıracaktır.
 7.a) Eğer kullanıcı uygunsuz bir değişiklik yaparsa, yazılımın kendi klasöründe varsayılanlar da saklı tutulmaktadır.
 
8. Test giriş ekranı grafik arayüz ile değiştirildi. 

9. Minör bug fixes.
