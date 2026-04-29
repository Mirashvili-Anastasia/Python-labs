"""
Запускающий модуль для лабораторных работ №4-6 (Вариант 6)
CLI интерфейс на Typer
"""

import typer
from rich import print as rprint
from rich.table import Table
from rich.panel import Panel
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from package import (
intersect,root,intersect_recursive,root_iterative,fibonacci_closure,cache_decorator,PasswordGenerator
)

app = typer.Typer(help="Лабораторные работы №4-6 - Вариант 6", add_completion=False)
console = Console()


# ==================== ЛАБОРАТОРНАЯ №4 ====================

@app.command()
def lab4():
    """Лабораторная №4: рекурсивные и итеративные алгоритмы"""
    rprint(Panel.fit("[bold cyan]Лабораторная работа №4 - Вариант 6[/bold cyan]", border_style="cyan"))

    rprint("\n[yellow]Выберите программу:[/yellow]")
    rprint("  [green]1.[/green] Распаковка списка (рекурсивно)")
    rprint("  [green]2.[/green] Распаковка списка (итеративно)")
    rprint("  [green]3.[/green] Последовательность w_i (рекурсивно)")
    rprint("  [green]4.[/green] Последовательность w_i (итеративно)")

    choice = typer.prompt("\nВаш выбор", default="1")

    if choice == "1":
        # Распаковка рекурсивно
        data_str = typer.prompt(
            "Введите данные для распаковки",
            default="[None, [1, ({2, 3}, {'foo': 'bar'})]]"
        )
        try:
            data = eval(data_str)
            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                    transient=True
            ) as progress:
                progress.add_task(description="Распаковка...", total=None)
                result = unpack_recursive(data)
            rprint(f"\n[green]Результат распаковки:[/green] {result}")
            rprint(f"[dim]Количество элементов: {len(result)}[/dim]")
        except Exception as e:
            rprint(f"[red]Ошибка: {e}[/red]")

    elif choice == "2":
        # Распаковка итеративно
        data_str = typer.prompt(
            "Введите данные для распаковки",
            default="[None, [1, ({2, 3}, {'foo': 'bar'})]]"
        )
        try:
            data = eval(data_str)
            result = unpack_iterative(data)
            rprint(f"\n[green]Результат распаковки:[/green] {result}")
            rprint(f"[dim]Количество элементов: {len(result)}[/dim]")
        except Exception as e:
            rprint(f"[red]Ошибка: {e}[/red]")

    elif choice == "3":
        # Последовательность рекурсивно
        try:
            i = typer.prompt("Введите номер члена последовательности (i)", type=int)
            if i <= 0:
                rprint("[red]Ошибка: номер должен быть положительным![/red]")
                return

            with Progress(
                    SpinnerColumn(),
                    TextColumn("[progress.description]{task.description}"),
                    console=console,
                    transient=True
            ) as progress:
                progress.add_task(description=f"Вычисление w_{i}...", total=None)
                result = sequence_recursive(i)

            rprint(f"\n[green]w_{i} = {result}[/green]")

            # Вывод дополнительной информации
            if i <= 10:
                rprint("[dim]Примечание: вычислено рекурсивно[/dim]")
            else:
                rprint("[yellow]Внимание: при больших i рекурсия может быть медленной[/yellow]")

        except ValueError:
            rprint("[red]Ошибка: введите целое число![/red]")
        except RecursionError:
            rprint("[red]Ошибка: слишком глубокий уровень рекурсии! Попробуйте меньшее число (≤ 20)[/red]")

    elif choice == "4":
        # Последовательность итеративно
        try:
            i = typer.prompt("Введите номер члена последовательности (i)", type=int)
            if i <= 0:
                rprint("[red]Ошибка: номер должен быть положительным![/red]")
                return

            result = sequence_iterative(i)
            rprint(f"\n[green]w_{i} = {result}[/green]")

            # Вывод таблицы для наглядности
            if i <= 10:
                rprint("\n[dim]Первые члены последовательности:[/dim]")
                table = Table(show_header=True, header_style="bold cyan")
                table.add_column("i", style="yellow", justify="center")
                table.add_column("w_i", style="green")
                for j in range(1, i + 1):
                    table.add_row(str(j), f"{sequence_iterative(j):.10f}")
                rprint(table)

        except ValueError:
            rprint("[red]Ошибка: введите целое число![/red]")

    else:
        rprint("[red]Ошибка: неверный выбор! Введите 1, 2, 3 или 4[/red]")


# ==================== ЛАБОРАТОРНАЯ №5 ====================

