# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 13:47:30 2017

@author: Cheese
"""

testDict = {"1":{
#headlinesDictionary
"titleDict": {
"1": """
SAĞLIKLI KATILIMCILAR İÇİN BİLGİ TOPLAMA FORMU

------------------------------------------------------------------------------
DİKKAT !

>Bilgi Toplama Formunda yer alan sorulara geçmeden önce, 
 araştırma hakkında katılımcıya kısaca bilgi verin.
	
>Test uygulama oturumunun başında katılımcıdan aşağıdaki konularda bilgi alın.
------------------------------------------------------------------------------   
""",

"5": """
------------------------------------------------------------------------------   
DİKKAT !	
    Katılımcının bildirdiği ilaçlar bilişsel süreçleri etkileyen türdense,
    daha sonra uygulamaya almak için katılımcıdan aşağıdaki konularda bilgi alabilirsiniz.
    Ancak bildirilen ilaçların etkisi ortadan kalkana kadar
    katılımcıya herhangi bir nöropsikolojik test uygulamayın.
------------------------------------------------------------------------------   

Kimlik Bilgileri ve Demografik Özellikler
------------------------------------------------------------------------------
""",

"20": """
Eğitim Durumu
------------------------------------------------------------------------------
""",

"23": """
Fizyolojik  Özellikler ve  Sağlık Durumu
------------------------------------------------------------------------------
"""
}, 
#end of headlines

#mainquestiondictionary
"qDict": {        
        
"1": {"qType": "cQuest", "qText": "Katılımcı No: "},
            
"2": {"qType": "cQuest", "qText": "Katılımcı Kodu: "},

"3": {"qType":"eQuest", 
      "qText":"Kullanılmakta olan ilaçların adları / Miktarları / Kullanım süreleri",
      "colNum":3,
          "1": "İlaç adı: ", 
          "2": "Miktarı: ",
          "3": "Kullanım süresi: " },
      
"4": {"qType":"eQuest", 
      "qText":"Uzun süre kullanıldıktan sonra bırakılan ilaçların adları / Miktarları / Kullanım süreleri / Ne kadar süre önce bırakıldığı",
      "colNum":4,
          "1": "İlaç adı: ", 
          "2": "Miktarı: ",
          "3": "Kullanım süresi: ",
          "4": "Ne kadar süre önce bırakıldığı: "},

"5": {"qType": "pullData", "qText": "Katılımcı ismi: ", "data": "patient_name"},

"6": {"qType": "pullData", "qText": "Katılımcı cinsiyeti: ", "data": "patient_sex"},

"7": {"qType": "cQuest", 
      "qText": "Doğum yeri: "},

"8": {"qType": "runFunc", "qText": "Doğum tarihi: ", "runFunc": "calculate_age", "arg": "patient_age"},   #birthday
        
"9": {"qType": "pullData", "qText": "Katılımcı yaşı: ", "data": "patient_age"},

"10": {"qType": "mQuest", 
       "qText": "Medeni hali:", "optNum": 4, 
           "1": "Evli",
           "2": "Bekar",
           "3": "Dul/Boşanmış",
           "4": "Bilinmiyor",
           "extraMark": [None]},
       
"11": {"qType": "cQuest", 
       "qText": "Ev adresi: "},

"12": {"qType": "cQuest", 
       "qText": "Yazışma adresi (yukarıdakinden farklı ise): "},

"13": {"qType": "cQuest", 
       "qText": "Söz konusu il / ilçe / köyde oturma süresi: "},
       
"14": {"qType": "cQuest",
       "qText": "Telefon Numarası - Ev: "},
       
"15": {"qType": "cQuest",
       "qText": "Telefon Numarası - İş: "},

"16": {"qType": "cQuest",
       "qText": "Fax Numarası - Ev: "},

"17": {"qType": "cQuest",
       "qText": "Fax Numarası - İş: "},
       
"18": {"qType": "cQuest",
       "qText": "E-posta: "},
       
"19": {"qType": "cQuest",
       "qText": "Ailenin yaklaşık geliri: "},     
       
"20": {"qType": "mQuest",
      "qText": "Eğitim Durumu",
      "optNum": 7, 
         "1": "Çalışan katılımcı",
         "2": "Okuyan katılımcı (zorunlu temel eğitim: ilkokul ve ortaokul ve/veya lise)",
         "3": "Yükseköğrenim görmekte olan katılımcı",
         "4": "Yüksek lisans",
         "5": "Doktora",
         "6": "Tıpta uzmanlık",
         "7": "Bilinmiyor", 
         "extraMark": ["1", "2", "3", "4", "5", "6"]},
         
"21": {"qType": "mQuest",
      "qText": "Annenin Eğitim Durumu", "optNum": 8, 
          "1": "Bilmiyor",
          "2": "Yok",
          "3": "Okuryazar",
          "4": "İlköğretim",
          "5": "Ortaokul",
          "6": "Lise",
          "7": "Yükseköğretim",
          "8": "Bilinmiyor",
          "extraMark": ["7"]},
      
"22": {"qType": "mQuest",
      "qText": "Babanın Eğitim Durumu", "optNum": 8, 
          "1": "Bilmiyor",
          "2": "Yok",
          "3": "Okuryazar",
          "4": "İlköğretim",
          "5": "Ortaokul",
          "6": "Lise",
          "7": "Yükseköğretim",
          "8": "Bilinmiyor",
          "extraMark": ["7"]},   

"23": {"qType": "mQuest",
       "qText": """El tercihi: 
(El tercihini, uzağa bir taş atması gerektiğinde katılımcıya hangi elini kullanacağını sorarak belirleyin.)""",
        "optNum": 4, 
          "1": "Sağ",
          "2": "Sol",
          "3": "Her ikisi",
          "4": "Bilinmiyor",
          "extraMark": [None]},

"24": {"qType": "mQuest",
       "qText": "İşitme bozukluğu var mı? ", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"25": {"qType": "mQuest",
       "qText": "Görme bozukluğu var mı? ",
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"26": {"qType": "mQuest",
       "qText": """Renk ayırt etmeyle ilgili bir  problem var mı?
       
