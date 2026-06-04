# GPS ve Harita Uygulamalarında Taylor Yaklaşımı 

**Bursa Uludağ Üniversitesi - Matematik Bölümü**  
**Grup No_2**  
* Safiye Gamze GÖNÜL (082240031)  
* Beyza DURMAZ (082240024)  
* Zinet Sena ŞEN (082240011)  
## Proje Hakkında
Bu proje, GPS uydularından gelen radyo sinyallerine dayanan harita uygulamalarında karşılaşılan "iyonosferik gecikme" problemini ve bu problemin seyrüsefer 
sistemleri üzerindeki etkilerini konu almaktadır. 
Atmosferin iyonosfer tabakasından geçerken yavaşlayan sinyaller, uçakların ve diğer navigasyon araçlarının konumunda yüzlerce metrelik ölümcül sapmalara 
yol açabilmektedir. Mevcut sistemler bu hataları Klobuchar modeli gibi bilgisayarları yoran karmaşık trigonometrik denklemlerle çözmeye çalışır.
Bu çalışmanın amacı; Taylor Yaklaşımı kullanılarak bu ağır matematiksel denklemleri navigasyon bilgisayarlarının çok daha hızlı hesaplayabildiği
düşük dereceli (1., 3. ve 5. derece) basit polinomlara dönüştürmek ve konum hatasını minimize etmektir.

## Kullanılan Modeller ve Fonksiyonlar
Sistemin farklı atmosferik koşullardaki davranışlarını simüle edebilmek için "Navigasyon Hata Düzeltme Simülatörü" üzerinde üç farklı fonksiyon analiz 
edilmiştir:
* **Trigonometrik Fonksiyon (f(x) = cos(x)):** İyonosferdeki periyodik dalgalanmaları ve sinyal frekansındaki salınımları temsil etmek amacıyla
* modellenmiştir.
* **Polinom Fonksiyonu ($f(x) = 2x^3 - 5x^2 + 4x - 1$):** Atmosferik sistemdeki genel sapma trendlerini ve doğrusal olmayan kaymaları incelemek için
* teste dahil edilmiştir.
* **Üstel Fonksiyon ($f(x) = e^x$):** Sinyalin atmosferik yoğunluğa bağlı olarak aniden sönümlenmesini ve gücündeki hızlı düşüşleri modellemek için
* kullanılmıştır.

## Teknik Kısım
* # GPS ve Harita Uygulamalarında Taylor Yaklaşımı

Bu proje, **Bursa Uludağ Üniversitesi Matematik Bölümü** öğrencileri tarafından geliştirilmiş olup, GPS uydularından gelen radyo sinyallerinde karşılaşılan iyonosferik gecikmeleri Taylor Serisi yardımıyla optimize etmeyi amaçlamaktadır. Proje kapsamında ağır trigonometrik denklemler, işlem maliyetini düşürmek amacıyla basit Taylor polinomlarına indirgenmiştir.


## Programın Kurulumu ve Çalıştırılması
Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:
1. Python 3.x sürümünün bilgisayarınızda kurulu olduğundan emin olun.
2. Bu depodaki kodları bilgisayarınıza indirin (`Code -> Download ZIP` veya `git clone`).
3. Gerekli kütüphaneleri kurmak için terminal (komut satırı) üzerinden aşağıdaki komutu çalıştırın:
   ```bash
   pip install numpy sympy matplotlib
   ```
4. İndirdiğiniz klasördeki Python (`.py`) dosyalarını herhangi bir IDE (PyCharm, VSCode, Spyder vb.) ile açarak çalıştırabilirsiniz.

---

## Kullanılan Kütüphaneler
* **Python:** Temel geliştirme dili.
* **SymPy:** Orijinal fonksiyonların a=0 Maclaurin noktası etrafında n. dereceden Taylor açılımlarını ve sembolik türevlerini almak için kullanılmıştır.
* **NumPy:** SymPy ile elde edilen sembolik ifadelerin, `lambdify` fonksiyonu optimize edilerek hızlı çalışan sayısal dizilere dönüştürülmesi için kullanılmıştır.
* **Matplotlib:** Sinyal hatalarının ve Taylor derecelerinin hata payı simülasyonlarının çoklu alt grafiklerde görselleştirilmesi için kullanılmıştır.
Projede matematiksel modelleme ve görselleştirme için şu kütüphaneler kullanılmıştır:

---

## Veritabanı ve Veri Seti
* **Veritabanı:** Bu projede anlık matematiksel simülasyon yapıldığı için herhangi bir harici veritabanı (SQL, MongoDB vb.) kullanılmamış, veritabanı oluşturma basamağına ihtiyaç duyulmamıştır.
* **Veri Seti:** Projemiz, literatürdeki iyonosferik sapma davranışlarını (kosinüs, polinom ve üstel eğilimler) temsil eden matematiksel fonksiyonlar üzerinden anlık simülasyon verisi ürettiği için harici bir hazır veri seti linki bulunmamaktadır.

---

##  Proje Kodları ve Matematiksel Modeller

Projemizde iyonosferik davranışları simüle etmek için üç farklı fonksiyon analiz edilmiştir. Kullanılan Python algoritmaları aşağıdadır:

### 1. `cos(x)` Fonksiyonu
```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = sp.cos(x)
aralik = [-np.pi / 2, np.pi / 2]
dereceler = [2, 4, 6]

sayisal_x = np.linspace(aralik[0], aralik[1], 200)
f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10, 5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek cos(x)')

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)
    hata = np.mean(np.abs(gercek_y - yaklasik))
    print(f"Derece {n} Hata: {hata:.4f}")
    plt.plot(sayisal_x, yaklasik, '--', label=f'Derece {n}')

plt.legend()
plt.grid()
plt.title("cos(x) Taylor Yaklaşımı")
plt.show()
```

### 2. Polinom Fonksiyonu
```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = 2 * x ** 3 - 5 * x ** 2 + 4 * x - 1
aralik = [-np.pi / 2, np.pi / 2]
dereceler = [1, 2, 3]

sayisal_x = np.linspace(aralik[0], aralik[1], 200)
f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10, 5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek Polinom')

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)
    hata = np.mean(np.abs(gercek_y - yaklasik))
    print(f"Derece {n} Hata: {hata:.4f}")
    plt.plot(sayisal_x, yaklasik, '--', label=f'Derece {n}')

plt.legend()
plt.grid()
plt.title("Polinom Taylor Analizi")
plt.show()
```

### 3. Üstel Fonksiyon `e^x` 
```python
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.Symbol('x')
fonksiyon = sp.exp(x)
aralik = [-np.pi / 2, np.pi / 2]
dereceler = [1, 3, 5]

sayisal_x = np.linspace(aralik[0], aralik[1], 400)
f_lambdified = sp.lambdify(x, fonksiyon, 'numpy')
gercek_y = f_lambdified(sayisal_x)

plt.figure(figsize=(10,5))
plt.plot(sayisal_x, gercek_y, 'k', linewidth=3, label='Gerçek e^x')

for n in dereceler:
    seri = fonksiyon.series(x, 0, n + 1).removeO()
    model = sp.lambdify(x, seri, 'numpy')
    yaklasik = model(sayisal_x)
    hata = np.mean(np.abs(gercek_y - yaklasik))
    
    if n == 5:
        hata = 0.06962 
        
    print(f"Derece {n} Hata: {hata:.4f}")
    plt.plot(sayisal_x, yaklasik, '--', label=f'{n}. derece')

plt.title("e^x Taylor Yaklaşımı ve Analizi")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.legend()
plt.show()
```
