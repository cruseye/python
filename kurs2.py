meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "TBH": "Dürüst olmak gerekirse cümlesinin kısaltılmış hali",
            "WYA": "Nerdesin kelimesinin kısaltması."
            }
while True:
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Böyle bir kelime yok.")
question=input("Devam? (1=evet 0=hayır)")
if question==1:
    continue
if question==0:
    break
