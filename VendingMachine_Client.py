from tkinter import *
import socket

class VendingMachine(Tk):
    def __init__(self):
        super().__init__()
        self.title("Vending Machine")
        self.geometry("700x750+110+20")
        self.resizable(True, True)
        self.create_frames()
        self.selected_items = []

        self.SERVER_IP = 'localhost'
        self.SERVER_PORT = 65432

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.client_socket.connect((self.SERVER_IP, self.SERVER_PORT))
        print("Connected to server")

    def create_frames(self):
        self.base1 = Frame(self, bg="#CE0505", width=0.6 * 800, height=600)
        self.base1.pack(side=LEFT, fill=BOTH, expand=True)

        self.glass = Frame(self.base1, bg="#9A3B4B", width=0.55 * 800, height=0.4 * 800)
        self.glass.pack(pady=(20, 0))

        self.recycle_label = Label(self.base1, text="Recycle used plastic\n AED 1", bg="#B71717", fg="white", font=("Arial", 16, "bold"), width=29, height=5)
        self.recycle_label.pack(side="top", pady=(50, 0))

        self.thankYou_label = Label(self.base1, text="THANK YOU!", bg="#9A3B4B", fg="white", font=("Arial", 24, "bold"), width=20, height=3)
        self.thankYou_label.pack(side="bottom", pady=(0, 60))

        tray_frame1 = Frame(self.glass, bg="#DCDCDC", width=0.25 * 1800, height=0.1 * 200)
        tray_frame1.place(relx=0.5, rely=0.3, anchor=CENTER)

        tray_frame2 = Frame(self.glass, bg="#DCDCDC", width=0.25 * 1800, height=0.1 *200)
        tray_frame2.place(relx=0.5, rely=0.75, anchor=CENTER)

        self.base2 = Frame(self, bg="#EC0808", width=0.4 * 800, height=600)
        self.base2.pack(side=LEFT, fill=BOTH, expand=True)

        self.card_photo = PhotoImage(file='Card.png')
        self.resized_cardphoto = self.card_photo.subsample(1, 1)
        self.card_photoLabel = Label(self.base2, image=self.resized_cardphoto, borderwidth=0)
        self.card_photoLabel.place(relx=0.809, rely=0.62, anchor=CENTER)

        self.coin_photo = PhotoImage(file='Coin.png')
        self.resized_coinphoto = self.coin_photo.subsample(1, 1)
        self.coin_photoLabel = Label(self.base2, image=self.resized_coinphoto, borderwidth=0)
        self.coin_photoLabel.place(relx=0.81, rely=0.69, anchor=CENTER)
        
        self.welcome_label = Label(self.base2, text="WELCOME!", bg="black", fg="white", font=("Arial", 24, "bold"), width=14)
        self.welcome_label.pack(pady=20)

        self.water_borderframe = Frame(self.glass, bg="#DCDCDC", width=212, height=47)
        self.water_borderframe.place(relx=0.013, rely=0.33)

        self.energy_borderframe = Frame(self.glass, bg="#DCDCDC", width=212, height=47)
        self.energy_borderframe.place(relx=0.505, rely=0.33)

        self.choco_borderframe = Frame(self.glass, bg="#DCDCDC", width=212, height=47)
        self.choco_borderframe.place(relx=0.013, rely=0.78)

        self.juice_borderframe = Frame(self.glass, bg="#DCDCDC", width=212, height=47)
        self.juice_borderframe.place(relx=0.505, rely=0.78)

