# PythonIP

Este programa foi desenvolvido com o intuito de facilitar o dia-a-dia de seus utilizadores quanto a configuração da interface de rede da máquina.

O programa possui um arquivo de configuração customizável em su apasta (config.ini) para se adequar as necessidades do utilizador

Há algumas qu podem ser selecionadas no menu como:
1 - DHCP - Configura a interface selecionada para IP dinâmico
2 - ADD IP /24 - Para adicionar um ip a interface de rede selecionada com máscara 255.255.255.0
3 - Inserir IP manual - Auto explicativo hahaha
4 - ADD DNS - Após configuração de um ou mais IPs, adicionar um DNS manualmente
5 - ADD IP AUTO - Adiciona um IP segundo rede digitada e parâmetros setados em arquivo de configuração (máscara gateway, host e gateway)
6 - Menu predefinido - Sub menu que possibilita a rápida configuração da interface de acordo com os parâmetros configurados previamente nos "slots" do arquivo de configuração
7 - Alterar interface - Escolher qual interface será alvo da configuração solicitada pelos métodos deste programa
8 - Habilitar / desabilitar interface

#### HISTÓRICO ####

Para visualizar o histórico de modificações, utilize o comando "historico" dentro do programa

Versão 1.02 - Fev 21
    Configuração de slots predefinidos pelo programa
    Criação de arquivo config.ini (caso não exista)
    Aprimoramentos de estabilidade

Versão 1.01 - Jan 21
    A partir da versão 1.01 é possível inserir o comando "CMD" e utilizar o terminal de forma livre. Para sair deste modo, utilize o comando "exit"

