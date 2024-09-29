import flet as ft

hosts=ft.TextField(label="主機數量", width=100, value=0, label_style=ft.TextStyle(size=18))
sockets=ft.TextField(label="Socket / host ", width=120, value=0, label_style=ft.TextStyle(size=18))
cores=ft.TextField(label="Core / Socket ", width=120, value=0, label_style=ft.TextStyle(size=18))
hosts1=ft.TextField(label="主機數量", width=100, value=0, label_style=ft.TextStyle(size=18))
sockets1=ft.TextField(label="Socket / host ", width=120, value=0, label_style=ft.TextStyle(size=18))
cores1=ft.TextField(label="Core / Socket ", width=120, value=0, label_style=ft.TextStyle(size=18))

def btn_click(e):
    print(hosts.value)
    print(hosts1.value)


cluster_section=ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                    margin=5,
                    padding=5,
                    alignment=ft.alignment.center,
                    expand=True,
                    border_radius=10,
                    content=ft.Column([ft.Text("vSAN Configuration", size=20),
                                      ft.Divider(),
                                      ft.Row([
                                             hosts,
                                             sockets,
                                             cores
                                      ]),
                                      ft.Row([
                                             hosts1,
                                             sockets1,
                                             cores1
                                      ]),    
                                      
                    ])
                ),
                ft.ElevatedButton("ClickMe", on_click=btn_click)
            ],
            spacing=0,
            width=400,
            height=450,
            
        )

