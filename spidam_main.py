from model import Model
from view import View
from controller import Controller
import tkinter as tk

# Main Application
def main():
    root = tk.Tk()
    root.title("Scientific Python Interactive Data Acoustic Modeling")
    root.geometry("800x600")

    model = Model()
    view = View(root)
    Controller(model, view)

    root.mainloop()

if __name__ == "__main__":
    main()