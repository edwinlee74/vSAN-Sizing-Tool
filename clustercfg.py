import flet as ft

cluster_section = ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.ORANGE_300,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
                 ft.Divider(height=20, color="black"),
                ft.Container(
                    bgcolor=ft.colors.BROWN_400,
                    alignment=ft.alignment.center,
                    expand=1,
                ),
                 
            ],
            spacing=0,
            width=500,
            height=800
        )
    