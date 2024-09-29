import flet as ft
from clustercfg import cluster_section

def main(page: ft.Page) -> None:
    
    page.title = "vSAN Sizing Tool"
    page.window_width = 600
    page.window_height = 900
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.window.bgcolor = ft.colors.GREY_800
    page.bgcolor = ft.colors.TRANSPARENT
    page.window.title_bar_hidden = False
    page.window.frameless = False
    page.window.left = 400
    page.window.top = 200
    
    page.add(cluster_section
             )
  

if __name__ == "__main__":
   ft.app(main)
