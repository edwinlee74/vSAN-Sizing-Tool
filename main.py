import flet as ft
from flet_core.control_event import ControlEvent


def main(page: ft.Page) -> None:
    page.title = "vSAN Sizing Tool"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.add(ft.Row(
            [
                ft.Container(
                    bgcolor=ft.colors.ORANGE_300,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
                 ft.VerticalDivider(),
                ft.Container(
                    bgcolor=ft.colors.BROWN_400,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
                 ft.VerticalDivider(width=1, color="white"),
                ft.Container(
                    bgcolor=ft.colors.BLUE_300,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
                 ft.VerticalDivider(width=9, thickness=3),
                ft.Container(
                    bgcolor=ft.colors.GREEN_300,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
            ],
            spacing=0,
            width=400,
            height=400
        )
    )


if __name__ == "__main__":
   ft.app(main)
