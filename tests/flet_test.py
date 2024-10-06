import flet as ft

# 定义一个全局变量来存储列表值
shared_list = []

class HomePage(ft.View):
    def __init__(self, page):
        super().__init__(route="/")
        self.page = page
        self.page.title = "Home Page"
        self.page.add(ft.Text("Home Page"))
        self.page.add(ft.ElevatedButton("Go to List Page", on_click=self.go_to_list_page))

    def go_to_list_page(self, e):
        global shared_list
        shared_list = [1, 2, 3, 4, 5]  # 设置列表值
        self.page.go("/list")

class ListPage(ft.View):
    def __init__(self, page):
        super().__init__(route="/list")
        self.page = page
        self.page.title = "List Page"
        self.page.add(ft.Text("List Page"))
        self.page.add(ft.ElevatedButton("Go to Home Page", on_click=self.go_to_home_page))
        self.display_list()

    def display_list(self):
        global shared_list
        for item in shared_list:
            self.page.add(ft.Text(f"Item: {item}"))

    def go_to_home_page(self, e):
        self.page.go("/")

def main(page: ft.Page):
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(HomePage(page))
        elif page.route == "/list":
            page.views.append(ListPage(page))
        page.update()

    page.on_route_change = route_change
    page.go(page.route)

ft.app(target=main)
