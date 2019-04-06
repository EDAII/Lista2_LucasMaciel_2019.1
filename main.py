import os
from searchMethods import *
from listArchives import *
from movie import *
from ytPlaylist import *

DEFAULT_PATH = './videos'


def main_menu():
    op = 0
    while True:
        os.system('clear')
        print("---------------------------------- PLAYTUBE TERMINATOR -------------------------------------\n\n")
        print("\t(1) - Listar Videos")
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
        print("\t(1) - Listar Videos")
        print("\t(2) - Reproduzir Lista")
        print("\t(3) - Reproduzir video")
        print("\t(4) - Voltar para Lista de Pastas")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except ValueError:
            print("Digite um valor valido")
            continue
        finally:
            if op == 0:
                exit()
            elif op == 1:
                videos = get_movies(path)
                list_movies(videos)
                input()
            elif op == 2:
                videos = get_movies(path)
                list_movies(videos)
                print("---------------------------------------------------------------------------------------------")
                for v in videos:
                    play_movie(path, v[0])
                    if v != videos[-1]:
                        op_play = str(input("Continuar lista de Reprodução?[S/N]"))
                        if op_play.lower() == 'n':
                            break
                input()
            elif op == 3:
                videos = get_movies(path)
                print("---------------------------------------------------------------------------------------------")
                list_movies(videos)
                print("---------------------------------------------------------------------------------------------")
                title = str(input("Video a ser reproduzido('nomevideo.mp4' ou 'indice'):"))
                play_movie(path, videos, title)
            elif op == 4:
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
                args = str(input("Digite a url da Playlist: "))
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