(12'lik bir kalem setindeki kalemleri katılımcıya  teker teker göstererek,
ondan bu kalemlerin  ne renk olduğunu söylemesini isteyin. 
Katılımcı bu renkleri ayırt edemiyorsa, renklerin kullanıldığı
WCST, WMS-R ve Stroop Testi TBAG Formu gibi testleri uygulamayın.)  
""", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": [None]},

"27": {"qType": "mQuest",
       "qText": "Başkaca fiziksel özürleri var mı? ", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"28": {"qType":"eQuest", 
      "qText":"""
Geçirdiği önemli rahatsızlıkları, ameliyatları vs. tarihleri ile birlikte belirtin
(Nörolojik, psikolojik ve psikiyatrik olanlara özellikle değinin.).""",
      "colNum":3,
          "1": "Olay tanımı: ", 
          "2": "Tarihi: ",
          "3": "Açıklama: " },

"29": {"qType": "mQuest",
       "qText": "Daha ileriki bir tarihte kendisine  diğer bazı testlerin  uygulanmasını istiyor mu? ",
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"30": {"qType": "cQuest", "qText": "Uygulayıcının adı soyadı: "},
    
"31": {"qType": "cQuest", "qText": "Uygulama yeri: "},
    
"32": {"qType": "eQuest",
       "qText": "Uygulayıcının belirtilmesinde yarar gördüğü diğer hususlar: ",
       "colNum": 1,
       "1": "Notlar: "}

}, 
       

#end of main question dictionary
 
#extraQuestionsDictionary
"xtraQDict": {

    "20-1": {
            "1": {"qType": "cQuest", "qText": "En son mezun olduğu okul: "},
        
            "2": {"qType": "cQuest", "qText": "Görevi: "},
            
            "3": {"qType": "cQuest", "qText": "Görev ünvanı: "},
            
            "4": {"qType": "cQuest", "qText": "Hem çalışıp hem okuyorsa, devam ettiği okul: "},
            
            "5": {"qType": "cQuest", "qText": "İşten ayrıldıysa, ayrılma nedeni: "},
            
            "6": {"qType": "cQuest", "qText": "Ne kadar süre önce işten ayrıldığı: "}},
            
    "20-2": {
            "1": {"qType": "cQuest", "qText": "Okul: "},
        
            "2": {"qType": "cQuest", "qText": "Sınıf: "},
            
            "3": {"qType": "mQuest",
                  "qText": "Alınan eğitimin türü: ",
                  "optNum": 3,
                  "1": "Örgün",
                  "2": "Dışarıdan bitirme",
                  "3": "Bilinmiyor",
                  "extraMark": [None]}},
            
    "20-3": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "},
      
            "4": {"qType": "cQuest", "qText": "Sınıf: "},
            
            "5": {"qType": "mQuest",
                  "qText": "Alınan eğitimin türü: ",
                  "optNum": 3,
                  "1": "Örgün",
                  "2": "Dışarıdan bitirme",
                  "3": "Bilinmiyor",
                  "extraMark": [None]}},
            
    "20-4": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "}},
            
    "20-5": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "}},
       
    "20-6": {
            "1": {"qType": "cQuest", "qText": "Üniversite/Eğitim Hastanesi: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "},
            
            "4": {"qType": "cQuest", "qText": "Uzmanlık Alanı: "}}
        
        , #end of 20
    
    "21-7": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "}}
    
        ,#end of 21
    
    "22-7": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "}}
    
        ,#end of 22
   
    "24-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        ,#end of 24
    
    
    "25-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        , #end of 25    
    
    "27-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        , #end of 27   
    
    "29-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
         #end of 27   
    
#end of extra question dictionary
},
"templateDict": {

       },#end of template dictionary
"excelSheetName": "Sağlıklı Form"
},

"2":{
#headlinesDictionary
"titleDict": {
"1": """
KLİNİK OLGULAR İÇİN BİLGİ TOPLAMA FORMU

------------------------------------------------------------------------------
DİKKAT !

>Bilgi Toplama Formunda yer alan sorulara geçmeden önce, 
 araştırma hakkında olguya kısaca bilgi verin.
	
>Test uygulama oturumunun başında olgudan aşağıdaki konularda bilgi alın.
------------------------------------------------------------------------------   
""",

"7": """
------------------------------------------------------------------------------   
DİKKAT !	
    Olgunun bildirdiği ilaçlar bilişsel süreçleri etkileyen türdense,
    daha sonra uygulamaya almak için olgudan aşağıdaki konularda bilgi alabilirsiniz.
    Ancak bildirilen ilaçların etkisi ortadan kalkana kadar
    olguya herhangi bir nöropsikolojik test uygulamayın.
------------------------------------------------------------------------------   