@app.command()
def lab5():
    """Лабораторная №5: замыкания и декораторы"""
    rprint(Panel.fit("[bold magenta]Лабораторная работа №5 - Вариант 6[/bold magenta]", border_style="magenta"))

    rprint("\n[yellow]Выберите программу:[/yellow]")
    rprint("  [green]1.[/green] Замыкание для чтения файла")
    rprint("  [green]2.[/green] Декоратор с логированием")

    choice = typer.prompt("\nВаш выбор", default="1")

    if choice == "1":
        # Замыкание для чтения файла
        filename = typer.prompt("Введите имя файла", default="test.txt")

        try:
            reader = get_file_reader(filename)
            rprint(f"\n[green]Содержимое файла '{filename}':[/green]")

            line_num = 1
            lines = []
            while True:
                line = reader()
                if line is None:
                    break
                lines.append((line_num, line.rstrip('\n')))
                line_num += 1

            if not lines:
                rprint("[dim]  (файл пуст)[/dim]")
            else:
                table = Table(show_header=True, header_style="bold green")
                table.add_column("№", style="cyan", justify="center")
                table.add_column("Строка", style="white")
                for num, line in lines:
                    table.add_row(str(num), line[:80] + "..." if len(line) > 80 else line)
                rprint(table)

            rprint(f"[dim]Всего строк: {line_num - 1}[/dim]")

        except FileNotFoundError:
            rprint(f"[red]Ошибка: файл '{filename}' не найден![/red]")
            rprint("[dim]Создайте файл или укажите правильное имя[/dim]")
        except Exception as e:
            rprint(f"[red]Ошибка: {e}[/red]")

    elif choice == "2":
        # Декоратор с логированием
        rprint("\n[green]Демонстрация работы декоратора логирования:[/green]")

        @log_c
        def multiply(a: float, b: float) -> float:
            """Умножает два числа"""
            return a * b

        @log_c
        def power(base: float, exp: int) -> float:
            """Возводит число в степень"""
            return base ** exp

        @log_c
        def divide(a: float, b: float) -> float:
            """Делит одно число на другое"""
            if b == 0:
                raise ValueError("Деление на ноль!")
            return a / b

        rprint("\n[bold]--- Пример 1: multiply(5, 6) ---[/bold]")
        result1 = multiply(5, 6)
        rprint(f"[dim]Результат: {result1}[/dim]\n")

        rprint("[bold]--- Пример 2: power(2, 10) ---[/bold]")
        result2 = power(2, 10)
        rprint(f"[dim]Результат: {result2}[/dim]\n")

        rprint("[bold]--- Пример 3: divide(10, 2) ---[/bold]")
        result3 = divide(10, 2)
        rprint(f"[dim]Результат: {result3}[/dim]\n")

        rprint("[bold]--- Пример 4: multiply(5, 6) [повторно, должен быть в логах] ---[/bold]")
        result4 = multiply(5, 6)
        rprint(f"[dim]Результат: {result4}[/dim]\n")

        rprint("[bold]--- Пример 5: divide(10, 0) [ошибка] ---[/bold]")
        try:
            result5 = divide(10, 0)
        except ValueError as e:
            rprint(f"[red]Поймана ошибка: {e}[/red]")

    else:
        rprint("[red]Ошибка: неверный выбор! Введите 1 или 2[/red]")


# ==================== ЛАБОРАТОРНАЯ №6 ====================

@app.command()
def lab6():
    """Лабораторная №6: генератор простых чисел (решето Эратосфена)"""
    rprint(Panel.fit("[bold green]Лабораторная работа №6 - Вариант 6[/bold green]", border_style="green"))

    rprint("\n[cyan]Программа: Генератор простых чисел[/cyan]")
    rprint("[dim]Используется алгоритм «Решето Эратосфена»[/dim]\n")

    try:
        start = typer.prompt("Введите нижнюю границу", type=int)
        end = typer.prompt("Введите верхнюю границу", type=int)

        if start < 2:
            rprint("[yellow]Внимание: простые числа начинаются с 2. Устанавливаю start = 2[/yellow]")
            start = 2

        if start > end:
            rprint(f"[red]Ошибка: нижняя граница ({start}) больше верхней ({end})[/red]")
            return

        with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
                transient=True
        ) as progress:
            progress.add_task(description="Поиск простых чисел...", total=None)
            primes = generate_primes(start, end)

        if not primes:
            rprint(f"\n[yellow]Простых чисел в диапазоне [{start}, {end}] не найдено[/yellow]")
        else:
            # Вывод результатов в таблице
            rprint(f"\n[green]Простые числа в диапазоне [{start}, {end}]:[/green]")

            # Разбиваем на колонки для красивого вывода
            per_row = 10
            table = Table(show_header=False, show_lines=False)
            for _ in range(per_row):
                table.add_column(style="green", justify="center")

            rows = []
            for i in range(0, len(primes), per_row):
                rows.append(primes[i:i + per_row])

            for row in rows:
                table.add_row(*[str(x) for x in row])

            rprint(table)
            rprint(f"\n[bold]Всего найдено: {len(primes)} простых чисел[/bold]")

            # Дополнительная статистика
            if primes:
                rprint(f"[dim]Минимальное: {primes[0]}, Максимальное: {primes[-1]}[/dim]")

    except ValueError:
        rprint("[red]Ошибка: введите целые числа![/red]")


