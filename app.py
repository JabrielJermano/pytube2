from pytube import YouTube
from pytube import Playlist
import os
resolucoes = []
url_video = "https://www.youtube.com/watch?v="
nomes_proibidos = ["CON", "PRN", "AUX", "CLOCK$", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", 
"LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]


def baixar_playlist():
    while True:
        os.system('cls')
        url = input("Digite o URL da playlist do YouTube: ")
        if url.startswith(url_video) and "list" in url:
            p = Playlist(url)
            print(p.title)
            opcao = input("Esta é a playlist que você quer baixar? Digite 1 para continuar, 2 para digitar outro URL e 3 para sair: ")
            if opcao == "1":
                while True:
                    nome = input("Digite um nome para criar uma pasta com os vídeos da playlist: ")
                    if nome.upper() in nomes_proibidos:
                        input("Não se pode criar uma pasta com esse nome por regras do Windows, digite qualquer coisa para continuar: ")
                    else:
                        break
                print("Baixando...")
                for video in p.videos:
                    video.streams.first().download(r"C:\Users\Fic\Videos/"+nome)
                input("Download concluído, digite qualquer coisa para continuar: ")
            elif opcao == "2":
                continue
            else:
                break
        else:
            input("O URL digitado não é de uma playlist do YouTube ou não é um URL válido. Digite qualquer coisa para continuar: ")
        break    
            
def baixar_video():
    while True:
        os.system('cls')
        url = input("Digite o URL do vídeo do YouTube: ")
        if url.startswith(url_video) and not "list" in url:
            yt = YouTube(url)
            print(yt.title, ", do canal " , yt.author)
            opcao = input("Este é o vídeo que você quer baixar? Digite 1 para continuar, 2 para digitar outro URL e 3 para sair: ")
            if opcao == "1":
                for resolucao in yt.streams:
                    if resolucao in resolucoes:
                        continue
                    else:
                        resolucoes.append(resolucao.resolution)
                while True:
                    try:
                        resolucao_escolhida = int(input("Digite a resolução desejada (apenas o número da resolução): "))
                        resolucao_escolhida = str(resolucao_escolhida) + "p"
                    except ValueError:
                        continue
                    if resolucao_escolhida in resolucoes:
                        print("Baixando...")
                        yt.streams.filter(res=resolucao_escolhida).first().download(r"C:\Users\Fic\Videos")
                        input("Vídeo baixado, digite qualquer coisa para continuar: ")
                        resolucoes.clear()
                        break
                    else:
                        print("O vídeo não está disponível nesta resolução, escolha outra")
                break
            elif opcao == "2":
                continue
            else:
                break
        else:
            print("URL inválido, certifique-se de que o URL digitado começa com 'https://www.youtube.com/watch?v=' e de que seja de um vídeo")
            input("Digite qualquer coisa para continuar: ")
        break
def baixar_audio():
    while True:
        os.system('cls')
        url = input("Digite o URL do vídeo do YouTube: ")
        if url.startswith(url_video) and not "list" in url:
            yt = YouTube(url)
            print(yt.title, ", do canal " , yt.author)
            opcao = input("Este é o vídeo cujo áudio você quer baixar? Digite 1 para continuar, 2 para digitar outro URL e 3 para sair: ")
            if opcao == "1":
                print("Baixando...")
                yt.streams.get_audio_only().download(r"C:\Users\Fic\Videos/", yt.title + ".mp3")
                input("Áudio baixado, digite qualquer coisa para continuar: ")
                break
            elif opcao == "2":
                continue
            else:
                break
        else:
            print("URL inválido, certifique-se de que o URL digitado começa com 'https://www.youtube.com/watch?v=' e de que seja de um vídeo")
            input("Digite qualquer coisa para continuar: ")
        break

while True:
    os.system('cls')
    print(f"Youtube Video Downloader \n[1] - Baixar Playlist \n[2] - Baixar Vídeo\n[3] - Baixar áudio \n[4] - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        baixar_playlist()
    elif opcao == "2":
        baixar_video()
    elif opcao == "3":
        baixar_audio()
    elif opcao == "4":
        break