Kimlik Bilgileri ve Demografik Özellikler
------------------------------------------------------------------------------
""",

"22": """
Eğitim Durumu
------------------------------------------------------------------------------
""",

"25": """
Fizyolojik  Özellikler ve  Sağlık Durumu
------------------------------------------------------------------------------
"""
}, 
#end of headlines

#mainquestiondictionary
"qDict": {        
        
"1": {"qType": "cQuest", "qText": "Olgu No: "},
            
"2": {"qType": "cQuest", "qText": "Olgu Kodu: "},

"3": {"qType": "cQuest", "qText": "Tanı Kodu: "},

"4": {"qType": "cQuest", "qText": "Tanı No: "},

"5": {"qType":"eQuest", 
      "qText":"Kullanılmakta olan ilaçların adları / Miktarları / Kullanım süreleri",
      "colNum":3,
          "1": "İlaç adı: ", 
          "2": "Miktarı: ",
          "3": "Kullanım süresi: " },
      
"6": {"qType":"eQuest", 
      "qText":"Uzun süre kullanıldıktan sonra bırakılan ilaçların adları / Miktarları / Kullanım süreleri / Ne kadar süre önce bırakıldığı",
      "colNum":4,
          "1": "İlaç adı: ", 
          "2": "Miktarı: ",
          "3": "Kullanım süresi: ",
          "4": "Ne kadar süre önce bırakıldığı: "},

"7": {"qType": "pullData", "qText": "Olgu ismi: ", "data": "patient_name"},

"8": {"qType": "pullData", "qText": "Olgu cinsiyeti: ", "data": "patient_sex"},

"9": {"qType": "cQuest", 
      "qText": "Doğum yeri: "},

"10": {"qType": "runFunc", "qText": "Doğum tarihi: ", "runFunc": "calculate_age", "arg": "patient_age"},   #birthday
        
"11": {"qType": "pullData", "qText": "Olgu yaşı: ", "data": "patient_age"},

"12": {"qType": "mQuest", 
       "qText": "Medeni hali:", "optNum": 4, 
           "1": "Evli",
           "2": "Bekar",
           "3": "Dul/Boşanmış",
           "4": "Bilinmiyor",
           "extraMark": [None]},
       
"13": {"qType": "cQuest", 
       "qText": "Ev adresi: "},

"14": {"qType": "cQuest", 
       "qText": "Yazışma adresi (yukarıdakinden farklı ise): "},

"15": {"qType": "cQuest", 
       "qText": "Söz konusu il / ilçe / köyde oturma süresi: "},
       
"16": {"qType": "cQuest",
       "qText": "Telefon Numarası - Ev: "},
       
"17": {"qType": "cQuest",
       "qText": "Telefon Numarası - İş: "},

"18": {"qType": "cQuest",
       "qText": "Fax Numarası - Ev: "},

"19": {"qType": "cQuest",
       "qText": "Fax Numarası - İş: "},
       
"20": {"qType": "cQuest",
       "qText": "E-posta: "},
       
"21": {"qType": "cQuest",
       "qText": "Ailenin yaklaşık geliri: "},     
       
"22": {"qType": "mQuest",
      "qText": "Eğitim Durumu",
      "optNum": 7, 
         "1": "Çalışan olgu",
         "2": "Okuyan olgu (zorunlu temel eğitim: ilkokul ve ortaokul ve/veya lise)",
         "3": "Yükseköğrenim görmekte olan olgu",
         "4": "Yüksek lisans",
         "5": "Doktora",
         "6": "Tıpta uzmanlık",
         "7": "Bilinmiyor",
         "extraMark": ["1", "2", "3", "4", "5", "6"]},
         
"23": {"qType": "mQuest",
      "qText": "Annenin Eğitim Durumu", "optNum": 8, 
          "1": "Bilmiyor",
          "2": "Yok",
          "3": "Okuryazar",
          "4": "İlköğretim",
          "5": "Ortaokul",
          "6": "Lise",
          "7": "Yükseköğretim",
          "8": "Bilinmiyor",
          "extraMark": ["7"]},
      
"24": {"qType": "mQuest",
      "qText": "Babanın Eğitim Durumu", "optNum": 8, 
          "1": "Bilmiyor",
          "2": "Yok",
          "3": "Okuryazar",
          "4": "İlköğretim",
          "5": "Ortaokul",
          "6": "Lise",
          "7": "Yükseköğretim",
          "8": "Bilinmiyor",
          "extraMark": ["7"]},   

"25": {"qType": "mQuest",
       "qText": """El tercihi: 
(El tercihini, uzağa bir taş atması gerektiğinde olguya hangi elini kullanacağını sorarak belirleyin.)""",
        "optNum": 4, 
          "1": "Sağ",
          "2": "Sol",
          "3": "Her ikisi",
          "4": "Bilinmiyor",
          "extraMark": [None]},

"26": {"qType": "mQuest",
       "qText": "İşitme bozukluğu var mı? ", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"27": {"qType": "mQuest",
       "qText": "Görme bozukluğu var mı? ",
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"28": {"qType": "mQuest",
       "qText": """Renk ayırt etmeyle ilgili bir  problem var mı?
       
(12'lik bir kalem setindeki kalemleri olguya  teker teker göstererek,
ondan bu kalemlerin  ne renk olduğunu söylemesini isteyin. 
Olgu bu renkleri ayırt edemiyorsa, renklerin kullanıldığı
WCST, WMS-R ve Stroop Testi TBAG Formu gibi testleri uygulamayın.)  
""", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": [None]},

"29": {"qType": "mQuest",
       "qText": "Başkaca fiziksel özürleri var mı? ", 
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"30": {"qType":"eQuest", 
      "qText":"""
