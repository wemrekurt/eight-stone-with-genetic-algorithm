# eight-stone-with-genetic-algorithm
Genetik Algoritması ile sekiz taş problemi çözümü.

## Problem
`N x N` matrise rastgele sırayla dizilmiş ve üzerinde 1'den `(N^2 - 1)`'e kadar numaralar bulunan `(N^2 - 1)` adet taşın matrise doğru sıralama ile dizilmesidir. `N X N` matris üzerinde `(N^2 - 1)` taş ve hareketi sağlayan boş bir kare bulunmaktadır. Amaç ise boş kareye komşu olan taşın boşluğa doğru sağa (r), sola (l), yukarı (t) ve aşağı (b) yönde hareket ettirerek sonuçta doğru dizilimi bulmaktır.

Başlangıç Durumu

| | | |
|-|-|-|
| |6|5|
|4|2|1|
|3|8|7|

Hedef Durum

| | | |
|-|-|-|
|1|2|3|
|4|5|6|
|7|8| |

## Yaklaşım

3x3 matris için 8 taş problemi varsayılacaktır. Taşlar 1-9 şeklinde tanımlanacaktır. 9 numaralı taş boşluk olarak kabul edilecektir. Hareketlere genel olarak baktığımızda aslında boşluğun hareket ettiğini görebiliriz. Dolayısı ile biz de problemi boşluğu hareket ettirerek çözmeye çalışacağız. Boşluğun hareketleri ise Yukarı (T), Aşağı (B), Sola (L) ve Sağa (R) şeklindedir. Boşluğun bir dizi T,B,L ve R hareketleri sonucu doğru dizilişin bulunacağı kabul edilmiştir. Bu dizinin uzunluğu (sırasıyla hareket aşamaları) kromozom uzunluğu olarak tarif edilebilir. Başlangıçta rastgele oluşturulacak kromozomlar `CrossOver` ([Üreme](https://www.wikiwand.com/tr/Mayoz_b%C3%B6l%C3%BCnme)) ve `Mutation` ([Mutasyon](https://www.wikiwand.com/tr/Mutasyon)) ile yeni nesiller üretip, kalıtsal çeşitliliği artıracak, popülasyonu genişletecek ve çözümü bulan uygun dizilime ulaşacaktır.

Aşağıda rastgele seçilmiş 20 birim uzunluğunda bir kromozom örneği bulunmaktadır. Her bir değer `gene` ([Gen](https://www.wikiwand.com/tr/Gen)) olarak isimlendirilir.

|T|L|B|L|L|B|R|L|T|L|B|L|B|T|B|T|B|R|L|L|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

Bu kromozom dizilişi bir bireyi temsil etmektedir. Her bir nesildeki birey sayısı ise popülasyon olarak isimlendirilir. Seçilmiş bir kromozom dizisi algoritmada boşluğun hareketleri olarak 9 numaralı taşa uygulanacaktır.

## Başlangıç Popülasyonu

Başlangıçtaki kromozom tamamen rastgele olarak üretilecektir. Daha sonra popülasyon, kullanıcı tarafından belirlenecek sayıda rastgele kromozomlar üretecektir. Popülasyondaki her bireyin matematiksel olarak uygunluk değeri ölçülecek. Varsayılan olarak 20 birim uzunluğunda kromozomlar seçilmiştir. Değiştirilebilir..

## Mutasyon İşlemi

Kromozomların en iyi değere ulaşabilmesi için mutasyon ile zenginleştirilecektir. 

| | | | | | | | | | | | | | | | | | | | | |
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|Nesil 0-A|T|L|B|L|**L**|B|R|L|T|L|B|L|B|T|B|T|B|R|L|L|
|Nesil 0-A*|T|L|B|L|**R**|B|R|L|T|L|B|L|B|T|B|T|B|R|L|L|

Bu probleme göre bireylerde oluşan bazı gen dizilimleri sorunlu olabilir. Örneğin `N x N` matriste yan yana `N` adet aynı gen gelemez. Aksi taktirde boşluk matrisin dışına çıkar. Yine aynı şekilde Aynı ikili yanyana gelmesi hareketin tekrarı olur. Örneğin `LRLR`. Bu tür hatalı gen dizilimleri mutasyon ile düzeltilecektir.
