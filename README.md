# ♻️ Geri Dönüşüm Asistanı Discord Botu

Evdeki atık miktarını azaltmak isteyen ancak nereden başlayacağını bilmeyen yetişkin bireyler için geliştirilmiş çevreci bir Discord botudur
Geri dönüşüm bilgisi verir yapay zekâ ile sade ve uygulanabilir öneriler sunar.

---

## 🚀 Özellikler

- 🧠 Yerel çalışan LLaMA3 modeli (Ollama) ile entegre yapay zekâ desteği
- ♻️ Atık türlerine özel geri dönüşüm bilgisi (`!atik`)
- 💬 Kullanıcıdan gelen sorulara akıllı öneriler (`!soru`)


---

## 🔧 Kurulum

### 1. Gerekli Python Paketleri

Aşağıdaki komutla gerekli kütüphaneleri kur:

```bash
pip install discord.py
pip install requests
```


### 2. Ollama Kurulumu (Yapay Zekâ İçin)

Bu botun yapay zekâ kısmı, bilgisayarınızda yerel olarak çalışan **LLaMA3 modeli** ile çalışır.  
Bu modelin çalışması için **Ollama** adlı uygulamayı kurmanız gerekir.

#### 🔽 3.1 Ollama Nasıl İndirilir?

- Ollama’nın resmi sitesi: [https://ollama.com](https://ollama.com)
- Buradan işletim sisteminize göre indirip kurun:
  - Windows için `.exe`
  - macOS için `.pkg`
  - Linux için terminal kurulum komutları var (sitede belirtiliyor)
.

#### 🧠 3.2 LLaMA3 Modelini Yükle ve Çalıştır

Botun doğru şekilde çalışabilmesi için şu komutu girin:

```bash
ollama run llama3
```

Bu komut:
- LLaMA3 modelini indirir (4 GB)


#### ✅ Her Şey Yolundaysa

Sunucu şurada aktif olur:  
**http://localhost:11434**

Bot, bu adrese bağlanıp cevapları buradan alır.

---

### 4. Botu Başlat

Her şey hazırsa terminale şu komutu yaz:

```bash
python main.py
```

Artık bot Discord sunucunuzda aktif hale gelir ve komutlara cevap verir.

---

## 💬 Komutlar

| Komut         | Açıklama                                                                 |
|---------------|--------------------------------------------------------------------------|
| `!atik <ürün>` | Ürünün doğada çözülme süresi ve hangi kutuya atılması gerektiğini söyler |
| `!soru <soru>` | Yapay zekâ ile çevreye duyarlı yaşam önerisi alırsın                    |

---

## 🤖 Yapay Zekâ Rolü

Botun yapay zekâ kısmı şu kişilikle çalışır:

> "Sen evde ürettiği atık miktarını azaltmak isteyen ancak nereden başlayacağını bilmeyen yetişkin bireylere yardımcı olan bir çevre dostu asistansın. Cevaplarını sade, uygulanabilir ve cesaretlendirici şekilde ver."

---