Geçirdiği önemli rahatsızlıkları, ameliyatları vs. tarihleri ile birlikte belirtin
(Nörolojik, psikolojik ve psikiyatrik olanlara özellikle değinin.).""",
      "colNum":3,
          "1": "Olay tanımı: ", 
          "2": "Tarihi: ",
          "3": "Açıklama: " },
       
"31": {"qType": "cQuest", "qText": "Olgunun tanısı: "},

"32": {"qType": "mQuest", "qText": "Olgunun tedavi şekli: ", 
       "optNum": 2,
           "1": "Yatarak tedavi görüyor. ",
           "2": "Ayaktan tedavi görüyor.",
           "extraMark": ["1", "2"]},
       
"33": {"qType": "cQuest", "qText": "Tedavi süresi: "},        

"34": {"qType": "mQuest",
       "qText": "Daha ileriki bir tarihte kendisine  diğer bazı testlerin  uygulanmasını istiyor mu? ",
       "optNum": 3,
           "1": "Evet",
           "2": "Hayır",
           "3": "Bilinmiyor",
           "extraMark": ["1"]},
       
"35": {"qType": "cQuest", "qText": "Uygulayıcının adı soyadı: "},
    
"36": {"qType": "cQuest", "qText": "Uygulama yeri: "},
    
"37": {"qType": "eQuest",
       "qText": "Uygulayıcının belirtilmesinde yarar gördüğü diğer hususlar: ",
       "colNum": 1,
       "1": "Notlar: "}

}, 
       

#end of main question dictionary
 
#extraQuestionsDictionary
"xtraQDict": {

    "22-1": {
            "1": {"qType": "cQuest", "qText": "En son mezun olduğu okul: "},
        
            "2": {"qType": "cQuest", "qText": "Görevi: "},
            
            "3": {"qType": "cQuest", "qText": "Görev ünvanı: "},
            
            "4": {"qType": "cQuest", "qText": "Hem çalışıp hem okuyorsa, devam ettiği okul: "},
            
            "5": {"qType": "cQuest", "qText": "İşten ayrıldıysa, ayrılma nedeni: "},
            
            "6": {"qType": "cQuest", "qText": "Ne kadar süre önce işten ayrıldığı: "}},
            
    "22-2": {
            "1": {"qType": "cQuest", "qText": "Okul: "},
        
            "2": {"qType": "cQuest", "qText": "Sınıf: "},
            
            "3": {"qType": "mQuest",
                  "qText": "Alınan eğitimin türü: ",
                  "optNum": 3,
                  "1": "Örgün",
                  "2": "Dışarıdan bitirme",
                  "3": "Bilinmiyor",
                  "extraMark": [None]}},
            
    "22-3": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "},
      
            "4": {"qType": "cQuest", "qText": "Sınıf: "},
            
            "5": {"qType": "mQuest",
                  "qText": "Alınan eğitimin türü: ",
                  "optNum": 3,
                  "1": "Örgün",
                  "2": "Dışarıdan bitirme",
                  "3": "Bilinmiyor",
                  "extraMark": [None]}},
            
    "22-4": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "}},
            
    "22-5": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "}},
       
    "22-6": {
            "1": {"qType": "cQuest", "qText": "Üniversite/Eğitim Hastanesi: "},
        
            "2": {"qType": "cQuest", "qText": "Enstitü: "},
            
            "3": {"qType": "cQuest", "qText": "Anabilim Dalı: "},
            
            "4": {"qType": "cQuest", "qText": "Uzmanlık Alanı: "}}
        
        , #end of 20
    
    "23-7": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "}}
    
        ,#end of 21
    
    "24-7": {
            "1": {"qType": "cQuest", "qText": "Üniversite: "},
        
            "2": {"qType": "cQuest", "qText": "Fakülte: "},
            
            "3": {"qType": "cQuest", "qText": "Bölüm: "}}
    
        ,#end of 22
   
    "26-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        ,#end of 24
    
    
    "27-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        , #end of 25    
    
    "29-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        , #end of 27   
    
    "32-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
        
        ,
        
    "32-2": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
        , #end of 30
    
    "34-1": {
            "1": {"qType": "cQuest", "qText": "Belirtiniz: "}}
    
         #end of 32
    
#end of extra question dictionary
},
"templateDict": {
       },#end of template dictionary
"excelSheetName": "Klinik Olgu Form"
},
"formNames": {"1": "SAĞLIKLI KATILIMCILAR İÇİN BİLGİ TOPLAMA FORMU",
              "2": "KLİNİK OLGULAR İÇİN BİLGİ TOPLAMA FORMU"}


}
#end of the main dict


testDict1 = {"testName": "İşaretleme Testi", #Name of the test
                "itemsTotNum": 20, #total number of items in the test
                "sexDiff": False, #whether there's sex difference
                "ageDiff": True, #whether there's a age difference
                "eduDiff": True, #whether there's a education level difference
                "itemsDict": 
                    {
                        "1": "Düzenli Harfler Formu\nİşaretlenen hedef sayısı puanı: ",
                        "2": "Atlanan hedef sayısı puanı: ",
                        "3": "İşaretlenen yanlış half sayısı puanı: ",
                        "4": "Toplam hata puanı: ",
                        "5": "Tarama süresi puanı: ",
                        "6": "Düzenli Şekiller Formu\nİşaretlenen hedef sayısı puanı: ",
                        "7": "Atlanan hedef sayısı puanı: ",
                        "8": "İşaretlenen yanlış half sayısı puanı: ",
                        "9": "Toplam hata puanı: ",
                        "10": "Tarama süresi puanı: ",
                        "11": "Düzensiz Harfler Formu\nİşaretlenen hedef sayısı puanı: ",
                        "12": "Atlanan hedef sayısı puanı: ",
                        "13": "İşaretlenen yanlış half sayısı puanı: ",
                        "14": "Toplam hata puanı: ",
                        "15": "Tarama süresi puanı: ",
                        "16": "Düzensiz Şekiller Formu\nİşaretlenen hedef sayısı puanı: ",
                        "17": "Atlanan hedef sayısı puanı: ",
                        "18": "İşaretlenen yanlış half sayısı puanı: ",
                        "19": "Toplam hata puanı: ",
                        "20": "Tarama süresi puanı: "},
                    
                    
                "subGroups": [
                        {
                            "eduMin": 0, #orijinal data 5 
                            "eduMax": 11,
                            "ageMin": 0, #orijinal data 20
                            "ageMax": 54,
                            "1": [58.87, 1.64],
                            "2": [1.12, 1.64],
                            "3": [0.01, 0.11],
                            "4": [1.13, 1.64],
                            "5": [120.07, 44.20],
                            "6": [58.05, 2.21],
                            "7": [1.94, 2.23],
                            "8": [0.22, 0.67],
                            "9": [2.16, 2.47],
                            "10": [113.21, 43.07],
                            "11": [59.05, 1.21],
                            "12": [0.96, 1.21],
                            "13": [0.00, 0.00],
                            "14": [0.95, 1.21],
                            "15": [123.18, 46.62],
                            "16": [59.32, 1.10],
                            "17": [0.68, 1.10],
                            "18": [0.04, 0.23],
                            "19": [0.72, 1.14],
                            "20": [102.86, 41.81]},
    
                    
                        {
                            "eduMin": 0, #original data 5
                            "eduMax": 11, 
                            "ageMin": 55, 
                            "ageMax": 999, #orijinal data 89
                            "1": [58.77, 1.77],
                            "2": [1.23, 1.77],
                            "3": [0.05, 0.21],
                            "4": [1.27, 1.80],
                            "5": [153.59, 42.04],
                            "6": [57.86, 2.46],
                            "7": [2.14, 2.46],
                            "8": [0.86, 1.36],
                            "9": [3.00, 2.81],
                            "10": [144.45, 44.57],
                            "11": [58.68, 1.52],
                            "12": [1.32, 1.52],
                            "13": [0.00, 0.00],
                            "14": [1.32, 1.52],
                            "15": [160.50, 46.02],
                            "16": [58.64, 1.56],
                            "17": [1.36, 1.56],
                            "18": [0.14, 0.47],
                            "19": [1.50, 1.63],
                            "20": [132.45, 36.43]},
                        
                        {
                            "eduMin": 12, 
                            "eduMax": 999, #infinity and beyond
                            "ageMin": 0, #orijinal data 20
                            "ageMax": 54,    
                            "1": [],
                            "2": [],
                            "3": [],
                            "4": [],
                            "5": [],
                            "6": [],
                            "7": [],
                            "8": [],
                            "9": [],
                            "10": [],
                            "11": [],
                            "12": [],
                            "13": [],
                            "14": [],
                            "15": [],
                            "16": [],
                            "17": [],
                            "18": [],
                            "19": [],
                            "20": []},
                        
                        {
                            "eduMin": 12, 
                            "eduMax": 999, #infinity and beyond
                            "ageMin": 55, 
                            "ageMax": 999, #orijinal data 85
                            "1": [],
                            "2": [],
                            "3": [],
                            "4": [],
                            "5": [],
                            "6": [],
                            "7": [],
                            "8": [],
                            "9": [],
                            "10": [],
                            "11": [],
                            "12": [],
                            "13": [],
                            "14": [],
                            "15": [],
                            "16": [],
                            "17": [],
                            "18": [],
                            "19": [],
                            "20": []}
                            
                            
                            ]}




info_data = {
        "agreeTerms_data": """HAKKINDA
