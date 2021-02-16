import subprocess
import ctypes
import os
import time
from configparser import ConfigParser
import sys

def notas():
    print('''

    
    
    ''')

cfg = ConfigParser()
#print (cfg.read('config.ini'))

versao = '1.02'
data = 'Fev 21'

os.system("mode con cols=63 lines=30")

def isAdmin(): #Método para teste administrador
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin(): #Testa se está em modo administrador
    print("")
else:
    print("\n Você é um simples mortal! \n\n Nao é dígno de usar esse programa!")
    cmd = input('')
    os.system('cls')

    if cmd == '@admin': #Digitando @admin permite acesso ao programa, mesmo sem privilégios de administrador
        print('\n Tá bom, vai lá né :/ ')
        input('')
        os.system('cls')

    else: #Senão, sai
        exit()

def createCFG(): #Criar arquivo de configuração caso não exista
    try:
        if os.path.isfile('config.ini'):
            os.system('cls')
        else:
            print('Arquivo de configuração (config.ini) não encontrado! \nCriando novo arquivo...')
            cfg['DEFAULT'] = {'DNS': '8.8.8.8'}
            cfg['IPauto'] = {'MASK': '255.255.255.0',
                                'HOST': '253',
                                'GATE': '254'}
            cfg['INTERFACES'] = {'PRINCIPAL': 'Ethernet',
                                'SECUNDARIA': 'Wi-Fi'}
            cfg['SLOT_1'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_2'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_3'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_4'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_5'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_6'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_7'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SLOT_8'] = {'NAME': '',
                                'IP': '',
                                'MASK': '',
                                'GATE': ''}
            cfg['SRV_1'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_2'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_3'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_4'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_5'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_6'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_7'] = {'NOME': '',
                                'SRV': ''}
            cfg['SRV_8'] = {'NOME': '',
                                'SRV': ''}
            with open('config.ini', 'w') as configfile:
                cfg.write(configfile)
            os.system('cls')
    except Exception as e: 
        input(e)
        os.system('cls')

createCFG()

def setSlot(slot):    #Editar arquivo de configuração
    try:
        nome = input('Digite um nome para o slot: ')
        v1 = input('Digite um valor para IP: ')
        v2 = input('Digite um valor para MASCARA: ')    
        v3 = input('Digite um valor para GATEWAY: ')
        cfg.set("SLOT_{}".format(slot), "NAME", nome)
        cfg.set("SLOT_{}".format(slot), "IP", v1)
        cfg.set("SLOT_{}".format(slot), "MASK", v2)
        cfg.set("SLOT_{}".format(slot), "GATE", v3)
        os.system('cls')
    except KeyboardInterrupt:
        os.system('cls')
        predefinido()

def setIP24(IP): #Método para configurar IP rapidamente, somente IP e Máscara /24
    subprocess.call('netsh interface ipv4 add address "{}" {} 255.255.255.0'.format(Interface, IP))
    time.sleep(1)
    os.system('cls')

def setIP(IP, MK, GT): #Metodo para configuração manual de IP (Parâmetros herdados)
    subprocess.call('netsh interface ipv4 add address "{}" {} {} gateway = {}'.format(Interface, IP, MK, GT))
    time.sleep(2)
    os.system('cls')

def setDHCP(): #Metodo para setar a interface como DHCP
    subprocess.call('netsh interface ip set address "{}" dhcp'.format(Interface))
    subprocess.call('netsh interface ip set dns "{}" dhcp'.format(Interface))
    time.sleep(1)
    os.system('cls')
    
def setIPAuto(NW): #Método para configuração automática de IP
    ips = NW.split('.')
    ips[3] = cfg.get('IPauto','HOST')
    gtw = NW.split('.')
    gtw[3] = cfg.get('IPauto','GATE')
    ipj = '.'.join(ips)
    gtw = '.'.join(gtw)
    subprocess.call('netsh interface ip set address "{}" dhcp'.format(Interface))
    subprocess.call('netsh interface ipv4 add address "{}" {} {} gateway={}'.format(Interface, ipj, cfg.get('IPauto','MASK'), gtw))
    subprocess.call('netsh interface ip set dns "{}" static 8.8.8.8'.format(Interface))
    time.sleep(1)
    os.system('cls')

