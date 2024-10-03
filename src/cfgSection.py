import flet as ft

# vSAN Configuration section.
hosts=ft.TextField(label="Node數量", width=120, value=3, border="underline", label_style=ft.TextStyle(size=18))
sockets=ft.TextField(label="Sockets/Node ", width=120, value=2, border="underline", label_style=ft.TextStyle(size=18))
cores=ft.TextField(label="Cores/Socket", width=120, value=20, border="underline", label_style=ft.TextStyle(size=18))
memory=ft.TextField(label="RAM(GB)/Node", width=120, value=0, border="underline", label_style=ft.TextStyle(size=18))
clock=ft.TextField(label="CPU時脈(GHz)", width=120, value=0, border="underline", label_style=ft.TextStyle(size=18))
ftt=ft.TextField(label="FTT", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
diskgroup=ft.TextField(label="DiskGroup/Node", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
capacity=ft.TextField(label="容量層硬碟大小(TB)", width=125, value=1.2, border="underline", label_style=ft.TextStyle(size=18))
capacity_qty=ft.TextField(label="容量層硬碟數量", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
cache=ft.TextField(label="快取層硬碟大小(TB)", width=125, value=1.2, border="underline", label_style=ft.TextStyle(size=18))
cache_qty=ft.TextField(label="快取層硬碟數量", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
fault_tolerance=ft.Checkbox(label="Enable FT", value=False)

# Workload Configuration section.
vms=ft.TextField(label="VM數量", width=120, value=0, border="underline", label_style=ft.TextStyle(size=18))
vcpu=ft.TextField(label="vCPU/VM", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
vram=ft.TextField(label="vRAM/VM", width=120, value=1, border="underline", label_style=ft.TextStyle(size=18))
storage=ft.TextField(label="Storage/VM(GB)", width=120, value=0, border="underline", label_style=ft.TextStyle(size=18))
log_bandwith=ft.TextField(label="FT log bandwidth(KB/s)", width=150, value=0, disabled=True, border="underline", label_style=ft.TextStyle(size=18))

def result_calculate(e):
    print(hosts.value)
    print(vms.value)


# widgets
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
                                          cache_qty,
                                          fault_tolerance
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
                    content=ft.Column([ft.Text("Workload Configuration", size=20),
                                      ft.Divider(),
                                      ft.Row([
                                          vms,
                                          vcpu,
                                          vram,
                                      ]),
                                      ft.Row([
                                          storage,
                                          log_bandwith
                                      ])
                                      
                    ])
                ),
                ft.ElevatedButton("開始估算", on_click=result_calculate, bgcolor=ft.colors.BLUE)
            ],
            spacing=0,
            width=400,
            height=660,
            
        )