2017© Bilal Bahadır Akbulut, Yavuz Ayhan.  
Katkıda bulunanlar: Sirel Karakaş, Emel Erdoğan Bakar, Elvin Doğutepe Dinçer (Neurometrika-Tech); Duygu Çap, Ceren Şimşek, Berge Velibaşoğlu; Enes Çömez.  

Bu programın KESİNLİKLE HİÇBİR TEMİNATI YOKTUR; ayrıntılar için programın içinde bulunduğu klasördeki lisans dosyalarına başvurunuz.

Bu bir özgür yazılımdır, ve bazı koşullar altında yeniden dağıtmakta serbestsiniz; ayrıntılar için programın içinde bulunduğu klasördeki lisans dosyalarına başvurunuz.

=========================================================================
LÜTFEN OKUYUNUZ
=========================================================================

1. PsiNorm yazılımı uygulayıcı tarafından girilen içeriği kontrol etmemektedir.  İçerik sayısal olarak uygun olmasa dahi hesaplama yapılmakta ve uygulayıcıya sonuç verilmektedir.  Lütfen girişin doğru yapıldığına emin olunuz. 

2. PsiNorm yazılımı sonuçları işlenirken tarih ve saat bilgilerini otomatik olarak kaydetmektedir.  Lütfen bilgisayarınızın saatinin güncel olduğundan emin olunuz.

3. PsiNorm, alanda çalışan uygulayıcıların ihtiyaçları doğrultusunda geliştirilmiş ücretsiz bir yazılımdır.    Sonraki uyarlamalarda yazılımın daha iyi hale getirilmesi için uygulayıcıların katkı ve önerilerini gerekli görüyoruz.  Lütfen öneri ve eleştirilerinizi b.bahadirakbulut@gmail.com adresine yazınız.   

4. Çok basamaklı kalite kontrol aşamalarından geçse de uygulayıcı PsiNorm'da hatalar fark edebilir.  Hata fark ettiğiniz hususları lütfen b.bahadirakbulut@gmail.com adresine bildiriniz.  Maddi hatalar mümkün olduğunca hızlı şekilde ele alınacaktır.

5. PsiNorm kullanılarak yapılan akademik çalışmalarınızda PsiNorm'a atıfta bulunmanız gerekmektedir.  Lütfen atıfta bulunulacak çalışma için demans.org websitesini takip ediniz.

6. Bir sorunuz olduğunda lütfen Sık Sorulan Sorular bölümünü kontrol ediniz.  Sık Sorulan Sorulara giriş ekranından ulaşabilirsiniz.  Bu kısımda sorunuza yanıt bulamazsanız psinormsoftware@gmail.com adresine yazınız ve https://github.com/cheesealmighty/PsiNorm/issues sayfasında bir bildirim oluşturunuz. Sizinle 10 iş günü içinde iletişime geçilmeye çalışılacaktır.

