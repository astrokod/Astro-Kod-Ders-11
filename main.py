import p5
# bu kütüphaneyi kurmak için:
# pip install p5

# Konum ve Hız değişkenlerinin oluşturulması
x, y = 0, 0
v_x, v_y = 0, 0

# Yarışçap değişkeninin oluşturulması
r = 25


# p5 çalıştırıldığında başlangıç olarak bu fonksiyonu çalıştırır.
# Bir defalığına çalıştırır.
def setup():
    # Global scope'ta oluşturulan değişkenlerin
    # değiştirilebilmesi için global anahtar kelimesi kullanılır
    global x, y, v_x, v_y
    # 800x400'lük bir pencere oluştur
    p5.size(800, 400)
    # x, y koordinatını değiştir
    x, y = 400, 200
    # x ve y yönündeki hız değerlerini değiştir
    v_x, v_y = 5, 7


# Frame her yenilendiğinde uygulanacak fonksiyon
def draw():
    # Global scope'ta oluşturulan değişkenlerin
    # değiştirilebilmesi için global anahtar kelimesi kullanılır
    global x, y, v_x, v_y

    # Arka alanı siyah yap
    p5.background(255, 0, 0)

    # Oluşturacağım nesnenin içini yeşil yap
    p5.fill(0, 255, 0)
    # Oluşturacağım nesnenin etrafına çizgi çizme
    p5.no_stroke()
    # x, y Koordinatında 20x20'lik bir kare çiz
    p5.rect((x, y), 20, 20)

    # x, y Koordinatında r çapında bir daire çiz
    # p5.circle((x, y), r)

    # x ve y yönündeki hız değerlerini sırasıyla x ve y yönündeki konuma ekle
    x += v_x
    y += v_y

    # Eğer x koordinatı yarıçaptan küçük veya genişlik - yarıçaptan büyük ise
    # x yönündeki hızın yönünü değiştir
    if x <= r / 2 or x >= 800 - r / 2:
        v_x *= -1

    # Eğer y koordinatı yarıçaptan küçük veya yükseklik - yarıçaptan büyük ise
    # y yönündeki hızın yönünü değiştir
    if y <= r / 2 or y >= 400 - r / 2:
        v_y *= -1


if __name__ == "__main__":
    # p5'i çalıştır
    p5.run()