# ==================== ИНТЕРАКТИВНОЕ МЕНЮ ====================

@app.command()
def menu():
    """Интерактивное меню для выбора лабораторной работы"""
    console.clear()

    # Красивый заголовок
    title = Panel.fit(
        "[bold cyan]Лабораторные работы №4-6[/bold cyan]\n[dim]Вариант 6[/dim]",
        border_style="cyan"
    )
    rprint(title)

    # Таблица с описанием
    table = Table(title="[bold yellow]Доступные лабораторные работы[/bold yellow]",
                  title_style="bold yellow",
                  show_header=True,
                  header_style="bold white")

    table.add_column("№", style="cyan", justify="center", width=6)
    table.add_column("Название", style="magenta", width=25)
    table.add_column("Описание", style="green", width=40)
    table.add_column("Кол-во программ", style="yellow", justify="center", width=15)

    table.add_row("4", "Рекурсия и итерация",
                  "Распаковка списков, последовательность w_i", "4")
    table.add_row("5", "Замыкания и декораторы",
                  "Чтение файлов, логирование вызовов", "2")
    table.add_row("6", "Решето Эратосфена",
                  "Генератор простых чисел", "1")

    rprint(table)

    choice = typer.prompt("\n[bold]Введите номер лабораторной работы[/bold] (4-6) или [red]q[/red] для выхода",
                          default="q")

    if choice == "4":
        lab4()
    elif choice == "5":
        lab5()
    elif choice == "6":
        lab6()
    elif choice.lower() == "q":
        rprint("[green]До свидания! 👋[/green]")
        raise typer.Exit()
    else:
        rprint("[red]Ошибка: введите 4, 5, 6 или q[/red]")
        menu()


# ==================== ОТДЕЛЬНЫЕ КОМАНДЫ ДЛЯ УДОБСТВА ====================

@app.command()
def unpack(data: str = typer.Argument(..., help="Данные для распаковки"),
           recursive: bool = typer.Option(True, "--recursive", "-r", help="Использовать рекурсивную версию")):
    """
    Быстрая команда для распаковки списка
    """
    try:
        parsed_data = eval(data)
        if recursive:
            result = unpack_recursive(parsed_data)
        else:
            result = unpack_iterative(parsed_data)
        rprint(f"[green]Результат:[/green] {result}")
        rprint(f"[dim]Количество элементов: {len(result)}[/dim]")
    except Exception as e:
        rprint(f"[red]Ошибка: {e}[/red]")


@app.command()
def sequence(i: int = typer.Argument(..., help="Номер члена последовательности"),
             iterative: bool = typer.Option(False, "--iterative", "-i", help="Использовать итеративную версию")):
    """
    Быстрая команда для вычисления последовательности w_i
    """
    try:
        if i <= 0:
            rprint("[red]Ошибка: i должно быть положительным[/red]")
            return

        if iterative:
            result = sequence_iterative(i)
            rprint(f"[green]w_{i} = {result} (итеративно)[/green]")
        else:
            result = sequence_recursive(i)
            rprint(f"[green]w_{i} = {result} (рекурсивно)[/green]")
    except RecursionError:
        rprint("[red]Ошибка: слишком глубокая рекурсия (i ≤ 20 для рекурсивной версии)[/red]")


@app.command()
def file_reader(filename: str = typer.Argument(..., help="Имя файла для чтения")):
    """
    Быстрая команда для чтения файла через замыкание
    """
    try:
        reader = get_file_reader(filename)
        rprint(f"[green]Файл '{filename}':[/green]")
        line_num = 1
        while True:
            line = reader()
            if line is None:
                break
            rprint(f"  {line_num}. {line.rstrip()}")
            line_num += 1
        if line_num == 1:
            rprint("  (файл пуст)")
        else:
            rprint(f"[dim]Всего строк: {line_num - 1}[/dim]")
    except FileNotFoundError:
        rprint(f"[red]Ошибка: файл '{filename}' не найден[/red]")


@app.command()
def primes(start: int = typer.Argument(..., help="Нижняя граница"),
           end: int = typer.Argument(..., help="Верхняя граница")):
    """
    Быстрая команда для поиска простых чисел
    """
    try:
        if start < 2:
            start = 2
        primes_list = generate_primes(start, end)
        if primes_list:
            rprint(f"[green]Простые числа в [{start}, {end}]:[/green]")
            rprint(f"{primes_list}")
            rprint(f"[dim]Всего: {len(primes_list)}[/dim]")
        else:
            rprint(f"[yellow]Простых чисел в диапазоне [{start}, {end}] не найдено[/yellow]")
    except Exception as e:
        rprint(f"[red]Ошибка: {e}[/red]")


# ==================== ТОЧКА ВХОДА ====================

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    CLI для лабораторных работ №4-6 (Вариант 6)
    """
    if ctx.invoked_subcommand is None:
        menu()


if __name__ == "__main__":
    app()