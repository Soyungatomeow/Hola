import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
special_chars = "!@#$%^&*()_+"

print("\033[1;34mBienvenida Vane a tu generador de Contraseñas!!!\033[m")

Size = int(input("\033[1m¿De cuántos caracteres quieres que sea tu contraseña? \033[m"))
Special = input("\033[1m¿Quieres que tu contraseña tenga caracteres especiales? (\033[1;32mY\033[m/\033[1;32mN\033[m) ")

while Special != "Y" and Special != "N":
    print("\033[1;31mPor favor, introduce \033[1;32mY\033[m \033[1;31mo \033[1;32mN\033[m\033[1;31m.\033[m")
    Special = input("\033[1m¿Quieres que tu contraseña tenga caracteres especiales? (\033[1;32mY\033[m/\033[1;32mN\033[m) ")

if Special == "Y":
    password = ""
    for i in range(Size):
        password += random.choice(chars + special_chars)
elif Special == "N":
    password = ""
    for i in range(Size):
        password += random.choice(chars)

password = "\033[1;35m" + password + "\033[m"
print("\033[1mTu contraseña es: " + password)

        