7. PsiNorm yazılımı kaynaklarda verilen çalışmalar esas alınarak hazırlanmıştır, dolayısıyla yazılım sonuçları yalnız kaynaklardaki testler için geçerlidir, başka uyarlamalar için kullanılamaz.  Testler ile ilgili detaylı bilgi ve norm tabloları için lütfen ilgili kaynağa ulaşınız.
=========================================================================

Okudum, anladım ve kabul ediyorum.
""",
    
        "FAQ_data": """========================================
SIK SORULAN SORULAR
========================================
1."Yazılım kesirli sayıları kabul etmiyor.  Örneğin 18,5 girdiğimde hata veriyor."

Küsurat belirtirken lütfen nokta kullanınız.  Yukarıdaki örnekte "18,5" yerine "18.5" yazınız.

2."Testte yanlışlıkla 35 yazacağıma 350 yazdım, testin normlarında böyle bir değer olmamasına rağmen sonuç "Normal" olarak rapor edildi.  Oysa testten alınabilecek en yüksek puan 48\"

PsiNorm yazılımı uygulayıcı tarafından girilen içeriği kontrol etmemektedir.  İçerik sayısal olarak uygun olmasa dahi (yukarıdaki örnekte norm/eşik değerleri için belirlenen değerlerin dışında) program tarafından hesaplama yapılmakta ve uygulayıcıya sonuç verilmektedir.  Yine de bazı testlerde uyarı görmeniz olasıdır.  Lütfen girişin doğru yapıldığına emin olunuz. 

3.\"Kişiye testi uygularken önceki test sonuçlarını yukarı çıkıp sonucu kontrol etmek istiyorum ama müsaade etmiyor, ekranda yukarı çıkamıyorum."

PsiNorm yazılımının temel alındığı program giriş esnasında üst satırların kullanımına müsaade etmemektedir.  İlgili testin sonuçlarını TEST TAMAMLANDIKTAN SONRA (yani 22 komutu verildikten sonra oluşturulan) text veya excel dosyasından kontrol edebilirsiniz.  Eğer TEST ESNASINDA yanlış giriş yaptığınızdan şüphe ederseniz aynı test sonuçlarını tekrar girebilirsiniz.  Lütfen test ekranındaki yönergeleri takip ediniz.

4."Sonuçları nereden bulacağım?"

Sonuçlar "documents" ya da "belgelerim" içinde "PsiNorm" klasöründe bulunabilir.  Txt dosyaları katılımcı kodu ile tanınabilir; excel dosyasında her test için ilk sütunlar katılımcı bilgilerine ayrılmıştır. 

5."Excel dosyasında bir şey görünmüyor, nereden sonuçları bulacağım?"

Dosyadaki sayfaları (sheet) kontrol ediniz.  Her test için bir sayfa ayrılmıştır.  Bazı test maddelerinde yanıt sayısında farklılık olabileceği için (örneğin "kullandığı ilaçlar" sorusunda bir katılımcı için 5 kaleme yönelik giriş yapacak iken diğer katılımcı için 7 kaleme yönelik giriş yapılabilir)  cevap vermediğiniz halde bazı alanların boş bırakıldığını görebilirsiniz.  Bu nedenle lütfen başlıklara göre hücreleri kontrol ediniz.

6."Test sonuçlarının ne anlama geldiğini nasıl öğreneceğim?"

PsiNorm nöropsikolojik testlerin normlarını otomatik hesaplamakta ve kullanıcının hizmetine sunmaktadır.  Test sonuçlarını yorumlamak amacı gütmemektedir.  Test sonuçlarının nasıl yorumlanacağı ile ilgili lütfen test çıktısında belirtilen kaynaklara başvurunuz.  

7." … testinin norm verileri/ geçerlik çalışması yayımlandı.  Bunu da eklemek mümkün mü?"

PsiNorm, alanda çalışan uygulayıcıların ihtiyaçları doğrultusunda uygulayıcılar tarafından geliştirilmiş ücretsiz bir yazılımdır.  En az iki güncel uyarlamanın yapılması planlanmıştır.  İlk uyarlama/ güncellemenin 2019 başında yapılması hedeflenmiştir.  Kullanıcılardan gelen öneriler ve alınan izinler doğrultusunda ikinci uyarlamada test listesi içeriğinde değişiklik yapılabilir.  Bazı durumlarda ikinci uyarlamanın beta (ön) hali deneme amaçlı kullanıcılara açılabilir.  Deneme amaçlı kullanım ile ilgileniyorsanız demans.org sitesini takip ediniz.

8."Test verilerini girdikten sonra fark ettim ki bir testin sonucunu yanlış yazmışım.  En baştan mı başlamam gerekiyor?"

Eğer 22 komutu verilmiş ise o katılımcı için sonuç dosyası oluşturulmuş demektir.  Bu durumda aynı katılımcı için tekrar katılımcı bilgileri de dahil olmak üzere sonuç girişi yapmanız gerekmektedir.  Eğer 22 komutu verilmemiş ise, söz konusu katılımcı için hala veri girilebilir, yanlış girilen veri düzeltilebilir.  Bu durumda yanlış sonuç girilen testi tekrar seçerek doğru veriyi girebilirsiniz.  Lütfen unutmayın; bir katılımcı için 22 komutu verilmeden önce aynı test için tekrar veri girişi yaparsanız ilk girdiğiniz veriler silinecektir.

9."Hastam 95 yaşında.  PsiNorm bu testler için bana sonuç veriyor dolayısıyla testlerin bu yaş grubu normları var mı?"  

Norm çalışmalarında ilgili değişken için hangi aralık kullanıldıysa PsiNorm hesaplamaları o aralığa göre yapmaktadır.  Ancak hastaya özgü değerler norm aralığının dışında ise (bu örnekte yaş), hesaplama hastanın özelliklerine en yakın gruba göre yapılır.  Dolayısıyla test için belirlenen norm aralığında yaş için üst değer 80 ise yazılım 90 yaşındaki hastanın hesaplamasını 80 yaşa göre yapmaktadır.     

