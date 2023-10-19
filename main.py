import random

print("~~~足し算プログラム~~~")
count = 1
while True:

    if count > 3:
        print("お疲れ様でした！")
        break
    else:
        print(f"【{count}問目】")

    num_a = random.randint(1, 100)
    num_b = random.randint(1, 100)
    res = int(input(f"問題「{num_a} + {num_b} = ?」: "))

    if res == num_a + num_b:
        print("正解！")
        count += 1
    else:
        print("不正解！")
        break