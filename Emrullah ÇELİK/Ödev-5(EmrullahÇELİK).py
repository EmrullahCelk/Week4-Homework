import random
import string
import tkinter as tk



def random_student(std_list=["Emrullah Bey", "Ertan Bey", "Fethullah Bey", "Furkan Bey", 
    "Hasan Bey", "Mehmet Bey", "Ömer Bey", "Tayyip Bey", 
    "Yunus Emre Bey", "Merve Hanım", "Mustafa Bey", "Murat Bey"],
    waiting = []):
    
    student = random.sample(std_list, 1) # rastgele öğrenci seçimi
    std_list.remove(student[0]) # seçilen ismi listeden siliyor
    waiting += student # seçilen ismi bekleme listesine gönderiyor
    if len(waiting) == 4: # bekleme listesinin uzunluğu 4 e eşit olduğunda
        std_list.append(waiting[0]) #bekleme listesinin ilk elemanını en baştaki listeye gönderiyor
        del waiting[0] # ve gönderdiği ismi bekleme listesinden siliyor
    str = ''
    for i in student:
        str += i
    print(str)
    label.config(text=str)
 

window = tk.Tk()

window.title("Random Student")
window.geometry("600x300")


key_application = tk.Frame(window)
key_application.grid()


# label
label_txt = tk.Label(key_application, text="Student name:", font="arial 15 bold")
label_txt.grid(padx=110, pady=10)


# label
label = tk.Label(key_application, text="Please push the botton to choose a next student ", font="arial 12")
label.grid(padx=110, pady=20)


# button
button1 = tk.Button(key_application, text=" CHOOSE ", width=50, height=5, command=random_student)
button1.grid(padx=110, pady=40)

window.mainloop()
