import tkinter as tk
from gui import tela_login

def main():
    root = tk.Tk()
    root.title("Dark Web Simulator 🕸️")
    tela_login.TelaLogin(root)
    root.mainloop()

if __name__ == "__main__":
    main()
