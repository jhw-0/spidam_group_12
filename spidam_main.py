from model import Model
from view import View
from controller import Controller
import tkinter as tk

# Main Application
def main():
    # Create and initialize a tk.Tk() root instance
    root = tk.Tk()
    root.title("Scientific Python Interactive Data Acoustic Modeling")
    root.geometry("800x600")
    # Create MVC instances
    model = Model()
    view = View(root)
    Controller(model, view)
    # Start event loop
    root.mainloop()


if __name__ == "__main__":
    main()