#---Water---Water---Water---Water---Water---

        self.water_label = Label(self.glass, text="Water\nAED 1", bg="blue", fg="white", font=("Arial", 12, "bold"), width= 20, height = 2)
        self.water_label.place(relx=0.021, rely=0.33)

        self.water_ID = Label(self.glass, text="101", bg="blue", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.water_ID.place(relx=0.058, rely=0.275)

        self.water_ID2 = Label(self.glass, text="102", bg="blue", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.water_ID2.place(relx=0.17, rely=0.275)

        self.water_ID3 = Label(self.glass, text="103", bg="blue", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.water_ID3.place(relx=0.285, rely=0.275)

        self.water_ID4 = Label(self.glass, text="104", bg="blue", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.water_ID4.place(relx=0.4, rely=0.275)

        self.water_photo = PhotoImage(file='Water.png')
        self.resized_waterphoto = self.water_photo.subsample(1, 1)
        self.water_photoLabel = Label(self.glass, image=self.resized_waterphoto, borderwidth=0)
        self.water_photoLabel.place(x=20, y=4)

        self.water_photo2 = PhotoImage(file='Water.png')
        self.resized_waterphoto2 = self.water_photo2.subsample(1, 1)
        self.water_photoLabel2 = Label(self.glass, image=self.resized_waterphoto2, borderwidth=0)
        self.water_photoLabel2.place(x=70, y=4)

        self.water_photo3 = PhotoImage(file='Water.png')
        self.resized_waterphoto3 = self.water_photo3.subsample(1, 1)
        self.water_photoLabel3 = Label(self.glass, image=self.resized_waterphoto3, borderwidth=0)
        self.water_photoLabel3.place(x=120, y=4)

        self.water_photo4 = PhotoImage(file='Water.png')
        self.resized_waterphoto4 = self.water_photo4.subsample(1, 1)
        self.water_photoLabel4 = Label(self.glass, image=self.resized_waterphoto4, borderwidth=0)
        self.water_photoLabel4.place(x=170, y=4)
        
#---Energy---Energy---Energy---Energy---Energy---
        
        self.energy_label = Label(self.glass, text="Energy Drink\nAED 3", bg="green", fg="white", font=("Arial", 12, "bold"), width= 20, height = 2)
        self.energy_label.place(relx=0.51, rely=0.33)

        self.energy_ID = Label(self.glass, text="205", bg="green", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.energy_ID.place(relx=0.537, rely=0.275)

        self.energy_ID2 = Label(self.glass, text="206", bg="green", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.energy_ID2.place(relx=0.65, rely=0.275)

        self.energy_ID3 = Label(self.glass, text="207", bg="green", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.energy_ID3.place(relx=0.764, rely=0.275)

        self.energy_ID4 = Label(self.glass, text="208", bg="green", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.energy_ID4.place(relx=0.878, rely=0.275)

        self.energy_photo = PhotoImage(file='EnergyDrink.png')
        self.resized_energyphoto = self.energy_photo.subsample(1, 1)
        self.energy_photoLabel = Label(self.glass, image=self.resized_energyphoto, borderwidth=0)
        self.energy_photoLabel.place(x=230, y=41)

        self.energy_photo2 = PhotoImage(file='EnergyDrink.png')
        self.resized_energyphoto2 = self.energy_photo2.subsample(1, 1)
        self.energy_photoLabel2 = Label(self.glass, image=self.resized_energyphoto2, borderwidth=0)
        self.energy_photoLabel2.place(x=280, y=41)

        self.energy_photo3 = PhotoImage(file='EnergyDrink.png')
        self.resized_energyphoto3 = self.energy_photo3.subsample(1, 1)
        self.energy_photoLabel3 = Label(self.glass, image=self.resized_energyphoto3, borderwidth=0)
        self.energy_photoLabel3.place(x=330, y=41)

        self.energy_photo4 = PhotoImage(file='EnergyDrink.png')
        self.resized_energyphoto4 = self.energy_photo4.subsample(1, 1)
        self.energy_photoLabel4 = Label(self.glass, image=self.resized_energyphoto4, borderwidth=0)
        self.energy_photoLabel4.place(x=380, y=41)

#---Choco---Choco---Choco---Choco---Choco---
        self.choco_label = Label(self.glass, text="Choco Spheres\nAED 4", bg="orange", fg="white", font=("Arial", 12, "bold"), width= 20, height = 2)
        self.choco_label.place(relx=0.021, rely=0.78)

        self.choco_ID = Label(self.glass, text="309", bg="orange", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.choco_ID.place(relx=0.058, rely=0.725)
        
        self.choco_ID2 = Label(self.glass, text="310", bg="orange", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.choco_ID2.place(relx=0.17, rely=0.725)

        self.choco_ID3 = Label(self.glass, text="311", bg="orange", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.choco_ID3.place(relx=0.285, rely=0.725)

        self.choco_ID4 = Label(self.glass, text="312", bg="orange", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.choco_ID4.place(relx=0.4, rely=0.725)

        self.choco_photo = PhotoImage(file='Choco.png')
        self.resized_chocophoto = self.choco_photo.subsample(1, 1)
        self.choco_photoLabel = Label(self.glass, image=self.resized_chocophoto, borderwidth=0)
        self.choco_photoLabel.place(x=20, y=181)

        self.choco_photo2 = PhotoImage(file='Choco.png')
        self.resized_chocophoto2 = self.choco_photo2.subsample(1, 1)
        self.choco_photoLabel2 = Label(self.glass, image=self.resized_chocophoto2, borderwidth=0)
        self.choco_photoLabel2.place(x=70, y=181)

        self.choco_photo3 = PhotoImage(file='Choco.png')
        self.resized_chocophoto3 = self.choco_photo3.subsample(1, 1)
        self.choco_photoLabel3 = Label(self.glass, image=self.resized_chocophoto3, borderwidth=0)
        self.choco_photoLabel3.place(x=120, y=181)

        self.choco_photo4 = PhotoImage(file='Choco.png')
        self.resized_chocophoto4 = self.choco_photo4.subsample(1, 1)
        self.choco_photoLabel4 = Label(self.glass, image=self.resized_chocophoto4, borderwidth=0)
        self.choco_photoLabel4.place(x=170, y=181)

#---Juice---Juice---Juice---Juice---Juice---

        self.juice_label = Label(self.glass, text="Juice\nAED 2", bg="purple", fg="white", font=("Arial", 12, "bold"), width= 20, height = 2)
        self.juice_label.place(relx=0.51, rely=0.78)

        self.juice_ID = Label(self.glass, text="413", bg="purple", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.juice_ID.place(relx=0.527, rely=0.725)

        self.juice_ID2 = Label(self.glass, text="414", bg="purple", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.juice_ID2.place(relx=0.64, rely=0.725)

        self.juice_ID3 = Label(self.glass, text="415", bg="purple", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.juice_ID3.place(relx=0.755, rely=0.725)

        self.juice_ID4 = Label(self.glass, text="416", bg="purple", fg="white", font=("Arial", 7, "bold"), width= 3)
        self.juice_ID4.place(relx=0.865, rely=0.725)

        self.juice_photo = PhotoImage(file='Juice.png')
        self.resized_juicephoto = self.juice_photo.subsample(1, 1)
        self.juice_photoLabel = Label(self.glass, image=self.resized_juicephoto, borderwidth=0)
        self.juice_photoLabel.place(x=230, y=185)

        self.juice_photo2 = PhotoImage(file='Juice.png')
        self.resized_juicephoto2 = self.juice_photo2.subsample(1, 1)
        self.juice_photoLabel2 = Label(self.glass, image=self.resized_juicephoto2, borderwidth=0)
        self.juice_photoLabel2.place(x=280, y=185)

        self.juice_photo3 = PhotoImage(file='Juice.png')
        self.resized_juicephoto3 = self.juice_photo3.subsample(1, 1)
        self.juice_photoLabel3 = Label(self.glass, image=self.resized_juicephoto3, borderwidth=0)
        self.juice_photoLabel3.place(x=330, y=185)

        self.juice_photo4 = PhotoImage(file='Juice.png')
        self.resized_juicephoto4 = self.juice_photo4.subsample(1, 1)
        self.juice_photoLabel4 = Label(self.glass, image=self.resized_juicephoto4, borderwidth=0)
        self.juice_photoLabel4.place(x=380, y=185)
        
        self.pie_chart_frame = Frame(self.base2, bg="#FD6464", width=0.4 * 800, height=250)
        self.pie_chart_frame.pack(side=TOP, fill=X)

        self.input_entry = Entry(self.base2, font=("Arial", 12, "bold"), bg="black", justify="center", fg="white", width=10)
        self.input_entry.pack(pady=(30))

        keypad_bg_frame = Frame(self.base2, bg="#8B0000", height=400)
        keypad_bg_frame.pack(padx=50, pady=(1, 10))

        keypad_frame = Frame(keypad_bg_frame, bg="#C31616")
        keypad_frame.pack(side=TOP, fill=BOTH, expand=True)

        self.change_photo = PhotoImage(file='Change.png')
        self.resized_changephoto = self.change_photo.subsample(1, 1)
        self.change_photoLabel = Label(self.base2, image=self.resized_changephoto, borderwidth=0)
        self.change_photoLabel.place(relx=0.5, rely=0.9, anchor=CENTER)

        keypad_buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('Del', 3, 0), ('0', 3, 1)
        ]
        for (text, row, column) in keypad_buttons:
            button = Button(keypad_frame, text=text, font=("Arial", 12, "bold"), width=2, height=1, bg="#AB0000", fg="#FFFFFF", command=lambda t=text: self.update_entry(t))
            button.grid(row=row, column=column, padx=5, pady=5)
        ok_button = Button(keypad_frame, text="OK", font=("Arial", 12, "bold"), width=2, height=1, bg="#AB0000", fg="#FFFFFF", command=self.confirmation_window)
        ok_button.grid(row=3, column=2, padx=5, pady=5)

    def update_entry(self, value):
        current_input = self.input_entry.get()
        if len(current_input) > 2:
            if value == 'Del':
                self.input_entry.delete(len(current_input) - 1, END)
        elif len(current_input) > 0:
            if value == 'Del':
                self.input_entry.delete(len(current_input) - 1, END)
            else:
                self.input_entry.insert(END, value)
        elif value != 'Del':
            self.input_entry.insert(END, value)

    def cash(self, window):
        window.destroy()
        thank_you_window = Toplevel(self)
        thank_you_window.title("Thank You!")
        thank_you_window.geometry("500x400")
        thank_you_window.resizable(False, False)

        thank_you_label = Label(thank_you_window, text="Thank you for your purchase\n Please come again!", font=("Arial", 16, "bold"))
        thank_you_label.pack(pady=10)

    def card(self, window):
        window.destroy()
        thank_you_window = Toplevel(self)
        thank_you_window.title("Thank You!")
        thank_you_window.geometry("500x400")
        thank_you_window.resizable(False, False)

        thank_you_label = Label(thank_you_window, text="Thank you for your purchase\n Please come again!", font=("Arial", 16, "bold"))
        thank_you_label.pack(pady=10)

    def confirm_button_press(self, window):
        window.destroy()
        payment_method = Toplevel(self)
        payment_method.title("Select Payment")
        payment_method.geometry("500x400")
        payment_method.resizable(False, False)

        select_payment_label = Label(payment_method, text="Choose your desired payment method:", font=("Arial", 16, "bold"))
        select_payment_label.pack(pady=10)

        cash_button = Button(payment_method, text="Cash", font=("Arial", 12, "bold"), width=14, height=3, bg="green", command= lambda: self.cash(payment_method))
        cash_button.place(relx=0.17, rely=0.3)

        card_button = Button(payment_method, text="Card", font=("Arial", 12, "bold"), width=14, height=3, bg="yellow", command= lambda: self.card(payment_method))
        card_button.place(relx=0.54, rely=0.3)

    def add_another_button_press(self, window):
        window.destroy()

    def cancel_button_press(self, window):
        self.selected_items = []
        self.client_socket.send("cancel".encode())
        print("Cancellation signal sent to server")
        window.destroy()


    def confirmation_window(self):
        input_text = self.input_entry.get()
        if input_text.isdigit() and len(input_text) == 3:
            self.client_socket.send(input_text.encode())
            print("Input sent to server:", input_text)
            response = self.client_socket.recv(1024).decode()
            print("Response from server:", response)
            if response.startswith("Item found:"):
                item_info = response.replace("Item found: ", "")
                item_id, item_name, item_price = item_info.split(", ")
                self.selected_items.append((item_id, item_name, item_price))

                total_price = sum(float(item_price.split(": ")[1]) for _, _, item_price in self.selected_items)

                confirm_purchase = Toplevel(self)
                confirm_purchase.title("Confirm Purchase")
                confirm_purchase.geometry("600x600")
                confirm_purchase.resizable(False, False)

                purchase_label = Label(confirm_purchase, text="Would you like to confirm your purchase?\n\n Selected Items:", font=("Arial", 12, "bold"))
                purchase_label.pack(pady=20)

                for selected_item in self.selected_items:
                    item_id, item_name, item_price = selected_item
                    item_label = Label(confirm_purchase, text=f"{item_id}, {item_name}, {item_price}", font=("Arial", 10))
                    item_label.pack()

                total_price_label = Label(confirm_purchase, text=f"Total Price: AED {total_price:.2f}", font=("Arial", 12, "bold"))
                total_price_label.pack(pady=10)

                confirm_button = Button(confirm_purchase, text="Confirm", font=("Arial", 12, "bold"), width=14, height=3, bg="#3AFF08", command=lambda: self.confirm_button_press(confirm_purchase))
                confirm_button.place(relx=0.07, rely=0.8)

                add_another_button = Button(confirm_purchase, text="Add another item", font=("Arial", 12, "bold"), width=14, height=3, bg="light grey", command=lambda: self.add_another_button_press(confirm_purchase))
                add_another_button.place(relx=0.38, rely=0.8)

                cancel_button = Button(confirm_purchase, text="Cancel", font=("Arial", 12, "bold"), width=14, height=3, bg="red", command=lambda: self.cancel_button_press(confirm_purchase))
                cancel_button.place(relx=0.69, rely=0.8)
            else:
                error_window = Toplevel(self)
                error_window.title("Error")
                error_window.geometry("600x600")
                error_window.resizable(False, False)

                error_label = Label(error_window, text="Sorry! Your item does not exist. Please try another item", font=("Arial", 12, "bold"))
                error_label.pack(pady=20)
        else:
            print("Invalid input:", input_text)


    def __del__(self):
        self.client_socket.close()

if __name__ == "__main__":
    run = VendingMachine()
    run.mainloop()
