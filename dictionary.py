dict_uz={
    'salom':('hello','привет'),
    'xayr':('bye','до свидания'),
    'kitob':('book','книга'),
    'daftar':('notebook','тетрадь'),
    'ruchka':('pen','ручка')
}
dict_ru={
    'привет':('hello','salom'),
    'до свидания':('bye','xayr'),
    'книга':('book','kitob'),
    'тетрадь':('notebook','daftar'),
    'ручка':('pen','ruchka')
}
dict_eng={
    'hello':('salom','привет'),
    'bye':('xayr','до свидания'),
    'book':('kitob','книга'),
    'notebook':('daftar','тетрадь'),
    'pen':('ruchka','ручка')
}
print('Men mana shu usullarda tarjima qila olaman:')
print('I can translate in these ways:')
print('Я могу переводить этими способами:')
while True:
    print('1.uz-eng\n2.uz-ru\n3.eng-uz\n4.eng-ru\n5.ru-uz\n6.ru-eng')
    print('Mos sonni tanlang:')
    print('Select the appropriate number:')
    print('Выберите соответствующий номер:')
    a=int(input())
    if a == 1:
        print('uz-eng')
        print("Men shu so'zlarni tarjima qila olaman:")
        for i in dict_uz.keys():
            print(i,end=' ')
        print("\nSo'z kiriting:")
        while True:
            s=input()
            if s in dict_uz.keys():
                break
            else:
                print("Men bu so'zni tarjimasini bilmayman!\nIltimos qaytadan kiriting")
        print(s,'-',dict_uz[s][0])
    elif a == 2:
        print('uz-ru')
        print("Men shu so'zlarni tarjima qila olaman:")
        for i in dict_uz.keys():
            print(i,end=' ')
        print("\nSo'z kiriting:")
        while True:
            s=input()
            if s in dict_uz.keys():
                break
            else:
                print("Men bu so'zni tarjimasini bilmayman!\nIltimos qaytadan kiriting")
        print(s,'-',dict_uz[s][1])
    elif a == 3:
        print('eng-uz')
        print('I can translate those words:')
        for i in dict_eng.keys():
            print(i,end=' ')
        print('\nEnter the word:')
        while True:
            s=input()
            if s in dict_eng.keys():
                break
            else:
                print("I can't translate that word!\nPlease enter the word again")
        print(s,'-',dict_eng[s][0])
    elif a == 4:
        print('eng-ru')
        print('I can translate those words:')
        for i in dict_eng.keys():
            print(i,end=' ')
        print('\nEnter the word:')
        while True:
            s=input()
            if s in dict_eng.keys():
                break
            else:
                print("I can't translate that word!\nPlease enter the word again")
        print(s,'-',dict_eng[s][1])
    elif a == 5:
        print('ru-uz')
        print('Я могу перевести эти слова:')
        for i in dict_ru.keys():
            print(i,end=' ')
        print('\nВведите слово:')
        while True:
            s=input()
            if s in dict_ru.keys():
                break
            else:
                print("Я не могу перевести это слово!\nПожалуйста введите слово еще раз")
        print(s,'-',dict_ru[s][0])
    elif a == 6:
        print('ru-eng')
        print('Я могу перевести эти слова:')
        for i in dict_ru.keys():
            print(i,end=' ')
        print('\nВведите слово:')
        while True:
            s=input()
            if s in dict_ru.keys():
                break
            else:
                print("Я не могу перевести это слово!\nПожалуйста введите слово еще раз")
        print(s,'-',dict_ru[s][1])