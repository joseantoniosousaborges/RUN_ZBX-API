from Biblioteca import *
import os

op= 0

while op != 4:
    os.system('clear')
    banner()
    menup()

    op = int(input("\n\tDigite uma Opção:"))

    if op == 1:
        op1 =0
        while op1 != 6:
            os.system('clear')
            banner()
            submenu1()
            op1 = int(input("\n\tDigite uma Opção:"))

            if op1 == 1:

                file = input("\n\tDigite o caminho do arquivo: ")
                I = Import(zapi, file)
                num = I.contar_linhas_arquivo(file)
                I.progresso(num)
                I.ImportHost()
                sys.exit(1)

            # - Importando SLA
            if op1 == 2:
                file = input("\n\tDigite o caminho do arquivo: ")
                I = Import(zapi, file)
                I.ImportSLA()
                sys.exit(1)

            # - Importando Descrição
            if op1 == 3:
                file = input("\n\tDigite o caminho do arquivo: ")
                I = Import(zapi, file)
                I.ImportDescriptionHost()
                sys.exit(1)

            # - Importando Visible Hostname
            if op1 == 4:
                file = input("\n\tDigite o caminho do arquivo: ")
                I = Import(zapi, file)
                I.ImportVisibleHostName()
                sys.exit(1)

            # -  Importando nova interface
            if op1 == 5:
                file = input("\n\tDigite o caminho do arquivo: ")
                I = Import(zapi, file)
                num = I.contar_linhas_arquivo(file)
                I.progresso(num)
                I.ImportNewInterface()
                sys.exit(1)

            if op1 == 6:
                sys.exit(1)

    if op == 2:
        op2 = 0
        while op2 != 3:
            os.system('clear')
            banner()
            submenu2()
            op2 = int(input("\n\tDigite uma Opção:"))

            if op2 == 1:
                ops1 = 0
                while ops1 != 4:
                    os.system('clear')
                    banner()
                    submenuitem()
                    ops1 = int(input('\n\tDigite uma Opção:'))

                    if ops1 == 1:
                        hostname = input("\n\tDigite o hostname do host:")
                        I = Item(zapi,hostname)
                        I.DisableItems()
                        sys.exit(1)


                    if ops1 == 2:
                         sys.exit(1)
            if op2 == 2:
                sys.exit(1)


    if op == 3:
        op3 = 0
        while op3 != 2:
            os.system('clear')
            banner()
            submenu3()
            op3 = int(input('\n\tDigite uma Opção:'))

            if op3 == 1:
                ops3 = 0
                while ops3 != 3:
                    os.system('clear')
                    banner()
                    submenuiteml()
                    ops3 = int(input('\n\tDigite uma Opção:'))
                    if ops3 == 1:
                        hostname = input("\n\tDigite o hostname do host:")
                        I = Item(zapi, hostname)
                        I.LNSupported()
                        sys.exit(1)

                    if ops3 == 2:
                        hostname = input("\n\tDigite o hostname do host:")
                        I = Item(zapi, hostname)
                        I.LQNSupported()
                        sys.exit(1)

                    if ops3 == 3:
                        sys.exit(1)
            if op3 == 2:
                grp = input("\n\tDigite o hostgroup do host:")
                g = Group(zapi,grp)
                hostname = g.get_hostgroup(g.getGroupID())

                its = ITservice(zapi,hostname,grp)
                it=its.getChild_itservice_pid()
                print(it)



                sys.exit(1)
            if op3 == 3:
                sys.exit(1)


    if op == 4:
        print("Bye............ :)")
        sys.exit(1)
