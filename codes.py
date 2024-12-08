#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 19:38:18 2024

@author: emredikici
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Veri setini yükleyin
file_path = 'Etkinlik geri bildirimi.csv'  # Dosya yolunuzu güncelleyin
data = pd.read_csv(file_path)

# Kolon adlarını temizleyin
data.columns = data.columns.str.strip().str.replace('\n', ' ')

# Görselleştirme için genel stil ayarları
sns.set_theme(style="whitegrid")
plt.rcParams.update({'axes.titlesize': 14, 'axes.labelsize': 12, 'xtick.labelsize': 10, 'ytick.labelsize': 10})

# Grafik 1: Yaş Aralığına Göre Katılım Dağılımı
age_distribution = data['Yaş Aralığınız'].value_counts()
colors = sns.color_palette('pastel', len(age_distribution))

plt.figure(figsize=(8, 6))
plt.pie(age_distribution, labels=age_distribution.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Yaş Aralığına Göre Katılım Dağılımı", fontsize=16)
plt.show()

# Grafik 2: Kullanıcı Dostu Bulma Derecesi Dağılımı
plt.figure(figsize=(8, 6))
sns.countplot(
    data=data,
    x='Uygulamayı genel olarak ne kadar kullanıcı dostu buluyorsunuz? (1: Hiç kullanıcı dostu değil - 5: Çok kullanıcı dostu)',
    palette="Blues",
)
plt.title("Kullanıcı Dostu Olma Derecesi Dağılımı", fontsize=16)
plt.xlabel("Kullanıcı Dostu Derecesi (1-5)")
plt.ylabel("Kişi Sayısı")
plt.show()

# Grafik 3: Tasarımı Değerlendirme Dağılımı
plt.figure(figsize=(8, 6))
sns.countplot(
    data=data,
    x='Tasarımı nasıl değerlendirirsiniz? (1: Beğenmedim - 5: Çok beğendim)',
    palette="Greens",
)
plt.title("Tasarımı Değerlendirme Dağılımı", fontsize=16)
plt.xlabel("Tasarım Beğeni Derecesi (1-5)")
plt.ylabel("Kişi Sayısı")
plt.show()

# Grafik 4: Hız ve Performans Değerlendirmesi
plt.figure(figsize=(8, 6))
sns.countplot(
    data=data,
    x='Uygulamanın hızını ve performansını nasıl buldunuz? (1: Çok yavaş - 5: Çok hızlı)',
    palette="Oranges",
)
plt.title("Hız ve Performans Değerlendirmesi", fontsize=16)
plt.xlabel("Hız ve Performans Derecesi (1-5)")
plt.ylabel("Kişi Sayısı")
plt.show()

# Grafik 5: Şifre Güvenliği Hissi Dağılımı
security_feeling = data['Uygulama size şifrelerinizin güvende olduğunu hissettiriyor mu?'].value_counts()
colors = sns.color_palette('pastel', len(security_feeling))

plt.figure(figsize=(8, 6))
plt.pie(security_feeling, labels=security_feeling.index, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Şifre Güvenliği Hissi Dağılımı", fontsize=16)
plt.show()
