import os
import random
os.system('cls')

def sontop():
    tasodifiy_son = random.randint(1, 10)
    print(f"\n🎯 Men 1 dan 10 gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input('🔢 Taxminingiz: '))
        if taxmin < tasodifiy_son:
            print("⬆️  Xato! Men o'ylagan son bundan KATTAROQ. Yana harakat qiling!")
        elif taxmin > tasodifiy_son:
            print("⬇️  Xato! Men o'ylagan son bundan KICHIKROQ. Yana harakat qiling!")
        else:
            break
    print(f"🎉 Tabriklayman! {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc():
    print(f"\n🤖 1 dan 10 gacha son o'ylang. Men topishga harakat qilaman!")
    input("💭 Son o'ylagan bo'lsangiz istalgan tugmani bosing\n>> ")
    quyi = 1
    yuqori = 10
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(
            f'\n🤔 Siz [{taxmin}] sonini o\'yladingizmi?\n'
            f"   ✅ To'g'ri        → t\n"
            f'   ⬆️  Kattaroq      → +\n'
            f'   ⬇️  Kichikroq     → -\n'
            f'>> '
        ).lower()
        if javob == '+':
            quyi = taxmin + 1
        elif javob == '-':
            yuqori = taxmin - 1
        else:
            break
    print(f'🤖 Men {taxminlar} ta urinishda topdim!')
    return taxminlar

def play():
    print("=" * 40)
    print("🎮  SON TOPISH O'YINI  🎮")
    print("=" * 40)
    yana = True
    while yana:
        os.system('cls')
        print("\n" + "─" * 40)
        user_taxmin = sontop()
        pc_taxmin = sontop_pc()

        print("\n" + "=" * 40)
        print(f"📊 NATIJA:")
        print(f"   👤 Siz    : {user_taxmin} ta urinish")
        print(f"   🤖 Komputer: {pc_taxmin} ta urinish")
        print("=" * 40)

        if user_taxmin > pc_taxmin:
            print("😢 Afsuski, yutqizdingiz!")
        elif user_taxmin < pc_taxmin:
            print("🏆 Tabriklayman, Siz yutdingiz!")
        else:
            print("🤝 Durrang!")

        print("─" * 40)
        yana = int(input("🔄 Yana o'ynaysizmi?  Ha(1)  Yo'q(0): "))

    print("\n👋 O'yin tugadi. Xayr!")

play()