from pytube import YouTube
from pytube import Playlist
import os
resolucoes = []
nomes_proibidos = ["CON", "PRN", "AUX", "CLOCK$", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", 
"LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"]
yt = YouTube("https://www.youtube.com/watch?v=sbMb-g-jr6I")

#video = yt.steams.get_highest_resolution()
#video.download('url')

while True:
    os.system('cls')
    print(f"Youtube Video Downloader \n[1] - Baixar Playlist \n[2] - Baixar Vídeo\n[3] - Baixar áudio \n[4] - Sair")
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        os.system('cls')
        url = input("Digite o URL da playlist do YouTube: ")
        if url[0:32] == "https://www.youtube.com/watch?v=" and "list" in url:
            p = Playlist(url)
            print(p.title)
            opcao = input("Esta é a playlist que você quer baixar? Digite 1 para continuar, 2 para digitar outro URL: ")
            if opcao == "1":
                while True:
                    nome = input("Digite um nome para criar uma pasta com os vídeos da playlist: ")
                    if nome.upper() in nomes_proibidos:
                        input("Não se pode criar uma pasta com esse nome por regras do Windows, digite qualquer coisa para continuar: ")
                    else:
                        caminho1 = (r'C:\Users\Fic\Desktop\Pytube2\midias')
                        caminho2 = os.path.join(caminho1, nome) 
                        os.mkdir(caminho2)
                        break
                for video in p.videos:
                    video.streams.first().download(r"C:\Users\Fic\Desktop\Pytube2\midias/"+nome)
                input("Download concluído, digite qualquer coisa para continuar: ")
                
            else:
                continue
        else:
            input("O URL digitado não é uma playlist do YouTube ou não é um URL válido. Digite qualquer coisa para continuar: ")
    elif opcao == "2":
        os.system('cls')
        url = input("Digite o URL do vídeo do YouTube: ")
        if url[0:32] == "https://www.youtube.com/watch?v=":
            yt = YouTube(url)
            print(yt.title)
            opcao = input("Este é o vídeo que você quer baixar? Digite 1 para continuar, 2 para digitar outro URL: ")
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
                        yt.streams.filter(res=resolucao_escolhida).first().download('./midias')
                        input("Vídeo baixado, digite qualquer coisa para continuar: ")
                        resolucoes.clear()
                        break
                    else:
                        print("O vídeo não está disponível nesta resolução, escolha outra")
            else:
                continue
        else:
            print("URL inválido, certifique-se de que o URL digitado começa com 'https://www.youtube.com/watch?v='")
            input("Digite qualquer coisa para continuar: ")
    elif opcao == "3":
        os.system('cls')
        url = input("Digite o URL do vídeo do YouTube: ")
        if url[0:32] == "https://www.youtube.com/watch?v=":
            yt = YouTube(url)
            print(yt.title)
            opcao = input("Este é o vídeo cujo áudio você quer baixar? Digite 1 para continuar, 2 para digitar outro URL: ")
            if opcao == "1":
                arquivo_baixado =  yt.streams.first().download('./midias')
                base, ext = os.path.splitext(arquivo_baixado)
                new_file = base + '.mp3'
                os.rename(arquivo_baixado, new_file)
                input("Áudio baixado, digite qualquer coisa para continuar: ")
                break
            else:
                continue
    elif opcao == "4":
        break