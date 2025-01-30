from PIL import Image, ImageDraw, ImageFont

# Metni tanımla
text = "pillow güzel bir program. python paketi."

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 200), "white")

# Resme yazı yazmak için bir çizim nesnesi oluştur
draw = ImageDraw.Draw(image)

# Font ayarları (Varsayılan font kullanılıyor, isterseniz başka bir font dosyası da kullanabilirsiniz)
font = ImageFont.load_default()

# Satırlara metni bölelim (maksimum 8 karakter uzunluğunda)
max_line_length = 8
lines = []
current_line = ""
for word in text.split():
    if len(current_line + word) <= max_line_length:
        current_line += (word + " ")
    else:
        lines.append(current_line.strip())
        current_line = word + " "
if current_line:
    lines.append(current_line.strip())

# Metni yazdırmaya başlamadan önce, yazının konumunu hesapla
line_height = font.getbbox("A")[3] + 5  # Her satır arasındaki boşluk
text_width = max([draw.textbbox((0, 0), line, font=font)[2] for line in lines])
text_height = line_height * len(lines)

# Dikdörtgenin boyutları
rect_x0 = 50
rect_y0 = 50
rect_x1 = rect_x0 + text_width + 10  # Kenarlardan boşluk bırakmak için +10
rect_y1 = rect_y0 + text_height + 10

# Kırmızı kenarlı dikdörtgeni çiz
draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], outline="red", width=3)

# Metni dikdörtgenin içine yaz
y_position = rect_y0 + 5  # Başlangıç y konumu (üstten biraz aşağı)
for line in lines:
    draw.text((rect_x0 + 5, y_position), line, font=font, fill="black")
    y_position += line_height

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("pillow_text_with_box.png")



from PIL import Image, ImageDraw, ImageFont

# Metni tanımla
text = "pillow güzel bir program. python paketi."

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (500, 200), "white")

# Resme yazı yazmak için bir çizim nesnesi oluştur
draw = ImageDraw.Draw(image)

# Font ayarları (Varsayılan font kullanılıyor, isterseniz başka bir font dosyası da kullanabilirsiniz)
font = ImageFont.load_default()

# Satırlara metni bölelim (maksimum 12 karakter uzunluğunda)
max_line_length = 12
lines = []
current_line = ""
for word in text.split():
    if len(current_line + word) <= max_line_length:
        current_line += (word + " ")
    else:
        lines.append(current_line.strip())
        current_line = word + " "
if current_line:
    lines.append(current_line.strip())

# Metni yazdırmaya başlamadan önce, yazının konumunu hesapla
line_height = font.getbbox("A")[3] + 5  # Her satır arasındaki boşluk
text_width = max([draw.textbbox((0, 0), line, font=font)[2] for line in lines])
text_height = line_height * len(lines)

# Dikdörtgenin boyutları
rect_x0 = 50
rect_y0 = 50
rect_x1 = rect_x0 + text_width + 10  # Kenarlardan boşluk bırakmak için +10
rect_y1 = rect_y0 + text_height + 10

# Kırmızı kenarlı dikdörtgeni çiz
draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], outline="red", width=3)

# Metni dikdörtgenin içine yaz
y_position = rect_y0 + 5  # Başlangıç y konumu (üstten biraz aşağı)
for line in lines:
    draw.text((rect_x0 + 5, y_position), line, font=font, fill="black")
    y_position += line_height

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("pillow_text_with_box_12chars_per_line.png")



from PIL import Image, ImageDraw, ImageFont

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 400), "white")

# Resme yazı yazmak için bir çizim nesnesi oluştur
draw = ImageDraw.Draw(image)

# Üçgenin koordinatlarını belirleyelim
triangle_points = [(200, 50), (50, 350), (350, 350)]

# Üçgenin kenarlarını kırmızı çizeceğiz
draw.polygon(triangle_points, outline="red", fill=None)

# Üçgeni 5 eşit yüksekliğe ayıralım
triangle_height = 300  # Üçgenin yüksekliği
region_height = triangle_height / 5

