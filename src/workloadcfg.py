import flet as ft

workloadcfg_section = ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                    margin=5,
                    padding=5,
                    alignment=ft.alignment.center,
                    expand=True,
                    border_radius=10,
                    content=ft.Column([ft.Text("Workload Configuration", size=20),
                                      ft.Divider()
                                      
                    ])
                ),
                
                 
            ],
            spacing=0,
            width=400,
            height=450,
        )