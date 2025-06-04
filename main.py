import discord
from discord.ext import commands
from botsifre import sifreolustur
import random
import os
import requests
from deep_translator import GoogleTranslator

ingilizce_cumle = "A plastic bottle takes about 450 years to decompose."
turkce_ceviri = GoogleTranslator(source='en', target='tr').translate(ingilizce_cumle)
ingilizce_ceviri=GoogleTranslator(source='tr', target='en').translate(ingilizce_cumle)

print(turkce_ceviri)

intents = discord.Intents.default()
intents.message_content = True
intents.members=True
bot = commands.Bot(command_prefix='$', intents=intents)

def ollama_cevap(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "phi3",
        "prompt": "Sen evde ürettiği çöp miktarını azaltmak isteyen ancak nereden başlayacağını bilemeyen yetişkin bireylere yardımcı olan bir geri dönüşüm ve sürdürülebilir yaşam asistanısın en fazla 2000 karakter kullan "+prompt,
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()["response"]

geri_donusum_bilgisi = {
    "plastik şişe": ("Plastik geri dönüşüm kutusuna atılmalı", "450 yıl"),
    "cam şişe": ("Cam geri dönüşüm kutusuna atılmalı", "1 milyon yıl"),
    "alüminyum kutu": ("Metal geri dönüşüm kutusuna atılmalı", "200-500 yıl"),
    "gazete": ("Kağıt geri dönüşüm kutusuna atılmalı", "6 hafta"),
    "pil": ("Tehlikeli atık kutusuna atılmalı.", "Hiç çözünmez, çevreye çok zararlıdır."),
    "yemek artığı": ("Organik atık kutusuna atılmalı.", "1-2 hafta"),
    "kırık cam bardak": ("Evsel atığa atılmalı, cam geri dönüşüme uygun değildir.", "1 milyon yıl"),
    "peçete": ("Organik çöpe atılmalı.", "2-4 hafta"),
    "plastik poşet": ("Geri dönüşüm kutusuna atılabilir, tekrar kullanılmalı.", "10-1000 yıl")
}


@bot.command()
async def atik(ctx, *,urun):
    urun = urun.lower()
    
    if urun in geri_donusum_bilgisi:
        bilgi, sure = geri_donusum_bilgisi[urun]
        await ctx.send(f"{urun.title()} {bilgi} Doğada yok olma süresi: {sure}")
    else:
        await ctx.send("Bu ürün için veri bulunamadı daha genel bir isimle tekrar deneyin")

@bot.command()
async def soru(ctx, *,cevap):
    cevap=cevap.lower()
    ingilizce_cevap=GoogleTranslator(source='tr', target='en').translate(cevap)
    cevap_bot=ollama_cevap(ingilizce_cevap)
    turkce_cevap = GoogleTranslator(source='en', target='tr').translate(cevap_bot)
    await ctx.send(turkce_cevap)


bot.run("")
