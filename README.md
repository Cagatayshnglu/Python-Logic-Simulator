# Dijital Mantık Devre Simülatörü

Bu proje, Python ve PyQt6 kütüphanesi kullanılarak geliştirilmiş bir dijital mantık devre simülatörüdür. Elektrik-Elektronik Mühendisliği öğrencilerinin dijital tasarım derslerinde öğrendikleri kavramları görsel ve interaktif bir ortamda pekiştirmeleri için tasarlanmıştır.

## ✨ Özellikler

-   **Geniş Kapı Desteği:** AND, OR, NOT, NAND, NOR, XOR kapıları.
-   **İnteraktif Arayüz:** Menü üzerinden kolayca kapı ekleme ve tuval üzerinde serbestçe sürükleme.
-   **Görsel Pinler:** Her kapı üzerinde mantıksal bağlantılar için giriş ve çıkış pinleri bulunur.
-   **Profesyonel Kod Yapısı:** Nesne Yönelimli Programlama (OOP) prensiplerine uygun olarak `main.py` ve `gates.py` dosyalarına ayrılmış temiz kod.

## 🚀 Kurulum ve Çalıştırma

1.  Proje dosyalarını klonlayın veya indirin.
2.  Gerekli kütüphaneyi yükleyin:
    ```bash
    pip install PyQt6
    ```
3.  Ana betiği terminal üzerinden çalıştırın:
    ```bash
    python main.py
    ```
4.  Açılan pencerede "Kapı Ekle" menüsünü kullanarak simülasyona başlayın!

## 🔧 Gelecek Geliştirmeler

Projenin bir sonraki aşamasında aşağıdaki özelliklerin eklenmesi planlanmaktadır:

-   [ ] **Kablo Çizme:** Pinler arasına fare ile kablo çekme ve bağlama özelliği.
-   [ ] **Mantıksal Simülasyon:** Devrenin girişlerine göre çıkışlarının gerçek zamanlı olarak hesaplanması.
-   [ ] **Giriş/Çıkış Elemanları:** Değeri değiştirilebilen "Toggle Switch" (Giriş) ve durumu gösteren "LED" (Çıkış) elemanları.
-   [ ] **Devreyi Kaydet/Yükle:** Tasarlanan devreyi bir dosyaya kaydedip daha sonra geri yükleme.