10."Hastam hiç eğitim görmemiş.  PsiNorm bu testler için bana sonuç veriyor dolayısıyla tüm testlerin bu eğitim seviyesi için normları var mı?"

Norm çalışmalarında ilgili değişken için hangi aralık kullanıldıysa PsiNorm hesaplamaları o aralığa göre yapmaktadır.  Ancak hastaya özgü değerler norm aralığının dışında ise (bu örnekte eğitim), hesaplama hastanın özelliklerine en yakın gruba göre yapılır.  Dolayısıyla test için belirlenen norm aralığında eğitim için alt değer 5 ise yazılım hiç örgün eğitim görmemiş (0 sene eğitim görmüş) hastanın hesaplamasını 5 seneyi esas alarak yapmaktadır.     

11."Programın çıkardığı raporda Z skorlarının yanında * sembolü görüyorum, anlamı nedir?"

PsiNorm yazılımı kullanıcıya klinik olarak anlamlı sonuçlar vermek adına puanı yükseldikçe kötüleşen testlerin Z skorlarını "-1" ile çarpmaktadır. Bu sayede olgunun bulunduğu persentil, olgunun skorları kötüleştikçe sola kaymaktadır (pratikte alışıldığı üzere.).

""",

    "about_data": """HAKKINDA
2017© Bilal Bahadır Akbulut, Yavuz Ayhan.  
Katkıda bulunanlar: Sirel Karakaş, Emel Erdoğan Bakar, Elvin Doğutepe Dinçer (Neurometrika-Tech); Duygu Çap, Ceren Şimşek, Berge Velibaşoğlu; Enes Çömez.  

1.	PsiNorm yazılımı uygulayıcı tarafından girilen içeriği kontrol etmemektedir.  İçerik sayısal olarak uygun olmasa dahi hesaplama yapılmakta ve uygulayıcıya sonuç verilmektedir.  Lütfen girişin doğru yapıldığına emin olunuz. 

2.	PsiNorm yazılımı sonuçları işlenirken tarih ve saat bilgilerini otomatik olarak kaydetmektedir.  Lütfen bilgisayarınızın saatinin güncel olduğundan emin olunuz.

3.	PsiNorm, alanda çalışan uygulayıcıların ihtiyaçları doğrultusunda geliştirilmiş ücretsiz bir yazılımdır.    Sonraki uyarlamalarda yazılımın daha iyi hale getirilmesi için uygulayıcıların katkı ve önerilerini gerekli görüyoruz.  Lütfen öneri ve eleştirilerinizi b.bahadirakbulut@gmail.com adresine yazınız.   

4.	Çok basamaklı kalite kontrol aşamalarından geçse de uygulayıcı PsiNorm'da hatalar fark edebilir.  Hata fark ettiğiniz hususları lütfen b.bahadirakbulut@gmail.com adresine bildiriniz.  Maddi hatalar mümkün olduğunca hızlı şekilde ele alınacaktır.

5.	PsiNorm kullanılarak yapılan akademik çalışmalarınızda PsiNorm'a atıfta bulunmanız gerekmektedir.  Lütfen atıfta bulunulacak çalışma için demans.org websitesini takip ediniz.

6.	Bir sorunuz olduğunda lütfen Sık Sorulan Sorular bölümünü kontrol ediniz.  Sık Sorulan Sorulara giriş ekranından ulaşabilirsiniz.  Bu kısımda sorunuza yanıt bulamazsanız b.bahadirakbulut@gmail.com adresine yazınız.  Sizinle 10 iş günü içinde iletişime geçilmeye çalışılacaktır.

7. PsiNorm yazılımı kaynaklarda verilen çalışmalar esas alınarak hazırlanmıştır, dolayısıyla yazılım sonuçları yalnız kaynaklardaki testler için geçerlidir, başka uyarlamalar için kullanılamaz.  Testler ile ilgili detaylı bilgi ve norm tabloları için lütfen ilgili kaynağa ulaşınız.
""",

    "references_data":"""===================================================================                
ÖNEMLİ UYARILAR:
    
1) Testlerde hastaya özgü norm değerleri bulunmadığında, z-skorları hastanın özelliklerine en yakın gruba göre hesaplanmıştır.
Limitleri olan testler aşağıdaki şekildedir:
    
 > 3MS Eğitim < 5 VE Yaş < 65 VE Erkek
   3MS tüm gruplarda Yaş < 55

 > Görsel İşitsel Sayı Dizileri: 13 <= Yaş

 > Sözel Bellek Süreçleri: 15 <= Yaş VEYA Eğitim <= 19

 > Rey Karmaşık Figür: 17 <= Yaş <= 82

 > İz sürme: 20 <= Yaş

 > Stroop: 5 <= Eğitim <= 8 VE 20 <= Yaş <=74
           8 <= Eğitim VE 20 <= Yaş <= 82

 > Yetişkin Wisconsin Kart Eşleme: 5 <= Eğitim VE 20 <= Yaş <= 72
                                   12 <= Eğitim VE 20 <= Yaş <= 78

 > Görsel Sözel test: 20 <= Yaş <= 100
 
 > Renkli İz Sürme: 20 <= Yaş <= 100
 
 > Sözel Akıcılık: 5 <= Eğitim VEYA 15 <= Yaş
 
 > Semantik Akıcılık: 5 <= Eğitim VEYA 15 <= Yaş
 
 > Çizgi Yönünü Belirleme: 5 <= Eğitim <= 8 VE 20 <= Yaş <= 74
                           9 <= Eğitim <= 11 VE 20 <= Yaş <= 76
                           12 <= Eğitim VE 20 <= Yaş <= 73

