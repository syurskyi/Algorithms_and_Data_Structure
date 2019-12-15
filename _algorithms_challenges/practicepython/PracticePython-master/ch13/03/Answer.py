import random

member = ["花媽", "花橘子", "花柚子", "花爸"]
housework = ["掃地", "拖地", "洗衣服", "擦窗戶"]

for i in range(4):
    m = random.choice(member)
    h = random.choice(housework)
    print(m,h)

#沒說家事不可重複
