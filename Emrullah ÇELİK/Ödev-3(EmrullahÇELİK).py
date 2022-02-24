import requests
import random

# empty list for storing the concataned and sampled items
lst = []

# counter storage to stop the execution
count = 0

while count < 100 :

    # linkten veri çekme
    r = requests.get("https://randomuser.me/api/")

    # json() formatında gelen veriden istenilenleri alma, boşlukları silme, string yapıp küçük harfe çevirme
    name = (str(r.json()["results"][0]["name"]["first"]).replace(" ", "")).lower()
    surname = (str(r.json()["results"][0]["name"]["last"]).replace(" ", "")).lower()
    city = (str(r.json()["results"][0]["location"]["city"]).replace(" ", "")).lower()
    country = (str(r.json()["results"][0]["location"]["country"]).replace(" ", "")).lower()

    # verileri birleştirme
    sentence = name + surname + city + country
    lst_sentence = list(sentence)
   
    # listenin karakterlerinin yerlerini değiştirme
    random.shuffle(lst_sentence)

    # gelen tüm verileri buraya ekleme ve tırnak işaretlerini kaldırma
    lst.append("".join(lst_sentence))
    
    count += 1


print(max(lst, len)) #liste içinden en uzun seçimi yapma