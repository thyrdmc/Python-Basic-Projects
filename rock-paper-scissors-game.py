import random

from ascii_logos import rock, paper, scissors

images = [rock, paper, scissors]

user_name = str(input('Hoşgeldiniz adınız nedir? '))
user_choice = int(input(f'Hangisini seçiyorsun {user_name}? Taş için 0, Kağıt için 1, Makas için 2 yi tuşlayınız: '))

if user_choice >= 0 and user_choice < 3:
    
    print(images[user_choice])

    computer_choice = random.randint(0,2)
    print('Bilgisayarın Seçimi: \n')

    print(images[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("Geçersiz sayı girdiniz, Kaybettiniz!")

    elif user_choice == 0 and computer_choice == 2:
        print(f'Tebrikler {user_name} kazandınız!')

    elif user_choice == 2 and computer_choice == 0:
        print(f'Üzgünüm {user_name} kaybettiniz!')

    elif user_choice > computer_choice:
        print(f'Tebrikler {user_name} kazandınız!')

    elif user_choice < computer_choice:
        print(f'Üzgünüm {user_name} kaybettiniz!')

    else:
        print("Oyun berabere bitti.")

else:
    print("Geçersiz sayı girdiniz, Kaybettiniz!")


