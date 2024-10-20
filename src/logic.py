import flet as ft

class Logic(ft.Column):

    def __init__(self):
        
        super().__init__()
        self.spacing=0
        self.width=1500
        self.height=500

        # style
        config_label=ft.TextStyle(size=18)
        result_font_size=12
        deep_orange=ft.colors.DEEP_ORANGE
        black38=ft.colors.BLACK38

        # vSAN Configuration section.
        self.hosts=ft.TextField(label="Node數量", width=120, value=3, border="underline", label_style=config_label)
        self.sockets=ft.TextField(label="Sockets/Node ", width=120, value=2, border="underline", label_style=config_label)
        self.cores=ft.TextField(label="Cores/Socket", width=120, value=20, border="underline", label_style=config_label)
        self.memory=ft.TextField(label="RAM(GB)/Node", width=120, value=0, border="underline", label_style=config_label)
        self.clock=ft.TextField(label="CPU時脈(GHz)", width=120, value=0, border="underline", label_style=config_label)
        self.ftt=ft.TextField(label="FTT", width=120, value=1, disabled=True, border="underline", label_style=config_label)
        self.diskgroup=ft.TextField(label="DiskGroup/Node", width=120, value=1, border="underline", label_style=config_label)
        self.capacity=ft.TextField(label="容量層硬碟大小(TB)", width=130, value=1.2, border="underline", label_style=config_label)
        self.capacity_qty=ft.TextField(label="容量層硬碟數量", width=120, value=1, border="underline", label_style=config_label)
        self.cache=ft.TextField(label="快取層硬碟大小(GB)", width=135, value=400, border="underline", label_style=config_label)
        self.cache_qty=ft.TextField(label="快取層硬碟數量", width=120, value=1, border="underline", label_style=config_label)
        self.fault_tolerance=ft.Checkbox(label="Enable FT", value=False, on_change=self._is_ft_enable)
        self.vsan_section=ft.Container(
                             bgcolor=ft.colors.LIGHT_BLUE_100,
                             margin=5,
                             padding=5,
                             alignment=ft.alignment.center,
                             expand=False,
                             border_radius=10,
                             content=ft.Column([ft.Text("vSAN Configuration", weight=ft.FontWeight.BOLD, size=result_font_size),
                                               ft.Divider(height=9, thickness=3, color=ft.colors.AMBER),
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
                                               ]),
                                               
                             ],
                             width=400)
                          )
        
        # Workload Configuration section.
        self.vms=ft.TextField(label="VM數量", width=55, value=0, border="underline", label_style=config_label)
        self.vcpu=ft.TextField(label="vCPU/VM", width=65, value=1, border="underline", label_style=config_label)
        self.vram=ft.TextField(label="vRAM/VM", width=70, value=1, border="underline", label_style=config_label)
        self.storage=ft.TextField(label="Storage/VM(GB)", width=110, value=0, border="underline", label_style=config_label)
        self.cpu_usage=ft.TextField(label="CPU使用量/VM(MHZ)", width=150, value=0, border="underline", label_style=config_label)
        self.log_bandwith=ft.TextField(label="FT log 頻寬(KB/s)", width=140, value=0, disabled=True, border="underline", label_style=config_label)
        self.add_item_table=ft.DataTable(
            width=800,
            bgcolor="yellow",
            border=ft.border.all(2, "red"),
            border_radius=5,
            vertical_lines=ft.BorderSide(3, "blue"),
            horizontal_lines=ft.BorderSide(1, "green"),
            sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=30,
            data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
            show_checkbox_column=True,
            divider_thickness=0,
            column_spacing=10,
            data_row_max_height=30,
            data_row_min_height=20,
            columns=[
                ft.DataColumn(
                    ft.Text("項次", size=result_font_size, width=30),
                ),
                ft.DataColumn(
                    ft.Text("VM數量", size=result_font_size, width=50),
                ),
                 ft.DataColumn(
                    ft.Text("vCPU/VM", size=result_font_size, width=70),
                ),
                 ft.DataColumn(
                    ft.Text("vRAM/VM", size=result_font_size, width=70),
                ),
                ft.DataColumn(
                    ft.Text("Storage/VM(GB)", size=result_font_size, width=100),
                ),
                ft.DataColumn(
                    ft.Text("CPU使用量/VM(MHZ)", size=result_font_size, width=130),
                ),
                ft.DataColumn(
                    ft.Text("FT log 頻寬(KB/s)", size=result_font_size, width=110),
                ),
            ],
            rows=[
                 ft.DataRow([
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text("")),
                        ft.DataCell(ft.Text(""))
                     ],
                    color=ft.colors.WHITE,
                 ),
            ]
        )
        self.workload_section=ft.Container(
                                 bgcolor=ft.colors.LIGHT_BLUE_100,
                                 margin=5,
                                 padding=5,
                                 alignment=ft.alignment.center,
                                 expand=True,
                                 border_radius=10,
                                 content=ft.Column([ft.Text("Workload Configuration", weight=ft.FontWeight.BOLD, size=result_font_size),
                                                   ft.Divider(height=9, thickness=3, color=ft.colors.AMBER),
                                                   ft.Row([
                                                       self.vms,
                                                       self.vcpu,
                                                       self.vram,
                                                       self.storage,
                                                       self.cpu_usage,
                                                       self.log_bandwith,
                                                       ft.ElevatedButton("新增", on_click=self.on_add_workload_item),
                                                       ft.ElevatedButton("刪除", on_click=self.on_delete_workload_item),
                                                   ]),
                                                     self.add_item_table,
                                                      
                                                   
                                                   
                                 ])
                                )
        

        # Result section.
        ref_text=ft.Ref[ft.Text]()
        self.raw_capacity_value_ref=ref_text
        self.raw_cache_value_ref=ref_text
        self.pcpu_vcpu_value_ref=ref_text
        self.pram_vram_value_ref=ref_text
        self.cpu_total_volume_value_ref=ref_text
        self.cpu_consume_value_ref=ref_text
        self.cpu_free_value_ref=ref_text
        self.sys_reserve_space_value_ref=ref_text
        self.space_usage_value_ref=ref_text
        self.free_space_value_ref=ref_text
        self.sys_reserve_memory_value_ref=ref_text
        self.memory_usage_value_ref=ref_text
        self.free_memory_value_ref=ref_text
        self.total_log_bandwidth_ref=ref_text
        self.average_log_bandwidth_ref=ref_text

        self.raw_capacity=ft.Text(value="Raw Capacity", size=result_font_size, color=deep_orange)
        self.raw_cache=ft.Text(value="Raw Cache", size=result_font_size, color=deep_orange)
        self.pcpu_vcpu=ft.Text(value="pCPU : vCPU", size=result_font_size, color=deep_orange)
        self.pram_vram=ft.Text(value="pRAM : vRAM", size=result_font_size, color=deep_orange)
        self.cpu_total_volume=ft.Text(value="CPU總量(GHz)", size=result_font_size, color=deep_orange)
        self.cpu_consume=ft.Text(value="CPU耗用(GHz)", size=result_font_size, color=deep_orange)
        self.cpu_free=ft.Text(value="CPU可用(GHz)", size=result_font_size, color=deep_orange)
        self.sys_reserve_space=ft.Text(value="系統保留容量", size=result_font_size, color=deep_orange)
        self.space_usage=ft.Text(value="己用容量", size=result_font_size, color=deep_orange)
        self.free_space=ft.Text(value="可用容量", size=result_font_size, color=deep_orange)
        self.sys_reserve_memory=ft.Text(value="系統保留記憶體", size=result_font_size, color=deep_orange)
        self.memory_usage=ft.Text(value="己用記憶體", size=result_font_size, color=deep_orange)
        self.free_memory=ft.Text(value="可用記憶體", size=result_font_size, color=deep_orange)
        self.total_log_bandwidth=ft.Text(value="FT頻寛總計", size=result_font_size, color=deep_orange)
        self.average_log_bandwidth=ft.Text(value="平均FT頻寛/Node", size=result_font_size, color=deep_orange)

        self.raw_capacity_value=ft.Text(ref=self.raw_capacity_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.raw_cache_value=ft.Text(ref=self.raw_cache_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.pcpu_vcpu_value=ft.Text(ref=self.pcpu_vcpu_value_ref, value="0 : 0", size=result_font_size, color=black38)
        self.pram_vram_value=ft.Text(ref=self.pram_vram_value_ref, value="0 : 0", size=result_font_size, color=black38)
        self.cpu_total_volume_value=ft.Text(ref=self.cpu_total_volume_value_ref, value="0 GHZ", size=result_font_size, color=black38)
        self.cpu_consume_value=ft.Text(ref=self.cpu_consume_value_ref, value="0 GHZ", size=result_font_size, color=black38)
        self.cpu_free_value=ft.Text(ref=self.cpu_free_value_ref, value="0 GHZ", size=result_font_size, color=black38)
        self.sys_reserve_space_value=ft.Text(ref=self.sys_reserve_space_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.space_usage_value=ft.Text(ref=self.space_usage_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.free_space_value=ft.Text(ref=self.free_space_value_ref, value="0 TB", size=result_font_size, color=black38)
        self.sys_reserve_memory_value=ft.Text(ref=self.sys_reserve_memory_value_ref, value="0 GB", size=result_font_size, color=black38)
        self.memory_usage_value=ft.Text(ref=self.memory_usage_value_ref, value="0 GB", size=result_font_size, color=black38)
        self.free_memory_value=ft.Text(ref=self.free_memory_value_ref, value="0 GB", size=result_font_size, color=black38)
        self.total_log_bandwidth_value=ft.Text(ref=self.average_log_bandwidth_ref, value="0 KB/s", size=result_font_size, color=black38)
        self.average_log_bandwidth_value=ft.Text(ref=self.average_log_bandwidth_ref, value="0 KB/s", size=result_font_size, color=black38)
        self.result_datatable=ft.DataTable(
             columns=[
                 ft.DataColumn(self.raw_capacity),
                 ft.DataColumn(self.raw_cache),
                 ft.DataColumn(self.pcpu_vcpu),
                 ft.DataColumn(self.pram_vram),
                 ft.DataColumn(self.cpu_total_volume),
                 ft.DataColumn(self.cpu_consume),
                 ft.DataColumn(self.cpu_free),
                 ft.DataColumn(self.sys_reserve_space),
                 ft.DataColumn(self.space_usage),
                 ft.DataColumn(self.free_space),
                 ft.DataColumn(self.sys_reserve_memory),
                 ft.DataColumn(self.memory_usage),
                 ft.DataColumn(self.free_memory),
                 ft.DataColumn(self.total_log_bandwidth),
                 ft.DataColumn(self.average_log_bandwidth),
             ],
             rows=[
                 ft.DataRow([
                 ft.DataCell(self.raw_capacity_value),
                 ft.DataCell(self.raw_cache_value),
                 ft.DataCell(self.pcpu_vcpu_value),
                 ft.DataCell(self.pram_vram_value),
                 ft.DataCell(self.cpu_total_volume_value),
                 ft.DataCell(self.cpu_consume_value),
                 ft.DataCell(self.cpu_free_value),
                 ft.DataCell(self.sys_reserve_space_value),
                 ft.DataCell(self.space_usage_value),
                 ft.DataCell(self.free_space_value),
                 ft.DataCell(self.sys_reserve_memory_value),
                 ft.DataCell(self.memory_usage_value),
                 ft.DataCell(self.free_memory_value),
                 ft.DataCell(self.total_log_bandwidth_value),
                 ft.DataCell(self.average_log_bandwidth_value),
                ],
                 color=ft.colors.WHITE,
                ),
             ],
             bgcolor=ft.colors.GREEN_50,
             border=ft.border.all(2, "black"),
             border_radius=5,
             vertical_lines=ft.BorderSide(1, "black"),
             horizontal_lines=ft.BorderSide(1, "green"),
             heading_row_color=ft.colors.BLACK12,
             heading_row_height=30,
             data_row_color={ft.ControlState.HOVERED: "0x30FF0000"},
             column_spacing=10,
             expand=False,
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
                                                      ft.ElevatedButton("開始估算", on_click=self.on_result_calculate),
                                                    ]),
                                                   ft.Row([
                                                       ft.Container(
                                                           bgcolor=ft.colors.WHITE60,
                                                           margin=5,
                                                           padding=5,
                                                           alignment=ft.alignment.center,
                                                           expand=False,
                                                           border_radius=10,
                                                           content=ft.Row([
                                                               self.result_datatable,
                                                           ],
                                                           width=1250,
                                                           scroll=ft.ScrollMode.AUTO
                                                          )
                                                       ),
                                                   ]),
                                                  
                                        ])
                            
                            )

        self.controls=[ 
            ft.Row(
               spacing=10,
               width=1550,
               height=330,
               controls=[
                         self.vsan_section,
                         self.workload_section,
            ]),
            ft.Row(
                spacing=10,
                width=1300,
                height=300,
                controls=[
                          self.result_section,
                ]
            ),
        ]
        
    def on_result_calculate(self, e):
        raw_capacity=(float(self.diskgroup.value) * float(self.capacity.value) * 
                      float(self.capacity_qty.value) * float(self.hosts.value)
        )
        raw_cache=(float(self.diskgroup.value) * float(self.cache.value) *
                   float(self.cache_qty.value) * float(self.hosts.value)

        ) / 1000
        pcpu=int(self.hosts.value) * int(self.sockets.value) * int(self.cores.value)
        vcpu=int(self.vms.value) * int(self.vcpu.value)
        pvcpu_ratio=round(float(vcpu / pcpu), 3)
        pram=float(self.hosts.value) * float(self.memory.value)
        vram=float(self.vms.value) * float(self.vram.value)
        pvram_ration=round(float(vram / pram), 3)
        cpu_total=float(self.hosts.value) * float(self.sockets.value) * float(self.cores.value) * float(self.clock.value)
        sys_reserve_space=raw_capacity * 0.3
        space_usage=float(self.vms.value) * float(self.storage.value) * 2  # The multiple of 2 because of FTT=1 
        free_space=raw_capacity - sys_reserve_space - (space_usage / 1000)
        base_consumation=3                         # It is fixed 3GB consumation of vSAN, but if it more than 16 nodes than add 300MB.
        num_disk_groups=int(self.diskgroup.value)
        disk_group_base_consumption=500            # This is fixed 500MB consumed by each disk group.
        ssd_mem_overhead_per_gb=2                  # The 2MB for hybird and 7MB for all flash system.
        ssd_size=float(self.cache.value)
        sys_reserve_momory=((base_consumation + 8 + (num_disk_groups * (disk_group_base_consumption + (ssd_mem_overhead_per_gb * ssd_size)) / 1000))
                               * float(self.hosts.value)) # The esxi requires a minimum of 8 GB of physical RAM so that I add 8GB RAM for host reserve.
        memory_usage=float(self.vms.value) * float(self.vram.value)
        free_memory=((int(self.hosts.value) * float(self.memory.value)) - sys_reserve_momory - memory_usage )
        total_log_bandwidth=float(self.log_bandwith.value) * float(self.vms.value)
        average_log_bandwidth=total_log_bandwidth / float(self.hosts.value)

        self._check_min_memory()
        self._raw_capacity(raw_capacity=raw_capacity)
        self._raw_cache(raw_cache=raw_cache)
        self._pcpu_vcpu(pvcpu_ratio=pvcpu_ratio)
        self._pram_vram(pvram_ration=pvram_ration)
        self._cpu_total(cpu_total=cpu_total)
        self._sys_reserve_space(sys_reserve_space=sys_reserve_space)
        self._space_usage(space_usage=space_usage)
        self._free_space(free_space=free_space)
        self._sys_reserve_memory(sys_reserve_momory=sys_reserve_momory)
        self._memory_usage(memory_usage=memory_usage)
        self._free_memory(free_memory=free_memory)
        self._total_log_bandwidth(total_log_bandwidth=total_log_bandwidth)
        self._average_log_bandwidth(average_log_bandwidth=average_log_bandwidth)     
        
    def on_add_workload_item(self, e):
        rows_items=len(self.add_item_table.rows)
        if rows_items > 4:
            dlg = ft.AlertDialog(  
                 title=ft.Text("最多只可新增五個筆數"),
                 bgcolor=ft.colors.RED_300,
                 icon=ft.Icon(name=ft.icons.WARNING)
            )
            self.page.open(dlg)
            return
        
        if self.add_item_table.rows and not self.add_item_table.rows[0].cells[0].content.value:
            self.add_item_table.rows.pop()
            rows_items=0

        self.add_item_table.rows.append(
            ft.DataRow([
                        ft.DataCell(ft.Text(str(rows_items + 1))),
                        ft.DataCell(ft.Text(self.vms.value)),
                        ft.DataCell(ft.Text(self.vcpu.value)),
                        ft.DataCell(ft.Text(self.vram.value)),
                        ft.DataCell(ft.Text(self.storage.value)),
                        ft.DataCell(ft.Text(self.cpu_usage.value)),
                        ft.DataCell(ft.Text(self.log_bandwith.value)),
                     ],
                    color=ft.colors.WHITE,
                 )
        )
        self.add_item_table.update()

    def on_delete_workload_item(self, e):
        if self.add_item_table.rows:
           self.add_item_table.rows.pop()
           self.add_item_table.update()

    def _is_ft_enable(self, e):
        if self.log_bandwith.disabled is True:
           self.log_bandwith.disabled=False
        else:
           self.log_bandwith.disabled=True 
           self.log_bandwith.value=0   
        self.log_bandwith.update()

    def _check_min_memory(self):
        if int(self.memory.value) < 32:
           dlg = ft.AlertDialog(  
                 title=ft.Text("記憶體小於vSAN建議的32GB"),
                 bgcolor=ft.colors.RED_300,
                 icon=ft.Icon(name=ft.icons.WARNING)
           )
           self.page.open(dlg)

    def _raw_capacity(self, raw_capacity):
        self.raw_capacity_value_ref.current.value=str(round(raw_capacity, 2)) + " TB"
        self.raw_capacity_value.value=self.raw_capacity_value_ref.current.value
        self.raw_capacity_value.update()

    def _raw_cache(self, raw_cache):
        self.raw_cache_value_ref.current.value=str(round(raw_cache, 2)) + " TB"
        self.raw_cache_value.value=self.raw_cache_value_ref.current.value
        self.raw_cache_value.update()

    def _pcpu_vcpu(self, pvcpu_ratio):
        self.pcpu_vcpu_value_ref.current.value="1 : " + str(pvcpu_ratio)
        self.pcpu_vcpu_value.value=self.pcpu_vcpu_value_ref.current.value
        self.pcpu_vcpu_value.update()

    def _pram_vram(self, pvram_ration):
        self.pram_vram_value_ref.current.value="1 : " + str(pvram_ration)
        self.pram_vram_value.value=self.pram_vram_value_ref.current.value
        self.pram_vram_value.update()

    def _cpu_total(self, cpu_total):
        print(cpu_total)
        self.cpu_total_volume_value_ref.current.value=str(cpu_total) + " GHz"
        self.cpu_total_volume_value.value=self.cpu_consume_value_ref.current.value
        self.cpu_total_volume_value.update()

    def _sys_reserve_space(self, sys_reserve_space):
        self.sys_reserve_space_value_ref.current.value=str(round(float(sys_reserve_space), 3)) + " TB"
        self.sys_reserve_space_value.value=self.sys_reserve_space_value_ref.current.value
        self.sys_reserve_space_value.update()

    def _space_usage(self, space_usage):
        self.space_usage_value_ref.current.value=str(round(space_usage / 1000, 3)) + " TB"
        self.space_usage_value.value=self.space_usage_value_ref.current.value
        self.space_usage_value.update()

    def _free_space(self, free_space):
        self.free_space_value_ref.current.value=str(round(float(free_space), 3)) + " TB"
        self.free_space_value.value=self.free_space_value_ref.current.value
        self.free_space_value.update()

    def _sys_reserve_memory(self, sys_reserve_momory):
        self.sys_reserve_memory_value_ref.current.value=str(round(sys_reserve_momory, 3)) + " GB"
        self.sys_reserve_memory_value.value=self.sys_reserve_memory_value_ref.current.value
        self.sys_reserve_memory_value.update()
    
    def _memory_usage(self, memory_usage):
        self.memory_usage_value_ref.current.value=str(round(memory_usage, 3)) + " GB"
        self.memory_usage_value.value=self.memory_usage_value_ref.current.value
        self.memory_usage_value.update()

    def _free_memory(self, free_memory):
        self.free_memory_value_ref.current.value=str(round(free_memory, 3)) + " GB"
        self.free_memory_value.value=self.free_memory_value_ref.current.value
        self.free_memory_value.update()
    
    def _total_log_bandwidth(self, total_log_bandwidth):
        self.total_log_bandwidth_ref.current.value=str(round(float(total_log_bandwidth), 3)) + " KB/s"
        self.total_log_bandwidth_value.value=self.total_log_bandwidth_ref.current.value
        self.total_log_bandwidth_value.update()

    def _average_log_bandwidth(self, average_log_bandwidth):
        self.average_log_bandwidth_ref.current.value=str(round(float(average_log_bandwidth), 3)) + " KB/s"
        self.average_log_bandwidth_value.value=self.average_log_bandwidth_ref.current.value
        self.average_log_bandwidth_value.update()