import os
from sortMethods import *
from listArchives import *
from movie import *
from ytPlaylist import *

DEFAULT_PATH = './videos'


def main_menu():
    op = 0
    while True:
        os.system('clear')
        print(" ____  _        _ __   _______ _   _ ____  _____ ")
        print("|  _ \| |      / \\\ \\ / /_   _| | | | __ )| ____|")
        print("| |_) | |     / _ \\\ V /  | | | | | |  _ \\|  _|  ")
        print("|  __/| |___ / ___ \| |   | | | |_| | |_) | |___ ")
        print("|_|   |_____/_/   \_\_|   |_|  \___/|____/|_____|")
        print(" _____ _____ ____  __  __ ___ _   _    _  _____ ___  ____  ")
        print("|_   _| ____|  _ \|  \/  |_ _| \ | |  / \|_   _/ _ \|  _ \ ")
        print("  | | |  _| | |_) | |\/| || ||  \| | / _ \ | || | | | |_) |")
        print("  | | | |___|  _ <| |  | || || |\  |/ ___ \| || |_| |  _ < ")
        print("  |_| |_____|_| \_\_|  |_|___|_| \_/_/   \_\_| \___/|_| \_\\")
        print("---------------------------------- PLAYTUBE TERMINATOR -------------------------------------\n\n")
        print("\t(1) - Listar de Pastas")
        print("\t(2) - Baixar PlayList do Youtube")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except:
            print("Digite um valor valido")
            continue
        finally:
            if op == 0:
                exit()
            elif op == 1:
                list_menu()
            elif op == 2:
                download_menu()


def list_menu():
    op = 0
    while True:
        os.system('clear')
        print("------------------------------------- Lista de Pastas -------------------------------------\n\n")
        print("\t(1) - Pasta Padrao ("+DEFAULT_PATH+")")
        print("\t(2) - Outras Pastas")
        print("\t(3) - Mostrar pastas disponiveis")
        print("\t(4) - Voltar para o Menu Principal")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except:
            print("Digite um valor valido")
        
        if op == 0:
            exit()
        elif op == 1:
            play_menu(DEFAULT_PATH)
            input()
        elif op == 2:
            list_dir()
            print("---------------------------------------------------------------------------------------------")
            path = str(input("Caminho(ex: /movies): "))
            if not os.path.exists(path):
                print("Pasta não encontrada")
                input()
                continue
            play_menu(path)
            input()
        elif op == 3:
            list_dir()
            input()
        elif op == 4:
            main_menu()


def play_menu(path):
    op = 0
    while True:
        os.system('clear')
        print("---------------------------------- Lista de Reprodução -------------------------------------")
        print("pasta atual: "+path+"\n\n")
        print("\t(1) - Listar Videos(default = title and ascendent)\n\t\t(options sort: -dr = duration, -dt = date, -D = descendent)")
        print("\t(2) - Reproduzir Lista(default = title and ascendent)")
        print("\t(3) - Reproduzir video")
        print("\t(4) - Voltar para Lista de Pastas")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        try:
            op = input("Opcoes(Digite o NUMERO Correspondente): ")
        except ValueError:
            print("Digite um valor valido")
            continue
        finally:
            if op == '0':
                exit()
            elif op[0] == '1':
                op_field = 0    # campo a ser ordenado (title, duration, date)
                op_ord = 0      # ordenacao (ascendente ou descendente 0 - asc, 1 - desc)
                if '-dr' in op:
                    op_field = 1
                elif '-dt' in op:
                    op_field = 2
                
                if '-D' in op:
                    op_ord = 1

                videos = get_movies(path)
                list_movies(videos, op_field, op_ord)
                input()
            elif op[0] == '2':
                op_field = 0    # campo a ser ordenado (title, duration, date)
                op_ord = 0      # ordenacao (ascendente ou descendente 0 - asc, 1 - desc)
                if '-dr' in op:
                    op_field = 1
                elif '-dt' in op:
                    op_field = 2
                
                if '-D' in op:
                    op_ord = 1

                videos = get_movies(path)
                videos = list_movies(videos, op_field, op_ord)
                print("---------------------------------------------------------------------------------------------")
                for v in videos:
                    play_movie(path, videos, v[0])
                    if v != videos[-1]:
                        op_play = str(input("Continuar lista de Reprodução?[S/N]"))
                        if op_play.lower() == 'n':
                            break
            elif op == '3':
                videos = get_movies(path)
                print("---------------------------------------------------------------------------------------------")
                list_movies(videos)
                print("---------------------------------------------------------------------------------------------")
                title = str(input("Video a ser reproduzido('nomevideo.mp4' ou 'indice'):"))
                play_movie(path, videos, title)
            elif op == '4':
                list_menu()


def download_menu():
    op = 0
    while True:
        os.system('clear')
        print("---------------------------------- Baixar Videos do Youtube ---------------------------------\n\n")
        print("\t(1) - PlayList Youtube")
        print("\t(2) - Voltar para o Menu Principal")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")

        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except:
            print("Digite um valor valido")

        if op == 0:
            exit()
        elif op == 1:
            try:
                args = str(input("Digite a url da Playlist(https://www.youtube.com/playlist?list=url pasta(opcional)): "))
                args = args.split()
                url = args[0]

                if (len(args) == 1):
                    downloadPlaylist(url, DEFAULT_PATH)
                elif (len(args) == 2):
                    directory = args[1]
                    downloadPlaylist(url, directory)
                input("\nConcluído! Pressione [Enter] para Continuar")
            except IndexError:
                print("Deve ter apenas dois argumentos. Formato correto: http://url directory")
                input()
                continue
        elif op == 2:
            main_menu()


main_menu()
