import flet as ft

class Logic(ft.Row):

    def __init__(self):
        
        super().__init__()
        self.spacing=0
        self.width=800
        self.height=700

        # style
        config_label=ft.TextStyle(size=18)
        result_font_size=20
        deep_orange=ft.colors.DEEP_ORANGE
        black38=ft.colors.BLACK38

        # vSAN Configuration section.
        self.hosts=ft.TextField(label="Node數量", width=120, value=3, border="underline", label_style=config_label)
        self.sockets=ft.TextField(label="Sockets/Node ", width=120, value=2, border="underline", label_style=config_label)
        self.cores=ft.TextField(label="Cores/Socket", width=120, value=20, border="underline", label_style=config_label)
        self.memory=ft.TextField(label="RAM(GB)/Node", width=120, value=0, border="underline", label_style=config_label)
        self.clock=ft.TextField(label="CPU時脈(GHz)", width=120, value=0, border="underline", label_style=config_label)
        self.ftt=ft.TextField(label="FTT", width=120, value=1, border="underline", label_style=config_label)
        self.diskgroup=ft.TextField(label="DiskGroup/Node", width=120, value=1, border="underline", label_style=config_label)
        self.capacity=ft.TextField(label="容量層硬碟大小(TB)", width=125, value=1.2, border="underline", label_style=config_label)
        self.capacity_qty=ft.TextField(label="容量層硬碟數量", width=120, value=1, border="underline", label_style=config_label)
        self.cache=ft.TextField(label="快取層硬碟大小(TB)", width=125, value=1.2, border="underline", label_style=config_label)
        self.cache_qty=ft.TextField(label="快取層硬碟數量", width=120, value=1, border="underline", label_style=config_label)
        self.fault_tolerance=ft.Checkbox(label="Enable FT", value=False, on_change=self._is_ft_enable)
        self.vsan_section=ft.Container(
                             bgcolor=ft.colors.LIGHT_BLUE_100,
                             margin=5,
                             padding=5,
                             alignment=ft.alignment.center,
                             expand=True,
                             border_radius=10,
                             content=ft.Column([ft.Text("vSAN Configuration", size=result_font_size),
                                               ft.Divider(),
                                               ft.Row([
                                                   self.hosts,
                                                   self.sockets,
                                                   self.cores
                                               ]),
                                               ft.Row([
                                                   self.memory,
                                                   self.clock,
                                                   self.ftt
                                               ]),    
                                               ft.Row([
                                                   self.diskgroup,
                                                   self.capacity,
                                                   self.capacity_qty,
                                               ]),
                                               ft.Row([
                                                   self.cache,
                                                   self.cache_qty,
                                                   self.fault_tolerance
                                               ])
                             ])
                          )
        
        # Workload Configuration section.
        self.vms=ft.TextField(label="VM數量", width=120, value=0, border="underline", label_style=config_label)
        self.vcpu=ft.TextField(label="vCPU/VM", width=120, value=1, border="underline", label_style=config_label)
        self.vram=ft.TextField(label="vRAM/VM", width=120, value=1, border="underline", label_style=config_label)
        self.storage=ft.TextField(label="Storage/VM(GB)", width=120, value=0, border="underline", label_style=config_label)
        self.log_bandwith=ft.TextField(label="FT log bandwidth(KB/s)", width=150, value=0, disabled=True, border="underline", label_style=config_label)
        self.workload_section=ft.Container(
                                 bgcolor=ft.colors.LIGHT_BLUE_100,
                                 margin=5,
                                 padding=5,
                                 alignment=ft.alignment.center,
                                 expand=True,
                                 border_radius=10,
                                 content=ft.Column([ft.Text("Workload Configuration", size=result_font_size),
                                                   ft.Divider(),
                                                   ft.Row([
                                                       self.vms,
                                                       self.vcpu,
                                                       self.vram,
                                                   ]),
                                                   ft.Row([
                                                       self.storage,
                                                       self.log_bandwith
                                                   ])
                                                   
                                 ])
                                )
        

        # Result section.
        ref_text=ft.Ref[ft.Text]()
        self.raw_capacity_value_ref=ref_text
        self.raw_cache_value_ref=ref_text
        self.pcpu_vcpu_value_ref=ref_text
        self.pram_vram_value_ref=ref_text

        self.raw_capacity=ft.Text(value="Raw Capacity: ", size=result_font_size, color=deep_orange)
        self.raw_cache=ft.Text(value="Raw Cache: ", size=result_font_size, color=deep_orange)
        self.pcpu_vcpu=ft.Text(value="pCPU : vCPU: ", size=result_font_size, color=deep_orange)
        self.pram_vram=ft.Text(value="pRAM : vRAM: ", size=result_font_size, color=deep_orange)
        self.raw_capacity_value=ft.Text(ref=self.raw_capacity_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.raw_cache_value=ft.Text(ref=self.raw_cache_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.pcpu_vcpu_value=ft.Text(ref=self.pcpu_vcpu_value_ref, value="0 : 0", size=result_font_size, color=black38)
        self.pram_vram_value=ft.Text(ref=self.pram_vram_value_ref, value="0 : 0", size=result_font_size, color=black38)

        self.normal_radius = 50
        self.hover_radius = 60
        self.normal_title_style = ft.TextStyle(
            size=16, color=ft.colors.WHITE, weight=ft.FontWeight.BOLD
        )
        self.hover_title_style = ft.TextStyle(
            size=22,
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD,
            shadow=ft.BoxShadow(blur_radius=2, color=ft.colors.BLACK54),
        )
        self.space_usage_chart = ft.PieChart(
                 sections=[
                     ft.PieChartSection(
                         40,
                         title="disk space",
                         title_style=self.normal_title_style,
                         color=ft.colors.BLUE,
                         radius=self.normal_radius,
                     ),
                     ft.PieChartSection(
                         30,
                         title="30%",
                         title_style=self.normal_title_style,
                         color=ft.colors.YELLOW,
                         radius=self.normal_radius,
                     ),
                     ft.PieChartSection(
                         15,
                         title="15%",
                         title_style=self.normal_title_style,
                         color=ft.colors.PURPLE,
                         radius=self.normal_radius,
                     ),
                     ft.PieChartSection(
                         15,
                         title="15%",
                         title_style=self.normal_title_style,
                         color=ft.colors.GREEN,
                         radius=self.normal_radius,
                     ),
                 ],
                 sections_space=0,
                 center_space_radius=40,
                 on_chart_event=self.on_chart_event,
                 expand=True,
                 visible=False
             )
        
      

        self.result_section=ft.Container(
                            bgcolor=ft.colors.LIGHT_GREEN_100,
                                 margin=5,
                                 padding=5,
                                 alignment=ft.alignment.center,
                                 expand=True,
                                 border_radius=10,
                                 content=ft.Column([
                                                   ft.Row([
                                                      self.raw_capacity,
                                                      self.raw_capacity_value,
                                                      self.raw_cache,
                                                      self.raw_cache_value,
                                                      self.pcpu_vcpu,
                                                      self.pcpu_vcpu_value,
                                                      self.pram_vram,
                                                      self.pram_vram_value,
                                                    ]),
                                                   ft.Row([
                                                      self.space_usage_chart,
                                                   ])
                                        ])
                            
                            )

        self.controls=[ 
            ft.Column([
            self.vsan_section,
            self.workload_section,
            ft.ElevatedButton("開始估算", on_click=self.on_result_calculate),
            ]),
            ft.Row(
                spacing=10,
                width=1100,
                height=800,
                controls=[
                          self.result_section,
                ]
            )
            
        ]
        
    def on_result_calculate(self, e):  
        self._check_min_memory()
        self._raw_capacity()
        self._raw_cache()
        self._pcpu_vcpu()
        self._pram_vram()
        self._space_usage_piechart()
    
    def _is_ft_enable(self, e):
        if self.log_bandwith.disabled is True:
           self.log_bandwith.disabled=False
        else:
           self.log_bandwith.disabled=True    
        self.log_bandwith.update()

    def _check_min_memory(self):
        if int(self.memory.value) < 32:
           dlg = ft.AlertDialog(  
                 title=ft.Text("記憶體小於vSAN建議的32GB"),
                 bgcolor=ft.colors.RED_300,
                 icon=ft.Icon(name=ft.icons.WARNING)
           )
           self.page.open(dlg)

    def _raw_capacity(self):
        raw_capacity=(float(self.diskgroup.value) * float(self.capacity.value) * 
                      float(self.capacity_qty.value) * float(self.hosts.value)
        )
        self.raw_capacity_value_ref.current.value=str(round(raw_capacity, 2)) + " TB"
        self.raw_capacity_value.update()

    def _raw_cache(self):
        raw_cache=(float(self.diskgroup.value) * float(self.cache.value) *
                   float(self.cache_qty.value) * float(self.hosts.value)

        )
        self.raw_cache_value_ref.current.value=str(round(raw_cache, 2)) + " TB"
        self.raw_cache_value.update()

    def _pcpu_vcpu(self):
        pcpu=int(self.hosts.value) * int(self.sockets.value) * int(self.cores.value)
        vcpu=int(self.vms.value) * int(self.vcpu.value)
        pvcpu_ratio=round(float(vcpu / pcpu), 3)
        self.pcpu_vcpu_value_ref.current.value="1 : " + str(pvcpu_ratio)
        self.pcpu_vcpu_value.update()

    def _pram_vram(self):
        pram=float(self.hosts.value) * float(self.memory.value)
        vram=float(self.vms.value) * float(self.vram.value)
        pvram_ration=round(float(vram / pram), 3)
        self.pram_vram_value_ref.current.value="1 : " + str(pvram_ration)
        self.pram_vram_value.update()

    def _space_usage_piechart(self):
        for idx, section in enumerate(self.space_usage_chart.sections):
            section.value=25
            print(section.value)
        self.space_usage_chart.visible=True
        self.space_usage_chart.update()

    def on_chart_event(self, e: ft.PieChartEvent):
        for idx, section in enumerate(self.space_usage_chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title_style = self.hover_title_style
            else:
                section.radius = self.normal_radius
                section.title_style = self.normal_title_style
        self.space_usage_chart.update()