def VAZIO():
    try:
        input('\nTem nada aqui não! Oxi :/')
        os.system('cls')
    except KeyboardInterrupt:
        os.system('cls')

def predefinido(): #Menu predefinido integrado ao arquivo config.ini
    os.system("color 0f")

    print('''

    -----------------------------------------------------

            MENU PREDEFINIDO

            (1) {}
            (2) {}
            (3) {}
            (4) {}
            (5) {}
            (6) {}
            (7) {}
            (8) {}
            (9) VOLTAR    "set" para alterar um slot

    -----------------------------------------------------
    '''.format(cfg.get('SLOT_1','NAME'), cfg.get('SLOT_2','NAME'), cfg.get('SLOT_3','NAME'), cfg.get('SLOT_4','NAME'),
    cfg.get('SLOT_5','NAME'), cfg.get('SLOT_6','NAME'), cfg.get('SLOT_7','NAME'), cfg.get('SLOT_8','NAME')
    ))
    try:
        ec = input('Digite uma opção: ')

        listaEC = ['1', '2', '3', '4', '5', '6','7', '8']

        if ec in listaEC:
            teste = cfg.get('SLOT_{}'.format(ec),'IP')
            if teste == "":
                VAZIO()
                predefinido()
            else:
                setIP((cfg.get('SLOT_{}'.format(ec),'IP')),(cfg.get('SLOT_{}'.format(ec),'MASK')),(cfg.get('SLOT_{}'.format(ec),'GATE')))
                setDNS(cfg.get('DEFAULT','DNS'))
                os.system('cls')


        elif ec == '9':
            os.system('cls')

        elif ec == 'exit':
            os.system('cls') 
            sai()

        elif ec == 'set' or ec == 'SET' or ec == 'Set':
            print('\n    --------------Configuração de slots------------------\n')
            slot = input('Digite o slot a ser alterado:')
            if slot in listaEC:
                setSlot(slot)
                predefinido()
            else:
                input('Esse slot não existe!')
                os.system('cls')
                predefinido()

        else:
            os.system('cls')
            predefinido()
    except KeyboardInterrupt:
        os.system('cls')

def setDNS(DNS): #Método para configuração de DNS
    subprocess.call('netsh interface ip set dns "{}" static {}'.format(Interface, DNS))
    time.sleep(1)
    os.system('cls')

def srvMAN(NOME, SRV): #Habilitar / Desabilitar o serviço selecionado
    print('\n{}'.format(NOME))
    try:
        se = input('\nEscolha habilitar ou desabilitar (h/d): ')
        if se == 'h' or se == 'H':
            os.system('net start {}'.format(SRV))
            time.sleep(1)
            os.system('cls')
            servicos()
        elif se == 'd' or se == 'D':
            os.system('net stop {}'.format(SRV))
            time.sleep(1)
            os.system('cls')
            servicos()
        else:
            servicos()
            os.system('cls')
            servicos()
    except KeyboardInterrupt:
            os.system('cls')
            servicos()

