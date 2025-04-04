import flet as ft
from db import init_db, save_preset, load_presets
from export import export_to_pdf


def main(page: ft.Page):
    """Основной класс приложения."""
    page.title = "Skating System Pro"
    page.theme_mode = ft.ThemeMode.LIGHT

    def on_resize(e):
        """Обработчик изменения размера окна."""
        print(f"Window resized to {page.window_width}x{page.window_height}")

    # Состояние
    dances = ["Вальс", "Танго", "Фокстрот"]
    dancers = [f"Участник {i + 1}" for i in range(6)]
    judges = [f"Судья {i + 1}" for i in range(5)]
    current_dance_idx = 0

    # Инициализация БД
    page.on_resize = on_resize
    init_db()

    # 1. Вкладки танцев (Drag-and-Drop)
    def move_dance(e: ft.DragTargetEvent):
        from_idx = int(e.data)
        to_idx = dances.index(e.control.content.content.value)
        dances.insert(to_idx, dances.pop(from_idx))
        update_dance_tabs()

    def update_dance_tabs():
        dance_tabs.controls = [
            ft.Draggable(
                group="dances",
                content=ft.DragTarget(
                    group="dances",
                    content=ft.Container(
                        content=ft.Text(dance),
                        padding=10,
                        border=ft.border.all(1),
                    ),
                    on_accept=move_dance,
                    data=str(idx),
                ),
            )
            for idx, dance in enumerate(dances)
        ]
        page.update()

    dance_tabs = ft.Row(scroll=True)

    # 2. Таблица участников (Drag-and-Drop)
    def move_dancer(e: ft.DragTargetEvent):
        from_idx = int(e.data)
        to_idx = dancers.index(e.control.content.value)
        dancers.insert(to_idx, dancers.pop(from_idx))
        update_dancer_table()

    def update_dancer_table():
        dancer_rows.controls = [
            ft.Draggable(
                group="dancers",
                content=ft.DragTarget(
                    group="dancers",
                    content=ft.Text(dancer),
                    on_accept=move_dancer,
                    data=str(idx),
                ),
            )
            for idx, dancer in enumerate(dancers)
        ]
        page.update()

    dancer_rows = ft.Column()
    dancers_list_view = ft.ListView(expand=True)

    # 3. Экспорт в PDF
    def on_export(e):
        export_to_pdf(dances, dancers, judges)
        page.snack_bar = ft.SnackBar(ft.Text("PDF сохранён!"))
        page.snack_bar.open = True
        page.update()

    # Интерфейс
    page.add(
        ft.AppBar(
            title=ft.Text("Skating System"),
            actions=[ft.IconButton(ft.icons.FILE_DOWNLOAD, on_click=on_export)],
        ),
        ft.Text("Танцы:"),
        dance_tabs,
        ft.Divider(),
        ft.Text("Участники:"),
        ft.Container(
            content=dancer_rows,
            height=300,
            border=ft.border.all(1),
            padding=10,
        ),
    )

    # Инициализация
    update_dance_tabs()
    update_dancer_table()


if __name__ == "__main__":
    ft.app(target=main)