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
        print("----------------------------- REPRODUTOR DE VIDEOS NO TERMINAL -------------------------------\n\n")
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
            if op == 0: exit()
            elif op == 1:
                list_menu()
            elif op == 2:
                download_menu()

def list_menu():
    op = 0
    while True:
        os.system('clear')
        print("----------------------------- Listar Videos -------------------------------\n\n")
        print("\t(1) - Pasta Padrao ("+DEFAULT_PATH+")")
        print("\t(2) - Digite um caminho valido")
        print("\t(3) - Reproduzir video")
        print("\t(4) - Voltar para o Menu Principal")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except:
            print("Digite um valor valido")
        finally:
            if op == 0: exit()
            elif op == 1:
                list_movies(DEFAULT_PATH)
                input()
            elif op == 2:
                path = input("Caminho(ex: /movies): ")
                list_movies(path)
                input()
            elif op == 3:
                title = input("Nome do Video:")
                play_movie(DEFAULT_PATH+"/"+title)
            elif op == 4:
                main_menu()

def download_menu():
    op = 0
    while True:
        os.system('clear')
        print("----------------------------- Baixar Videos do Youtube -------------------------------\n\n")
        print("\t(1) - PlayList Youtube")
        print("\t(3) - Voltar para o Menu Principal")
        print("\t(0) - Fechar Programa")
        print("---------------------------------------------------------------------------------------------")
        
        try:
            op = int(input("Opcoes(Digite o NUMERO Correspondente): "))
        except:
            print("Digite um valor valido")

        try:
            if op == 0: exit()
            elif op == 1:
                url, directory = (str(i) for i in input("Digite a url da Playlist: ").split())
                print(url+","+directory)
                downloadPlaylist(url, directory)
            elif op == 3:
                main_menu()
            input()
        except:
            print("Deve ter apenas dois argumentos. Formato correto: http://url directory")
            input()
            continue

    
main_menu()
    
