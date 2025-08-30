import flet as ft
import time
from os import _exit, name
from random import choice, randint
from string import ascii_letters, punctuation

use_letters = False
use_digits = False
use_symbols = False

password = []
password_string = ""

def change_letters(e):
    global use_letters
    use_letters = e.control.value
    print(use_letters)

def change_digits(e):
    global use_digits
    use_digits = e.control.value
    print(use_digits)

def change_symbols(e):
    global use_symbols
    use_symbols = e.control.value
    print(use_symbols)

password_length_number = ft.TextField(value="8", text_align="center", width=64)

password_length = 0

def main(page: ft.Page):
    page.title = "Password Generator by Shady, v4"
    #page.window_window_icon = "assets/icon.ico"

    page.window.width = 640
    page.window.height = 480
    page.window.min_width = 400
    page.window.min_height = 300

    page.window.center()

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    title_text = ft.Text(value="Password Generator", size=36)
    continue_btn = ft.ElevatedButton("Continue")

    def button_clicked():
        print('рлп')

    page.add(title_text, continue_btn)

    def route_change(route):
        page.views.clear()
        
        # Welcome
        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Column(
                            [
                                ft.Text(value="Password Generator", size=36),
                                ft.ElevatedButton(content=ft.Text("Start", size=16), on_click=lambda _: page.go("/choose_symbols"), style=ft.ButtonStyle(padding=18))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        
        # Symbol Types Choice
        elif page.route == "/choose_symbols":
            page.views.append(
                ft.View(
                    "/choose_symbols",
                    [
                        ft.Column(
                            [
                                ft.Text(value="Select the characters to be used in the password", size=24),
                                ft.Row(
                                    [
                                        ft.Checkbox(label = "Letters", on_change=lambda e: change_letters(e)),
                                        ft.Checkbox(label = "Digits", on_change=lambda e: change_digits(e)),
                                        ft.Checkbox(label = "Symbols", on_change=lambda e: change_symbols(e))
                                    ], 
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.ElevatedButton(content=ft.Text("Done", size=14), on_click=lambda _: page.go("/password_length"), style=ft.ButtonStyle(padding=14))
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )
        
        # Password Length
        elif page.route == "/password_length":
            page.views.append(
                ft.View(
                    "/password_length",
                    [
                        ft.Column(
                            [
                                ft.Text(value="Set the password length", size=24),
                                ft.Row(
                                    [
                                        ft.IconButton(ft.Icons.REMOVE, on_click=lambda e: minus_click(e)),
                                        password_length_number,
                                        ft.IconButton(ft.Icons.ADD, on_click=lambda e: plus_click(e)),
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.ElevatedButton(
                                    content=ft.Text("Done", size=14),
                                    on_click=lambda _: generate_password(),
                                    style=ft.ButtonStyle(padding=14)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                )
            )

        # Your Password
        elif page.route == "/your_password":
            page.views.append(
                ft.View(
                    "/your_password",
                    [
                        ft.Column(
                            [
                                ft.Text(value="Your Password", size=24),
                                ft.Text(value=password_string, size=36, selectable=True),
                                ft.ElevatedButton(
                                    content=ft.Text("Done", size=14),
                                    on_click=lambda _: page.go("/"),
                                    style=ft.ButtonStyle(padding=14)
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # No Password
        elif page.route == "/no_password":
            page.views.append(
                ft.View(
                    "/no_password",
                    [
                        ft.Column(
                            [
                                ft.Text(value="You decided that you don\'t need a password.", size=18, text_align=ft.TextAlign.CENTER),
                                ft.Text(value="Have you changed your mind?", size=24, text_align=ft.TextAlign.CENTER),
                                ft.Row(
                                    [
                                        ft.ElevatedButton(
                                        content=ft.Text("Yes", size=16),
                                        on_click=lambda _: page.go("/"),
                                        style=ft.ButtonStyle(padding=16)
                                        ),
                                        ft.ElevatedButton(
                                        content=ft.Text("No", size=16),
                                        on_click=lambda _: page.go("/hackers_never_sleep"),
                                        style=ft.ButtonStyle(padding=16)
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                )
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )

        # Hackers never sleep
        elif page.route == "/hackers_never_sleep":
            page.views.append(
                ft.View(
                    "/hackers_never_sleep",
                    [
                        ft.Column(
                            [
                                ft.Text(value="Ok, but remember.", size=18, text_align=ft.TextAlign.CENTER),
                                ft.Text(value="Hackers never sleep 😈", size=24, text_align=ft.TextAlign.CENTER),
                                ft.ElevatedButton(
                                    content=ft.Text("Exit", size=18),
                                    on_click=lambda _: os._exit(0),
                                    style=ft.ButtonStyle(padding=18)
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand = True
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                )
            )
        
        page.update()

    def generate_password():
        global password, password_string

        password_length = int(password_length_number.value)

        print(password_length)
        print(use_letters, use_digits, use_symbols)

        if password_length > 0:
            for i in range(password_length):
            
                if use_letters == False and use_digits == False and use_symbols == True: #001
                    password.append(choice(punctuation))
                elif use_letters == False and use_digits == True and use_symbols == False: # 010
                    password.append(randint(0,9))
                elif use_letters == False and use_digits == True and use_symbols == True:   #011
                    charType = randint(0, 1)
                    if charType == 0:
                        password.append(randint(0,9))
                    elif charType == 1:
                        password.append(choice(punctuation))
                elif use_letters == True and use_digits == False and use_symbols == False:   #100
                    password.append(choice(ascii_letters))
                elif use_letters == True and use_digits == False and use_symbols == True:   #101
                    charType = randint(0, 1)
                    if charType == 0:
                        password.append(choice(ascii_letters))
                    elif charType == 1:
                        password.append(choice(punctuation))
                elif use_letters == True and use_digits == True and use_symbols == False:   #110
                    charType = randint(0, 1)
                    if charType == 0:
                        password.append(choice(ascii_letters))
                    elif charType == 1:
                        password.append(randint(0,9))
                elif use_letters == True and use_digits == True and use_symbols == True:   #111
                    charType = randint(0, 2)
                    if charType == 0:
                        password.append(randint(0,9))
                    elif charType == 1:
                        password.append(choice(ascii_letters))
                    elif charType == 2:
                        password.append(choice(punctuation))
                elif use_letters == False and use_digits == False and use_symbols == False: #000
                    break
                
            password_string = ' '.join(str(char) for char in password)
            password_string = password_string.replace(' ', '')

        if use_letters == True or use_digits == True or use_symbols == True:
            if password_length > 0:
                page.go("/your_password")
            else: page.go("/no_password")
        else: page.go("/no_password")

    def minus_click(e):
        password_length_number.value = str(int(password_length_number.value) - 1)
        refresh_page()

    def plus_click(e):
        password_length_number.value = str(int(password_length_number.value) + 1)
        refresh_page()

    def refresh_page():
        current_route = page.route
        page.go(current_route)

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, assets_dir="assets")