from tkinter import *
from tkinter import ttk

class Price:
    def __init__(self, master):
        self.master = master
        master.title("Расчёт коммунальных платежей")

        global services
        services = ["Холодная вода", "Горячая вода", "Газ", "Электроэнергия", "Отопление"]

        global prices
        prices = {"Холодная вода": 20, "Горячая вода": 50, "Газ": 100, "Электроэнергия": 200, "Отопление": 40}

        self.calculate_button = Button(master, text="Расчёт", command=self.calculate)
        self.calculate_button.pack(side=BOTTOM)

        self.final_result = Text(master, width=40, height=1)
        self.final_result.pack(side=BOTTOM)

        self.final_label = Label(master, text="Сумма к оплате")
        self.final_label.pack(side=BOTTOM)

        self.past_box = []
        self.present_box = []
        self.heat_box = []
        self.result_box = []
        self.final_box = []

        for i in range(len(services)):
            if services[i] != "Отопление":
                self.label = Label(master, text=services[i])
                self.label.pack()

                self.past = ttk.Entry(master, width=50, justify=CENTER)
                self.past.insert(0, "Предыдущие показания")
                self.past_box.append(self.past)
                self.past.pack()

                self.present = ttk.Entry(master, width=50, justify=CENTER)
                self.present.insert(0, "Текущие показания")
                self.present_box.append(self.present)
                self.present.pack()

                self.price = ttk.Label(master, text=f"Тариф  - {prices[services[i]]}")
                self.price.pack()

                self.result = Text(master, width=40, height=1)
                self.result_box.append(self.result)
                self.result.pack()

            else:
                self.label = Label(master, text=services[i])
                self.label.pack()

                self.heat = ttk.Entry(master, width=50, justify=CENTER)
                self.heat.insert(0, "Площадь помещения")
                self.past_box.append(self.heat)
                self.heat.pack()

                self.price = ttk.Label(master, text=f"Тариф  - {prices[services[i]]}")
                self.price.pack()

                self.heat_result = Text(master, width=40, height=1)
                self.result_box.append(self.result)
                self.heat_result.pack()



    def calculate(self):
        self.final_box = []
        for i in range(len(self.past_box)):
            try:
                past = self.past_box[i].get()
                present = self.present_box[i].get()
                try:
                    result = prices[services[i]] * (int(present) - int(past))
                    if result > 0:
                        result = result
                    else:
                        result = "Предыдущие показания превышают текущие"
                except:
                    result = "Неверные данные"

                self.final_box.append(result)
                self.result_box[i].delete('1.0', END)
                self.result_box[i].tag_configure("center", justify='center')
                self.result_box[i].insert(INSERT, str(result))
                self.result_box[i].tag_add("center", "1.0", "end")
                self.result_box[i].pack()

            except:
                heat = self.past_box[i].get()
                try:
                    result = prices[services[i]] * (int(heat))
                    if result > 0:
                        result = result
                except:
                    result = "Неверные данные"

                self.final_box.append(result)
                self.heat_result.delete('1.0', END)
                self.heat_result.tag_configure("center", justify='center')
                self.heat_result.insert(INSERT, str(result))
                self.heat_result.tag_add("center", "1.0", "end")
                self.heat_result.pack()

        try:
            self.final_result.delete('1.0', END)
            self.final_result.tag_configure("center", justify='center')
            self.final_result.insert(INSERT, str(sum(self.final_box)))
            self.final_result.tag_add("center", "1.0", "end")
            self.final_result.pack()
        except:
            self.final_result.delete('1.0', END)
            self.final_result.tag_configure("center", justify='center')
            self.final_result.insert(INSERT, "Неверные данные")
            self.final_result.tag_add("center", "1.0", "end")
            self.final_result.pack()


root = Tk()
root.geometry('500x800')
my_gui = Price(root)
root.mainloop()