# 5 bölgeyi çizelim
for i in range(1, 5):
    y = 50 + i * region_height
    draw.line([(50, y), (350, y)], fill="blue", width=1)

# En alt bölgeye "Fizyolojik İhtiyaçlar" yazalım
font = ImageFont.load_default()
draw.text((140, 330), "Fizyolojik İhtiyaçlar", font=font, fill="black")

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("maslow_triangle.png")


from PIL import Image, ImageDraw, ImageFont

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 400), "white")

# Resme yazı yazmak için bir çizim nesnesi oluştur
draw = ImageDraw.Draw(image)

# Üçgenin koordinatlarını belirleyelim
triangle_points = [(200, 50), (50, 350), (350, 350)]

# Üçgenin kenarlarını kırmızı çizeceğiz
draw.polygon(triangle_points, outline="red", fill=None)

# Üçgeni 5 eşit yüksekliğe ayıralım
triangle_height = 300  # Üçgenin yüksekliği
region_height = triangle_height / 5

# 5 bölgeyi çizelim (mavi çizgilerle)
for i in range(1, 5):
    y = 50 + i * region_height
    draw.line([(50, y), (350, y)], fill="blue", width=1)

# Metinleri her bölgeye ekleyelim
font = ImageFont.load_default()

# Alt sıradaki metin: Fizyolojik İhtiyaçlar
draw.text((140, 330), "Fizyolojik İhtiyaçlar", font=font, fill="black")

# İkinci sıradaki metin: Güvenlik İhtiyaçları
draw.text((120, 265), "Güvenlik İhtiyaçları", font=font, fill="black")

# Üçüncü sıradaki metin: Sevgi, Aidiyet
draw.text((120, 200), "Sevgi, Aidiyet", font=font, fill="black")

# Dördüncü sıradaki metin: Saygı
draw.text((140, 135), "Saygı", font=font, fill="black")

# En üst sıradaki metin: Kendini Gerçekleştirme
draw.text((100, 70), "Kendini Gerçekleştirme", font=font, fill="black")

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("maslow_triangle_with_labels.png")

from PIL import Image, ImageDraw, ImageFont

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 400), "white")

# Resme yazı yazmak için bir çizim nesnesi oluştur
draw = ImageDraw.Draw(image)

# Üçgenin koordinatlarını belirleyelim
triangle_points = [(200, 50), (50, 350), (350, 350)]

# Üçgenin kenarlarını kırmızı çizeceğiz
draw.polygon(triangle_points, outline="red", fill=None)

# Üçgeni 5 eşit yüksekliğe ayıralım
triangle_height = 300  # Üçgenin yüksekliği
region_height = triangle_height / 5

# 5 bölgeyi çizelim (mavi çizgilerle)
for i in range(1, 5):
    y = 50 + i * region_height
    draw.line([(50, y), (350, y)], fill="blue", width=1)

# Font ayarları: Daha okunaklı bir font (Arial) kullanıyoruz
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # DejaVu fontunu kullanıyoruz
font = ImageFont.truetype(font_path, 16)  # Yazı boyutunu ayarlayabilirsiniz

# Metinleri her bölgeye ekleyelim (ortalanmış şekilde)
texts = [
    "Kendini Gerçekleştirme",
    "Saygı",
    "Sevgi, Aidiyet",
    "Güvenlik İhtiyaçları",
    "Fizyolojik İhtiyaçlar"  
]

# Yazıları her bölgenin ortasına yerleştirelim
for i, text in enumerate(texts):
    y = 50 + (i + 1) * region_height - region_height / 2  # Y konumu ortalanmış
    bbox = draw.textbbox((0, 0), text, font=font)  # Yeni metod textbbox kullanıldı
    text_width = bbox[2] - bbox[0]  # Metnin genişliği
    text_height = bbox[3] - bbox[1]  # Metnin yüksekliği
    x = (400 - text_width) / 2  # X konumu ortalanmış
    draw.text((x, y - text_height / 2), text, font=font, fill="black")  # Dikeyde de ortalanmış

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("maslow_triangle_with_centered_labels.png")




#Domates resmi 

