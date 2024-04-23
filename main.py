import flet as ft


def main(page: ft.page):
    page.bgcolor = ft.colors.BLACK
    page.scrollable = True

    def change_main_image(e):
        for element in options.controls:
            if element == e.control:
                element.opacity = 1
                main_image.src = element.image_src
            else:
                element.opacity = 0.5
        main_image.update()
        options.update()

    product_images = ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9 / 16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                main_image := ft.Image(
                    src='assets/img/couch_1.png',
                ),
                options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            image_src='assets/img/couch_1.png',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src='assets/img/couch_2.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                        ft.Container(
                            image_src='assets/img/couch_3.png',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image,
                        ),
                    ]
                )
            ]
        )
    )
    product_details = ft.Container(
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9 / 16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='chairs'.upper(),
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),
                ft.Text(
                    value='Modern Yellow Couch',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),
                ft.Text(
                    value='Living Room',
                    color=ft.colors.GREY,
                    italic=True,

                ),
                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 339',
                            color=ft.colors.WHITE,
                            size=28),
                        ft.Row(controls=[ft.Icon(
                            col={'xs': 12, 'sm': 6},
                            name=ft.icons.STAR,
                            color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                        ) for _ in range(5)]),
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Description',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value= 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro.' +
                                    'De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo ' +
                                    'vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. ' +
                                    'Hi mindless mortuis soulless creaturas, imo evil stalking monstra adventus resi ' +
                                    'dentevil vultus comedat cerebella viventium. Qui animated corpse, cricket bat ' +
                                    'max brucks terribilem incessu zomby. The voodoo sacerdos flesh eater, suscitat ' +
                                    'mortuos comedere carnem virus. Zonbi tattered for solum oculi eorum defunctis go ' +
                                    'lum cerebro. Nescio brains an Undead zombies. Sicut malus putrid voodoo horror. ' +
                                    'Nigh tofth eliv ingdead.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.Tab(
                            text='Details',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro.' +
                                          'De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo ' +
                                          'vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. ' +
                                          'Hi mindless mortuis soulless creaturas, imo evil stalking monstra adventus resi ' +
                                          'mortuos comedere carnem virus. Zonbi tattered for solum oculi eorum defunctis go ' +
                                          'lum cerebro. Nescio brains an Undead zombies. Sicut malus putrid voodoo horror. ' +
                                          'Nigh tofth eliv ingdead.',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),
                        ft.ResponsiveRow(
                            columns=12,
                            controls=[
                                ft.Dropdown(
                                    col=6,
                                    label='Color',
                                    label_style=ft.TextStyle(),
                                )
                            ]
                        ),
                    ]
                ),
            ]
        )
    )
    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                ft.Column(col=6, controls=[product_images, ]),
                ft.Column(col=6, controls=[product_details, ]),
            ]
        )

    )
    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main, assets_dir='assets')
