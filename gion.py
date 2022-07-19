import random

gion=["れろれろ", "ちゅぱ", "じゅる", "くちゅ", "くぱぁ", "じゅぽ", "ぐにゅ", "・・・"]
x=0
home=""
for i in range(0,50001,1):
    x=random.randint(0,7)
    text=gion[x]
    home= str(home) + str(text)
print(home)