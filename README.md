Proje Raporu: E-Ticaret Web Sitesi Loglarına Dayalı Soru-Cevap Sistemi
1. Proje Tanımı ve Amacı
Bu proje, bir e-ticaret web sitesine ait log verilerini kullanarak kullanıcıların belirli sorularına
otomatik olarak yanıt verebilen bir Soru-Cevap (Q&A) sistemi geliştirmeyi amaçlamaktadır.
Projede, bilgi alma (retrieval) ve yanıt oluşturma (generation) aşamalarını birleştiren RAG
(Retrieval-Augmented Generation) modeli kullanılmıştır. RAG modeli, verilen bir soruya yanıt
oluşturabilmek için önce ilgili bilgileri veri setinden alır ve bu bilgileri kullanarak bir dil modeli
aracılığıyla yanıt üretir.
2. Kullanılan Yöntem ve Araçlar
Proje boyunca izlenen temel adımlar aşağıda özetlenmiştir:
● Veri Yükleme ve Ön İşleme:
○ E-ticaret web sitesi logları pandas kullanılarak yüklendi ve accessed_date
gibi tarih formatındaki sütunlar datetime formatına dönüştürüldü.
○ Eksik değerler "Unknown" olarak dolduruldu ve uygun sütunlar kategorik
verilere dönüştürüldü.
○ Veri seti kaggle üzerinden alınmıştır ve daha kısa compile süresi için %70
oranında küçültülmüştür.
● Metin Verisinin Hazırlanması:
○ Log verilerindeki çeşitli sütunlar (ip, accessed_From, network_protocol,
country, language, pay_method, membership, gender) birleştirilerek,
her log için tek bir metin veri noktası oluşturuldu. Bu metinler, veriyi temsil
eden anlamlı vektörler oluşturmak için kullanıldı.
● Model Seçimi ve Vektörizasyon:
○ sentence-transformers kütüphanesi kullanılarak
msmarco-distilbert-base-tas-b modeli ile metin verisi vektörlere
dönüştürüldü. Bu model, RAG sisteminde bilgi alma aşaması için kullanıldı.
○ Vektörler FAISS kütüphanesi kullanılarak yüksek boyutlu bir uzayda
indekslendi ve en yakın komşular arandı.
● Yanıt Üretimi:
○ Soruya en uygun log girişleri alındıktan sonra, bu bilgiler T5-base dil
modeline verilerek yanıt üretildi. Bu model, yanıtın bağlamla uyumlu olmasını
sağlamak amacıyla eğitilmiş bir transformer modelidir.
3. Karşılaşılan Zorluklar ve Çözüm Yolları
Proje boyunca karşılaşılan en büyük zorluk, dil modeli seçiminde kısıtlı seçeneklerin
olmasıydı. Bilgisayar sistemim, daha güçlü modelleri çalıştırmak için yeterli donanıma sahip
olmadığından, nispeten daha basit ve hafif modeller kullanmak zorunda kaldım. Bu durum,
elde edilen cevapların kalitesini sınırladı. Daha güçlü bir dil modeli kullanabilseydim, elde
edilen sonuçların doğruluğu ve bağlamsal uyumluluğu daha yüksek olabilirdi.
Ek olarak, yanıtların kalitesini artırmak için metin verisinin hazırlanması ve modele sağlanan
bağlamın düzenlenmesi de önemli bir adımdı. Yanıtların doğruluğunu artırmak adına, log
verilerinden daha özet ve hedef odaklı bilgiler çıkararak modelin daha isabetli tahminler
yapmasını sağlamaya çalıştım.
Son olarak RAG ile ilgili hiçbir deneyimimin olmaması nedeniyle teknik olarak zorlandığımı
itiraf edebilirim.
4. Sistem Performansı ve Doğruluk Değerlendirmesi
● Performans: Kullanılan modeller ve yöntemler, mevcut donanım sınırları içinde
oldukça hızlı bir şekilde sonuç verdi. Özellikle msmarco-distilbert-base-tas-b
modeli, log verilerinden hızlı ve ilgili bilgiler alabilmek için uygun bir seçim oldu.
● Doğruluk: Sistem, bazı sorulara doğru ve bağlamla uyumlu yanıtlar verebilse de,
bazı sorularda beklenen doğruluk düzeyini sağlayamadı. Yanıtların kalitesini artırmak
için daha sofistike modeller veya ince ayar yapılmış (fine-tuned) dil modelleri
kullanılabilir. Ben yazdığım her kodu yorum satırı ile anlatmaya çalıştım. NLP ilk defa
denediğim bir alan olduğu için teknik olarak hatalar olmuş olması kuvvetle muhtemel.
5. Sonuç ve Gelecekteki Çalışmalar
Bu proje, veri tabanlı bir Soru-Cevap sistemi geliştirme sürecinde temel bir yaklaşım ve
uygulanabilir bir çözüm sunmaktadır. Gelecekte, daha güçlü dil modelleri ve daha gelişmiş
donanım kullanılarak, sistemin doğruluğunu ve bağlamsal anlamını iyileştirmek mümkün
olacaktır. Ayrıca, kullanıcıların ihtiyaçlarına göre özelleştirilebilecek ve daha çeşitli sorgulara
yanıt verebilecek daha gelişmiş bir Soru-Cevap platformu geliştirilmesi hedeflenebilir. İşte
bazı sorular ve modelin ürettiği cevaplar;
Sonuç olarak, mevcut sistem, veri alma ve yanıt üretimi aşamalarını entegre ederek,
kullanıcıların e-ticaret sitesi loglarından anlamlı bilgiler elde etmelerini sağlamaktadır. Ancak,
daha gelişmiş modellerin entegrasyonu ve daha geniş bir veri kümesi ile bu sistemin
performansı daha da artırılabilir. Görüldüğü üzere sistem bazı sorulara keskin doğru
cevaplar verirken, bazı soruların bağlamını dahi anlamakta güçlük çekiyor. Bu durumu
iyileştirmek için daha güçlü dil modelleri kullanılabilir(T5-Base, GPT3.5 gibi) ve belki daha iyi
vektör optimizasyonu yapılabilirdi.
