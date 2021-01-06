import subprocess
import ctypes
import os
import time
from configparser import ConfigParser 

cfg = ConfigParser() 
print (cfg.read('config.ini')) 

Interface = cfg.get('INTERFACES','PRINCIPAL')
InstanciaSQL = 'SQLBOSCH'

os.system("mode con cols=63 lines=30")

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    print("Admin!")
else:
    print("\n Você é um simples mortal! \n\n Nao é dígno de usar esse programa!")
    cmd = input('')
    os.system('cls')

    if cmd == '@admin':
        print('\n Tá bom, vai lá né :/ ')
        input('')
        os.system('cls')

    else:
        exit()



def setIP24(IP):
    subprocess.call('netsh interface ipv4 add address "Ethernet" {} 255.255.255.0'.format(IP))
    time.sleep(1)
    os.system('cls')

def setIP(IP, MK, GT):
    subprocess.call('netsh interface ipv4 add address "{}" {} {} gateway = {}'.format(Interface, IP, MK, GT))
    time.sleep(1)
    os.system('cls')

def setDHCP():
    subprocess.call('netsh interface ip set address "{}" dhcp'.format(Interface))
    subprocess.call('netsh interface ip set dns "{}" dhcp'.format(Interface))
    time.sleep(1)
    os.system('cls')
    
def setIPAuto(NW):
    ips = NW.split('.')
    ips[3] = cfg.get('IPauto','HOST')
    gtw = ips
    gtw[3] = cfg.get('IPauto','GATE')
    ipj = '.'.join(ips)
    gtw = '.'.join(gtw)
    subprocess.call('netsh interface ip set address "{}" dhcp'.format(Interface))
    subprocess.call('netsh interface ipv4 add address "{}" {} {} gateway={}'.format(Interface, ipj, cfg.get('IPauto','MASK'), gtw))
    subprocess.call('netsh interface ip set dns "{}" static 8.8.8.8'.format(Interface))
    time.sleep(1)
    os.system('cls')

def VAZIO():
    input('\nTem nada aqui não! Oxi :/')
    os.system('cls')

def predefinido():


    print('''

    -----------------------------------------------------

          Menu Predefinido

          (1) {}
          (2) {}
          (3) {}
          (4) {}
          (5) {}
          (6) {}
          (7) {}
          (8) {}
          (9) VOLTAR

    -----------------------------------------------------
    '''.format(cfg.get('SLOT_1','NAME'), cfg.get('SLOT_2','NAME'), cfg.get('SLOT_3','NAME'), cfg.get('SLOT_4','NAME'),
    cfg.get('SLOT_5','NAME'), cfg.get('SLOT_6','NAME'), cfg.get('SLOT_7','NAME'), cfg.get('SLOT_8','NAME')
    ))
    ec = input('Digite uma opção: ')

    listaEC = ['1', '2', '3', '4', '5', '6','7', '8']

    if ec in listaEC:
        if (cfg.get('SLOT_{}'.format(ec),'NAME')) == 'VAZIO':
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

    else:
        os.system('cls')
        predefinido()

def setDNS(DNS):
    subprocess.call('netsh interface ip set dns "{}" static {}'.format(Interface, DNS))
    time.sleep(1)
    os.system('cls')

def servicos():
    print('''

    -----------------------------------------------------

        GERENCIAMENTO DE SERVIÇOS

        (1) SQL
        (2) 
        (3) VOLTAR
    //em construção!!!
    
    -----------------------------------------------------

    ''')
    es = input('Digite a opção: ')

    if es == '1':
        print('\nSERVIÇO SQL')
        se = input('\nEscolha habilitar ou desabilitar (h/d): ')
        if se == 'h' or se == 'H':
            os.system('net start {}'.format(InstanciaSQL))
            time.sleep(1)
            os.system('cls')
            servicos()
        elif se == 'd' or se == 'D':
            os.system('net stop {}'.format(InstanciaSQL))
            time.sleep(1)
            os.system('cls')
            servicos()
        else:
            servicos()
        os.system('cls')
        servicos()
        
    elif es == '2':
        os.system('cls')

    elif es == '3':
        os.system('cls')

    elif es == 'exit':
        os.system('cls')
        sai()

    else:
        os.system('cls')
        servicos()

def intMan():
    print('''

    -----------------------------------------------------

           GERENCIAMENTO DE INTERFACE

           INTERFACE {}

           (1) DESABILITAR
           (2) HABILITAR
           (3) VOLTAR
    
    -----------------------------------------------------

    '''.format(Interface))
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

def sai():
    input('\nAté a próxima abestado! ;)')#hahahaha
    exit()

def intChange(Intf):
    print('''

    -----------------------------------------------------

            SELECIONE A INTERFACE      
                           
            Interface atual {}
           
            (1) {}
            (2) {}
            (3) INSERIR MANUAL
            (4) VOLTAR
    
    -----------------------------------------------------
            '''.format(Interface, cfg.get('INTERFACES','PRINCIPAL'), cfg.get('INTERFACES','SECUNDARIA')))

    ei = input('Digite uma opção: ')

    if ei == '1':
        os.system('cls')
        return cfg.get('INTERFACES','PRINCIPAL')
        
    elif ei == '2':
        os.system('cls')
        return cfg.get('INTERFACES','SECUNDARIA')
        
    elif ei == '3':
        os.system('cls')
        Intf = input('Digite o nome da interface: ')
        return Intf
    
    elif ei == '4':
        os.system('cls')
        return Intf    

    elif ei == 'exit':
        os.system('cls')
        sai()
    else:
        os.system('cls')
        intChange(Intf)

def sobre():
    input('''

    -----------------------------------------------------

    Desenvolvido por Júlio Cardoso

    Ano 2020
    Sim, foi na quarentena mesmo :)

    Na pasta do programa há o arquivo config.ini com os
    parâmetros padrões do programa
    
    -----------------------------------------------------

    ''')

def nadaAqui():
    os.system('cls')#Sério, não tem nada mesmo

while True:
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
            (9) SAIR

            (10)Sobre
    -----------------------------------------------------
            '''.format(Interface, cfg.get('IPauto','HOST')))
    e = input('\nDigite uma opção: ')
    if e == '1':
        os.system('cls')
        setDHCP()
        
    elif e == '2':
        print()
        IP = input('digite o IP: ')
        os.system('cls')
        setIP24(IP)
        
    elif e == '3':
        print()
        IP = input('Digite o IP: ')
        MK = input('Digite a máscara: ')
        GT = input('Digite o gateway: ')
        os.system('cls')
        setIP(IP, MK, GT)
        
    elif e == '4':
        print()
        DNS = input('Digite o DNS: ')
        os.system('cls')
        setDNS(DNS)
        
    elif e == '5':
        print()
        NW = input('Insira o ip da rede: ')
        os.system('cls')
        setDHCP()
        setIPAuto(NW)
        
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
    
    elif e == '10':
        os.system('cls')
        sobre()

    elif e == 'serv':
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

    