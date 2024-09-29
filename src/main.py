import flet as ft
from src.clustercfg import cluster_section
from workloadcfg import workloadcfg_section

def main(page: ft.Page) -> None:
    
    page.title = "vSAN Sizing Tool"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.window.bgcolor = ft.colors.AMBER
    page.window.title_bar_hidden = False
    page.window.frameless = False
    page.window.maximized = True
    page.scroll = ft.ScrollMode.AUTO

    page.add(cluster_section,
             workloadcfg_section
             )
  

if __name__ == "__main__":
   ft.app(main)
