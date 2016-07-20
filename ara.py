import webbrowser

adres = "www.google.com.tr/search?num=20&newwindow=1&site=&source=hp&q="
adres2 = "http://www.bing.com/search?q="
adres3 = "https://yandex.com.tr/search/?text="
adres4 = "https://search.yahoo.com/?p="
adres5 = "https://duckduckgo.com/?q="
adres6 = "https://tr.wikipedia.org/w/index.php?search="

while True:
    new = 2

    arama = input("Arama: ")

    adres += arama
    adres2 += arama
    adres3 += arama
    adres4 += arama
    adres5 += arama
    adres6 += arama

    webbrowser.open(adres,new=new)
    webbrowser.open(adres2,new=new)
    webbrowser.open(adres3,new=new)
    webbrowser.open(adres4,new=new)
    webbrowser.open(adres5,new=new)
    webbrowser.open(adres6,new=new)

    print("Arama işlemi gerçekleştirildi. :-)")
