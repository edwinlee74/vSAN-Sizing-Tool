import flet as ft

# vSAN Configuration section.
hosts=ft.TextField(label="Node數量", width=120, value=0, border="underline", label_style=ft.TextStyle(size=16))
sockets=ft.TextField(label="Sockets/Node ", width=120, value=2, border="underline", label_style=ft.TextStyle(size=16))
cores=ft.TextField(label="Cores/Socket", width=120, value=0, border="underline", label_style=ft.TextStyle(size=16))
memory=ft.TextField(label="RAM(GB)/Node", width=120, value=0, border="underline", label_style=ft.TextStyle(size=16))
clock=ft.TextField(label="CPU時脈(GHz)", width=120, value=0, border="underline", label_style=ft.TextStyle(size=16))
ftt=ft.TextField(label="FTT", width=120, value=1, border="underline", label_style=ft.TextStyle(size=16))
diskgroup=ft.TextField(label="DiskGroup/Node", width=120, value=1, border="underline", label_style=ft.TextStyle(size=16))
capacity=ft.TextField(label="容量層硬碟大小(TB)", width=120, value=1.2, border="underline", label_style=ft.TextStyle(size=16))
capacity_qty=ft.TextField(label="容量層硬碟數量", width=120, value=1, border="underline", label_style=ft.TextStyle(size=16))
cache=ft.TextField(label="快取層硬碟大小(TB)", width=120, value=1.2, border="underline", label_style=ft.TextStyle(size=16))
cache_qty=ft.TextField(label="快取層硬碟數量", width=120, value=1, border="underline", label_style=ft.TextStyle(size=16))

# Workload Configuration section.
vms=ft.TextField(label="VM數量", width=120, value=0, label_style=ft.TextStyle(size=16))

def result_calculate(e):
    print(hosts.value)
    print(vms.value)


cluster_section=ft.Column(
            [
                ft.Container(
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                    margin=5,
                    padding=5,
                    alignment=ft.alignment.center,
                    expand=True,
                    border_radius=10,
                    content=ft.Column([ft.Text("vSAN Configuration", size=16),
                                      ft.Divider(),
                                      ft.Row([
                                          hosts,
                                          sockets,
                                          cores
                                      ]),
                                      ft.Row([
                                          memory,
                                          clock,
                                          ftt
                                      ]),    
                                      ft.Row([
                                          diskgroup,
                                          capacity,
                                          capacity_qty,
                                      ]),
                                      ft.Row([
                                          cache,
                                          cache_qty
                                      ])
                    ])
                ),
                ft.Container(
                    bgcolor=ft.colors.LIGHT_BLUE_100,
                    margin=5,
                    padding=5,
                    alignment=ft.alignment.center,
                    expand=True,
                    border_radius=10,
                    content=ft.Column([ft.Text("Workload Configuration", size=16),
                                      ft.Divider(),
                                      ft.Row([
                                          vms,
                                      ])
                                      
                    ])
                ),
                ft.ElevatedButton("開始估算", on_click=result_calculate, bgcolor=ft.colors.BLUE)
            ],
            spacing=0,
            width=400,
            height=650,
            
        )