2) Testlerin sonuçlarında bildirilen yorumlar, normalin 1 standart deviasyon(SD) uzağı normal,
1-2 SD aralığı hafif bozulma, 2-3 SD aralığı orta derecede bozulma, 3 SD'den uzakta olan 
sonuçlar ağır derecede bozulma olarak belirtilmiştir.

3) Benton Yüz Tanıma Testi için, testin orijinal normları matematiksel modele uyarlamak açısından değiştirilmiştir.
    Yani:
        Düşük Eğitim Grubu = 0-7 yıl (Orijinali ile aynı)
        Orta Eğitim Grubu = 8-12 yıl 
        Yüksek Eğitim Grubu = 13+ yıl 
    olarak belirlenmiştir. Yani program yüksek öğretimi yarıda bırakma durumunu göz ardı etmektedir.

===================================================================
Kaynakça:
    
> Ayhan Y., Saka E., Bariskin E., Bilir N., Karahan S., Caman O. ADAPTATION OF THE MODIFIED MINI-MENTAL STATE (3MS) EXAM, DEVELOPMENT OF A VERSION FOR THE UNDEREDUCATED, AND DETERMINATION OF NORMATIVE VALUES IN THE TURKISH POPULATION, Alzheimer's & Dementia 2017 vol: 13 (7) pp: P1561-P1562 DOI: 10.1016/j.jalz.2017.07.711

> Cangoz, B., Karakoc, E., & Selekler, K. (2009). Trail Making Test: normative data for Turkish elderly population by age, sex and education. J Neurol Sci, 283(1-2), 73-78. doi: 10.1016/j.jns.2009.02.313

> Cangöz B, Karakoc E., Selekler K (2006). Saat Çizme Testi'nin Türk yetişkin ve yaşlı örneklemi üzerindeki norm belirleme, geçerlik ve güvenirlik çalışmaları. Türk Geriatri Dergisi, 9 (3), 136-142. 

> Gungen C, Ertan T, Eker E, Yasar R, Engin F. (2002). Standardize Mini Mental Test’in Türk Toplumunda Hafif Demans Tanisinda Geçerlik ve Güvenilirliği. Türk Psikiyatri Dergisi 13(4):273-281

> Karakaş S., Erdoğan Bakar E., Doğutepe Dinçer E. (2013). BİLNOT Bataryası El Kitabı: Nöropsikolojik Testlerin Yetişkinler için Araştırma ve Geliştirme Çalışmaları: BİLNOT- Yetişkin (Cilt I-II). Konya: Eğitim Yayınevi

> Keskinkilic C. (2008). Standardization of Benton Face Recognition Test in a Turkish Normal Adult Population. Turkish Journal of Neurology, 14(3), 179-190.

> Keskinoglu P., Ucku R., Yener G., Yaka E., Kurt P., & Tunca Z. (2009). Reliability and validity of revised Turkish version of Mini Mental State Examination (rMMSE-T) in community-dwelling educated and uneducated elderly. Int J Geriatr Psychiatry, 24(11), 1242-1250. doi: 10.1002/gps.2252

> Kudiaki C., & Aslan A. (2008). Executive functions in a Turkish sample: associations with demographic variables and normative data. Appl Neuropsychol, 15(3), 194-204. doi: 10.1080/09084280802324416

> Kurt, M., Can H., Karakaş S. (2016). Boston Adlandırma Testi Türk Formu için araştırma-geliştirme çalışması. Yeni Sempozyum, 54(1), 6-14. doi:10.5455/NYS.2016001.

> Saka E., Mihci E., Topcuoglu M. A., & Balkan S. (2006). Enhanced cued recall has a high utility as a screening test in the diagnosis of Alzheimer's disease and mild cognitive impairment in Turkish people. Arch Clin Neuropsychol, 21(7), 745-751. doi: 10.1016/j.acn.2006.08.007

> Selekler K. C., B, Uluç S. (2010). Montreal Bilişsel Değerlendirme Ölçeği'nin (MOBİD) Hafif Bilişsel Bozukluk ve Alzheimer Hastalarını ayırdedebilme gücünün incelenmesi. Türk Geriatri Dergisi, 13(3), 166-171. 

> Tanor O. (2006). Öktem Sözel Bellek Süreçleri Testi. Ankara: Türk Psikologlar Derneği.

> Turkes N.,Can H., Kurt M., Dikeç BE. (2015). İz Sürme Testi’nin 20-49 Yaş Aralığında Türkiye İçin Norm Belirleme Çalışması. Türk Psikiyatri Dergisi; 2015;26(3):189-196

> Teng E. L., & Chui H. C. (1987). The Modified Mini-Mental State (3MS) examination. J Clin Psychiatry, 48(8), 314-318. 

> Varan E, Tanor O, Gurvit H (2007) Rey Karmaşık Figür Testi ve Tanıma Uygulaması (RKFT-T): Bir Yetişkin Türk Örneklemi Üzerinde Norm Belirleme Çalışması.  Turk J Neurol. 2007; 13(6): 387-394

> Yıldız GB, Özçelik EU, Kolukısa M, Işık AT, Gürsoy E, Kocaman G, Çelebi A (2016). Eğitimsizler İçin Modifiye Edilen Mini Mental Testin (MMSE-E) Türk Toplumunda Alzheimer Hastalığı Tanısında Geçerlik ve Güvenilirlik Çalışması. Türk Psikiyatri Dergisi, 27(1):41-46

===================================================================
                """
        
        }

    
import json
with open('info_data.json', 'w', encoding='utf8') as fp:
    json.dump(info_data, fp, sort_keys=False, indent=4, ensure_ascii=False)

#import json
#with open('test3msDataDict.json', 'w', encoding='utf8') as fp:
#    json.dump(test3msDataDict, fp, sort_keys=False, indent=4, ensure_ascii=False)

#class MyException(Exception):
#    """Raise for my specific kind of exception"""
#raise MyException()