import tkinter as tk
from tkinter import ttk
from logic import GymLogic

class GymManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gym Management System")
        self.logic = GymLogic()

        self.create_widgets()

    def create_widgets(self):
        # Labels and entry fields for customer information
        name_label = tk.Label(self.root, text="Name:")
        name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        phone_label = tk.Label(self.root, text="Phone Number:")
        phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        gender_label = tk.Label(self.root, text="Gender:")
        gender_label.pack()
        self.gender_var = tk.StringVar(value="Male")
        gender_radiobutton1 = tk.Radiobutton(self.root, text="Male", variable=self.gender_var, value="Male")
        gender_radiobutton2 = tk.Radiobutton(self.root, text="Female", variable=self.gender_var, value="Female")
        gender_radiobutton1.pack()
        gender_radiobutton2.pack()

        # Dropdown menu for plan selection
        plan_label = tk.Label(self.root, text="Select a Plan:")
        plan_label.pack()
        self.plan_var = tk.StringVar(value="Zumba")
        plan_menu = tk.OptionMenu(self.root, self.plan_var, *self.logic.get_plans())
        plan_menu.pack()

        # Buttons
        calculate_button = tk.Button(self.root, text="Calculate Price", command=self.calculate_price)
        calculate_button.pack()

        add_member_button = tk.Button(self.root, text="Add Member", command=self.add_member)
        add_member_button.pack()

        # Label to display the calculated price
        self.price_label = tk.Label(self.root, text="Total Price: ₹0")
        self.price_label.pack()

        # Table to display member details
        columns = ("Name", "Phone Number", "Gender", "Plan", "Price")
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack()

    def calculate_price(self):
        selected_plan = self.plan_var.get()
        price = self.logic.calculate_price(selected_plan)
        self.price_label.config(text=f"Total Price: ₹{price}pm")

    def add_member(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        gender = self.gender_var.get()
        plan = self.plan_var.get()

        self.logic.add_member(name, phone, gender, plan)
        self.update_table()

        # Clear the input fields
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)

    def update_table(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for member in self.logic.get_members():
            self.tree.insert("", "end", values=member)

    def run(self):
        self.root.mainloop()