import matplotlib.pyplot as plt
import numpy as np

# Domatesin gövdesi (kırmızı daire)
fig, ax = plt.subplots()

# Domatesin gövdesini çizen bir daire (kırmızı)
circle = plt.Circle((0.5, 0.5), 0.4, color='red', ec='black', lw=2)

# Sap kısmını çizmek için (yeşil)
stem_x = [0.5, 0.4, 0.6, 0.5]
stem_y = [0.85, 0.95, 0.95, 0.85]

# Domatesin gövdesini ekleyelim
ax.add_artist(circle)

# Sapı ekleyelim
ax.fill(stem_x, stem_y, color='green', ec='black', lw=2)

# Grafik sınırlarını ayarlayalım
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

# Eksenleri kapatalım
ax.axis('off')

# Resmi göster
plt.show()







from PIL import Image, ImageDraw

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 400), "white")

# Resme çizim yapacak bir nesne oluştur
draw = ImageDraw.Draw(image)

# Domatesin gövdesi (kırmızı daire)
draw.ellipse([(100, 100), (300, 300)], fill="red", outline="black")

# Domatesin sapı (yeşil üçgen)
draw.polygon([(180, 100), (220, 100), (200, 60)], fill="green", outline="black")

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("domates_pillow.png")






from PIL import Image, ImageDraw

# Yeni bir resim oluştur (beyaz arka plan)
image = Image.new("RGB", (400, 400), "white")

# Resme çizim yapacak bir nesne oluştur
draw = ImageDraw.Draw(image)

# Dal (kahverengi çizgi)
draw.line([(150, 300), (150, 200)], fill="brown", width=5)

# Elmalar (kırmızı yuvarlaklar)
draw.ellipse([(120, 150), (170, 200)], fill="red", outline="black")  # İlk elma
draw.ellipse([(180, 130), (230, 180)], fill="red", outline="black")  # İkinci elma
draw.ellipse([(100, 100), (150, 150)], fill="red", outline="black")  # Üçüncü elma

# Yapraklar (yeşil elipsler)
draw.ellipse([(130, 170), (180, 220)], fill="green", outline="black")  # İlk yaprak
draw.ellipse([(160, 100), (210, 150)], fill="green", outline="black")  # İkinci yaprak
draw.ellipse([(190, 180), (240, 230)], fill="green", outline="black")  # Üçüncü yaprak

# Resmi göster
image.show()

# Resmi kaydet (isteğe bağlı)
image.save("dalda_3_elma.png")





import networkx as nx
import matplotlib.pyplot as plt

# Kavramlar arasındaki ilişkileri tanımla
G = nx.DiGraph()

# Kavramlar ve ilişkiler
G.add_edge("Kavram 1", "Kavram 2")
G.add_edge("Kavram 1", "Kavram 3")
G.add_edge("Kavram 3", "Kavram 4")
G.add_edge("Kavram 2", "Kavram 5")

# Kavram haritasını çiz
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color="skyblue", font_size=12, font_weight="bold", arrows=True)

# Görselleştir
plt.title("Kavram Haritası")
plt.show()


from graphviz import Digraph

dot = Digraph()
dot.node('GM', 'GENEL MÜDÜR')
dot.node('DB1', 'DAİRE\n BAŞKANI 1')
dot.node('DB2', 'DAİRE BAŞKANI 2')
dot.node('ŞM1', 'ŞUBE MÜDÜRÜ 1')
dot.node('ŞM2', 'ŞUBE MÜDÜRÜ 2')
dot.node('ŞM3', 'ŞUBE MÜDÜRÜ 3')
dot.node('ŞM4', 'Burya Uzun\nBir metin\nyazarsam ne\n Olacak')


dot.edges([('GM', 'DB1'), 
           ('GM', 'DB2'), 
           ('DB1', 'ŞM1'), 
           ('DB1', 'ŞM2'), 
           ('DB2', 'ŞM3'), 
           ('DB2', 'ŞM4')])
dot.render('org_chart', format='png', view=True)


print("Hello, Org Mode!")

import sys
print(sys.executable)

