import flet as ft
from logic import Logic

def main(page: ft.Page) -> None:
    
    page.title="vSAN Sizing Tool"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    
    page.window.bgcolor=ft.colors.AMBER
    page.window.title_bar_hidden=False
    page.window.frameless=False
    page.window.maximized=True

    page.scroll = ft.ScrollMode.AUTO

    page.add(ft.Row([
                     Logic(),
                     
                    ])
             
             )
  

if __name__ == "__main__":
   ft.app(main)