def servicos(): #Menu de serviços
    print('''

    -----------------------------------------------------

            GERENCIAMENTO DE SERVIÇOS

            (1) {}
            (2) {}
            (3) {}
            (4) {}
            (5) {}
            (6) {}
            (7) {}
            (8) {}
            (9) VOLTAR

            "set" para configurar os serviços
    -----------------------------------------------------

    '''.format(cfg.get('SRV_1','NOME'), cfg.get('SRV_2','NOME'), cfg.get('SRV_3','NOME'), cfg.get('SRV_4','NOME'), cfg.get('SRV_5','NOME'), cfg.get('SRV_6','NOME'), cfg.get('SRV_7','NOME'), cfg.get('SRV_8','NOME') ))
    try:    
        es = input('Digite a opção: ')

        listaES = ['1', '2', '3', '4', '5', '6', '7', '8']

        if es in listaES:
            testeSRV = cfg.get('SRV_{}'.format(es),'SRV')

            if testeSRV == "":
                VAZIO()
                servicos()
            else:
                srvMAN(cfg.get('SRV_{}'.format(es),'NOME'), cfg.get('SRV_{}'.format(es),'SRV'))
                os.system('cls')
                servicos()

        elif es == 'set' or es =='SET':
            try:
                print('\n    --------------Configuração de slots------------------\n')
                Sslot = input('Digite o slot a ser alterado:')
                if Sslot in listaES:
                    Snome = input('Digite um nome para o slot: ')
                    SRVNome = input('Digite o nome do serviço: ')
                    cfg.set("SRV_{}".format(Sslot), "NOME", Snome)
                    cfg.set("SRV_{}".format(Sslot), "SRV", SRVNome)
    
                    os.system('cls')
                    servicos()
                else:
                    input('Esse slot não existe!')
                    os.system('cls')
                    servicos()
            except KeyboardInterrupt:
                os.system('cls')
                servicos()

        elif es == '9':
            os.system('cls')

        elif es == 'exit':
            os.system('cls')
            sai()

        else:
            os.system('cls')
            servicos()
    except KeyboardInterrupt:
        os.system('cls')

def intMan(): #Menu de gerenciamento de interface
    print('''

    -----------------------------------------------------

           GERENCIAMENTO DE INTERFACE

           INTERFACE {}

           (1) DESABILITAR
           (2) HABILITAR
           (3) VOLTAR
    
    -----------------------------------------------------

    '''.format(Interface))
    try:
        eit = input('Digite a opção: ')

        if eit == '1':
            subprocess.call('netsh interface set interface "{}" admin=disable'.format(Interface))
            os.system('cls')
            
        elif eit == '2':
            subprocess.call('netsh interface set interface "{}" admin=enable'.format(Interface))
            os.system('cls')
        elif eit == '3':
            os.system('cls')

        elif eit == 'exit':
            os.system('cls')
            sai()
        else:
            os.system('cls')
            intMan()
    except KeyboardInterrupt:
        os.system('cls')

def sai():
    input('\nAté a próxima! ;)')
    exit()

def CMD():
    os.system("color 0f")
    
    try:
        cmd = input('CMD>')
        if cmd == 'exit':
            os.system('cls')
        else:
            os.system(cmd)
            CMD()
    except KeyboardInterrupt:
            CMD()

def intChange(Intf): #Menu para seleção de interface
    print('''

    -----------------------------------------------------

            SELECIONE A INTERFACE      
                           
            Interface atual {}
           
            (1) {}
            (2) {}
            (3) VOLTAR 
            
            "set" para configurar as unidades
    
    -----------------------------------------------------
            '''.format(Interface, cfg.get('INTERFACES','PRINCIPAL'), cfg.get('INTERFACES','SECUNDARIA')))
    try:
        ei = input('Digite uma opção: ')
    except KeyboardInterrupt:
        os.system('cls')
        return Intf

    if ei == '1':
        os.system('cls')
        return cfg.get('INTERFACES','PRINCIPAL')
        
    elif ei == '2':
        os.system('cls')
        return cfg.get('INTERFACES','SECUNDARIA')
        
    elif ei == 'set' or ei == 'SET':
        print('\n--------------Configuração de slots-----------------\n')
        try:
            slot = input('Escolha a insterface 1 ou 2: ')
            if slot == '1':    
                valor1 = input('Digite o nome da interface:')
                cfg.set("INTERFACES", "PRINCIPAL", valor1)
                os.system('cls')
                intChange(Intf)
            if slot == '2':
                valor2 = input('Digite o nome da interface:')
                cfg.set("INTERFACES", "SECUNDARIA", valor2)
                os.system('cls')
                intChange(Intf)
            else:
                print('Opção incorreta!')
                time.sleep(1)
                os.system('cls')
                intChange(Intf)

        except KeyboardInterrupt:
            os.system('cls')
            intChange(Intf)
        
        
            
        os.system('cls')
        intChange(Intf)
        
    
    elif ei == '3':
        os.system('cls')
        return Intf    

    elif ei == 'exit':
        os.system('cls')
        sai()
    else:
        os.system('cls')
        intChange(Intf)

