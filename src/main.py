try:
    from turtle import mainloop
except Exception:
    def mainloop():
        pass

from src.menus import menu_principal

if __name__ == "src.main":
    menu_principal()
    mainloop()
