"""
Copyright [yyyy] [name of copyright owner] Licensed under the Educational 
Community License, Version 2.0 (the “License”); you may not use this file 
except in compliance with the License. You may obtain a copy of the License at 
http://www.osedu.org/licenses/ECL-2.0 Unless required by applicable law or 
agreed to in writing, software distributed under the License is distributed on an 
“AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, 
either express or implied. See the License for the specific language governing 
permissions and limitations under the License.
"""

import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_welcome = ft.Text("Welcome to the counter example")
    welcome_row = ft.Row([txt_welcome], alignment=ft.MainAxisAlignment.CENTER)
    page.add(welcome_row)

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )


ft.app(port=8080, target=main, view=ft.AppView.WEB_BROWSER)
