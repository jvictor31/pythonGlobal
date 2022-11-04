import os
from pathlib import Path

dePasta="/home/vagrant"
paraPastaTxt="/home/vagrant/arquivosTxt//"
paraPastaLog="/home/vagrant/arquivosLog//"

os.chdir(str(dePasta))
path = Path(dePasta)

for nomeArquivo in os.listdir(path):
    nome, extensao = os.path.splitext(nomeArquivo)
    if extensao == ".txt":
        os.rename(nomeArquivo, paraPastaTxt + nomeArquivo)
    elif extensao == ".log":
        os.rename(nomeArquivo, paraPastaLog + nomeArquivo)