def historico():
    os.system("color 0c")
    input('''

    -----------------------------------------------------

    Versão 1.02 - Jan 21
    Configuração de slots predefinidos pelo programa 
    (utilizando 'set')

    Criação de arquivo config.ini (caso não exista)
    Aprimoramentos de estabilidade

    Versão 1.01 - Jan 21
    Adicionado o modo terminal livre "cmd"

    Versão 1.00 - Jan 21
    Primeira versão distribuída

    Desenvolvido por Júlio Cardoso
    
    -----------------------------------------------------
    

    ''')
    os.system('cls')

def sobre(): #Sobre o programa
    os.system("color 0c")
    input('''

    -----------------------------------------------------

    Versão {} - {}

    Ano 2020 
    Sim, foi na quarentena mesmo :)

    Leia o arquivo README para mais informações e
    dicas de utilização

    Desenvolvido por Júlio Cardoso
    
    -----------------------------------------------------
    

    '''.format(versao, data))
    os.system('cls')

def nadaAqui():
    os.system('cls')#Sério, não tem nada mesmo

cfg.read_file(open(os.path.join(os.path.dirname(__file__),"config.ini")))
Interface = cfg.get('INTERFACES','PRINCIPAL')

while True: #Menu principal
    os.system("color 0f")
    print('''

    -----------------------------------------------------
    
            SELECIONE UMA DAS OPCOES ABAIXO      
                           
            Interface {}
           
            (1) DHCP
            (2) INSERIR IP /24
            (3) INSERIR IP (Manual)
            (4) ADD DNS
            (5) AUTO IP HOST .{}
            (6) MENU PREDEFINIDO
            (7) ALTERAR INTERFACE
            (8) HABILITAR / DESABILITAR INTERFACE
            (SRV) MENU DE SERVIÇOS
            (CMD) CONSOLE
            (9) SAIR

            (Sobre)                     Versão {}
                                            
    -----------------------------------------------------
            '''.format(Interface, cfg.get('IPauto','HOST'),versao))
    try:
        e = input('\nDigite uma opção: ')
        
        if e == '1':
            os.system('cls')
            setDHCP()
            
        elif e == '2':
            try:
                print()
                IP = input('digite o IP: ')
                os.system('cls')
                setIP24(IP)
            except KeyboardInterrupt:
                os.system('cls')
            
        elif e == '3':
            try:
                print()
                IP = input('Digite o IP: ')
                MK = input('Digite a máscara: ')
                GT = input('Digite o gateway: ')
                os.system('cls')
                setIP(IP, MK, GT)
            except KeyboardInterrupt:
                os.system('cls')
            
        elif e == '4':
            try:
                print()
                DNS = input('Digite o DNS: ')
                os.system('cls')
                setDNS(DNS)
            except KeyboardInterrupt:
                os.system('cls')
            
        elif e == '5':
            try:
                print()
                NW = input('Insira o ip da rede: ')
                os.system('cls')
                setDHCP()
                setIPAuto(NW)
            except KeyboardInterrupt:
                os.system('cls')
            
        elif e == '6':
            os.system('cls')
            predefinido()
            
        elif e == '7':
            os.system('cls')
            Interface = intChange(Interface)
            
        elif e == '8':
            os.system('cls')
            intMan()
            
        elif e == '9':
            exit()
        
        elif e == 'Sobre' or e == 'sobre' or e == '10':
            os.system('cls')
            sobre()

        elif e == 'cmd' or e == 'CMD': #Opção oculta - CMD
            os.system('cls')
            CMD()    

        elif e == 'historico' or e == 'Historico': #Opção oculta - CMD
            os.system('cls')
            historico() 

        elif e == 'srv' or e == 'SRV': #Opção oculta - Serviços
            os.system('cls')
            servicos()

        elif e == 'exit':
            os.system('cls')
            sai()

        else:
            print('Opção escolhida non exizte!')
            time.sleep(1)
            os.system('cls')        
            #nadaAqui()
    except KeyboardInterrupt:
        os.system('cls')
    
