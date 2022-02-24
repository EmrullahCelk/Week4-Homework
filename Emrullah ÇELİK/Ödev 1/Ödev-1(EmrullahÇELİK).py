from add import * # oluşturulan diğer sayfalardan import
from divide import *
from subtract import *
from multiply import *
import sys

def calculate():
    while True:
        try:
            choice = input("Press A for addition, S for subtraction, D for division, M for multiplication, E for exit: ").lower()
            if choice == "e": # programdan çıkış
                print("Have a nice day...")
                break
            number1 = float(input("enter first number please: "))
            number2 = float(input("enter second number please: "))
            if choice == "a":
                print(add(number1, number2)) # toplama
            elif choice == "s":
                print(subtract(number1, number2)) # çıkarma
            elif choice == "d":
                print(divide(number1, number2)) # bölme
            elif choice == "m":
                print(multiply(number1, number2)) # çarpma
            else:
                print("You entered incorrectly, please try again")
        except:
            print("Ooopss!! You entered incorrectly")
            excpt = str(sys.exc_info()[0]).split("'") # except bloğu ile hata adı yazdırma
            print(excpt[1])
            
        
        
        
calculate()

