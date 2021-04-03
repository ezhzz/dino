import webbrowser
import time
import os
import os.path
import glob

versions = [
"1.16.4","1.16.3","1.16.2","1.16.1","1.15.2","1.15.1","1.15","1.14.4","1.14.3","1.14.2","1.14.1","1.14",
"1.13.2","1.13.1","1.13","1.12.2","1.12.1","1.12","1.11.2","1.11.1","1.11","1.10.2", "1.10", "1.9.4", "1.9.2", "1.9", "1.8.8", "1.8.7", "1.8.6", "1.8.5", "1.8.4",
"1.8.3", "1.8", "1.7.10", "1.7.9", "1.7.8", "1.7.5", "1.7.2", "1.6.4", "1.6.2", "1.5.2", "1.5.1", "1.4.7", "1.4.6"]
print(' _______   __                     \n|       \ |  \                    \n| $$$$$$$\ \$$ _______    ______  \n| $$  | $$|  \|       \  /      \ \n| $$  | $$| $$| $$$$$$$\|  $$$$$$\ \n| $$  | $$| $$| $$  | $$| $$  | $$ \n| $$__/ $$| $$| $$  | $$| $$__/ $$\n| $$    $$| $$| $$  | $$ \$$    $$\n \$$$$$$$  \$$ \$$   \$$  \$$$$$$ ')

print('\nПривет! :)')

if os.path.isfile("ok :).txt") == True:
    print('Чтобы получить токен перейдите по ссылке ngrok.com, создайте аккаунт и в разделе Authentication - Your Authtoken вы сможете найти свой токен. Он нужен для игры с друзьями без открытия портов.')
    ngtoken = input('Введите токен от ngrok: ')
    os.system('./ngrok authtoken ' + ngtoken)

    print("Сервер готов!\nДавай же скорее его запустим!")
    input("Нажми Enter...")
    ozu = input('Сколько оперативки ты готов выделить серверу?: ')
    name = input('Имя файла ядра: ')
    os.system('./ngrok tcp -region eu 25565 &2>/dev/null')
    os.system('java -Xmx'+ ozu +'M -Xms1024M -jar ' + name + ' nogui &2>/dev/null')
    webbrowser.open('http://127.0.0.1:4040')
else:
    print('Я могу создать сервер Minecraft бесплатно на твоем компьютере.\nИ он будет доступен всем, бесплатно, без открытых портов.')
    print('\n-----------------------------------------\n1)1, 2, 3 и готово\n -Использование шаблонов в Dino\n2)Я могу настроить сам\n -Настройка важных параметров в Dino\n3)Я айтишник, дайте мне все настроить самому\n -Дефолтные параметры, настройка через конфиги\n-----------------------------------------\n')
    choose = int(input('Что выбираем?: '))
    if choose == 1:

        print('\nВыберите шаблон:\nОфициальные(с лицензией Minecraft):\n-----------------------------------------\n1)Обычный(самый обычный мир Minecraft)\n2)Хардкор(обычный мир с самым высоким уровнем сложности и одной жизнью)\n-----------------------------------------\n')
        print('Пиратские(без лицензии Minecraft):\n-----------------------------------------\n3)Обычный(самый обычный мир Minecraft)\n4)Хардкор(обычный мир с самым высоким уровнем сложности и одной жизнью)\n-----------------------------------------\n')
        template = int(input('>> '))

        if template == 1:
            version = input('Введите версию: ')
            url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
            for i in range(len(versions)):
                if versions[i] == version:
                    print("Генерация конфига...")

                    config = open('server.properties', 'w')
                    config.write("#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4\nallow-nether=true\nlevel-name=world\nallow-flight=false\nprevent-proxy-connections=false\nserver-port=25565\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true\nwhite-list=false\nspawn-animals=true\nhardcore=false\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=true\nresource-pack=\npvp=true\ndifficulty=1\nenable-command-block=false\ngamemode=0\nplayer-idle-timeout=0\nmax-players=100\nspawn-monsters=true\ngenerate-structures=true\nview-distance=10\nmotd=A Minecraft Server")
                    config.close()

                    config = open('eula.txt', 'w')
                    config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                    config.close()

                    print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                    easter_egg = open('ok :).txt', 'w')
                    easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                    easter_egg.close()

                    time.sleep(3)
                    webbrowser.open(url)
        if template == 2:
            version = input('Введите версию: ')
            url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
            for i in range(len(versions)):
                if versions[i] == version:
                    print("Генерация конфига...")

                    config = open('server.properties', 'w')
                    config.write("#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4\nallow-nether=true\nlevel-name=world\nallow-flight=false\nprevent-proxy-connections=false\nserver-port=25565\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true\nwhite-list=false\nspawn-animals=true\nhardcore=true\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=true\nresource-pack=\npvp=true\ndifficulty=3\nenable-command-block=false\ngamemode=0\nplayer-idle-timeout=0\nmax-players=100\nspawn-monsters=true\ngenerate-structures=true\nview-distance=10\nmotd=A Minecraft Server")
                    config.close()

                    config = open('eula.txt', 'w')
                    config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                    config.close()

                    print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                    easter_egg = open('ok :).txt', 'w')
                    easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                    easter_egg.close()

                    time.sleep(3)
                    webbrowser.open(url)
        if template == 3:
            version = input('Введите версию: ')
            url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
            for i in range(len(versions)):
                if versions[i] == version:
                    print("Генерация конфига...")

                    config = open('server.properties', 'w')
                    config.write("#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4\nallow-nether=true\nlevel-name=world\nallow-flight=false\nprevent-proxy-connections=false\nserver-port=25565\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true\nwhite-list=false\nspawn-animals=true\nhardcore=false\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=false\nresource-pack=\npvp=true\ndifficulty=1\nenable-command-block=false\ngamemode=0\nplayer-idle-timeout=0\nmax-players=100\nspawn-monsters=true\ngenerate-structures=true\nview-distance=10\nmotd=A Minecraft Server")
                    config.close()

                    config = open('eula.txt', 'w')
                    config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                    config.close()

                    print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                    easter_egg = open('ok :).txt', 'w')
                    easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                    easter_egg.close()

                    time.sleep(3)
                    webbrowser.open(url)
        if template == 4:
            version = input('Введите версию: ')
            url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
            for i in range(len(versions)):
                if versions[i] == version:
                    print("Генерация конфига...")

                    config = open('server.properties', 'w')
                    config.write("#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4\nallow-nether=true\nlevel-name=world\nallow-flight=false\nprevent-proxy-connections=false\nserver-port=25565\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true\nwhite-list=false\nspawn-animals=true\nhardcore=true\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=false\nresource-pack=\npvp=true\ndifficulty=3\nenable-command-block=false\ngamemode=0\nplayer-idle-timeout=0\nmax-players=100\nspawn-monsters=true\ngenerate-structures=true\nview-distance=10\nmotd=A Minecraft Server")
                    config.close()

                    config = open('eula.txt', 'w')
                    config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                    config.close()

                    print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                    easter_egg = open('ok :).txt', 'w')
                    easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                    easter_egg.close()

                    time.sleep(3)
                    webbrowser.open(url)
        else:
            print('Я не понял :|')
            exit(0)

    elif choose == 2:
        version = input('Введите версию: ')
        url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
        for i in range(len(versions)):
            if versions[i] == version:
                print('-Окей, давай настроим твой сервер.\nОтвечай д(да) или н(нет.)')

                config_text = "#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4"

                nether = input("Ад включен?(д, н): ")
                if nether == "д":
                    print("Ад включен!")
                    config_text = config_text + "\nallow-nether=true\nlevel-name=world"
                    nether = True
                elif nether == "н":
                    print("Ад выключен!")
                    nether = False
                    config_text = config_text + "\nallow-nether=false\nlevel-name=world"
                else:
                    print("Я не понял. Попробуйте еще раз.")

                fly = input("Полет включен?(д, н): ")
                if fly == "д":
                    print("Полет включен!")
                    config_text = config_text + "\nallow-flight=true"
                    fly = True
                elif fly == "н":
                    print("Полет выключен!")
                    config_text = config_text + "\nallow-flight=false"
                    fly = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                proxy = input("Блокировать прокси-соединения(это может использоваться для обхода банов по ip)? (д, н): ")
                if proxy == "н":
                    print("Прокси-соединения доступны!")
                    config_text = config_text + "\nprevent-proxy-connections=false"
                    proxy = True
                elif proxy == "д":
                    print("Прокси-соединения не доступны!")
                    config_text = config_text + "\nprevent-proxy-connections=true"
                    proxy = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                config_text = config_text + "\nserver-port=25565"

                npc = input("Спавнить npc? (д, н): ")
                if npc == "д":
                    print("Спавн npc включен!")
                    config_text = config_text + "\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true"
                    npc = True
                elif npc == "н":
                    print("Спавн npc выключен!")
                    config_text = config_text + "\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=false"
                    npc = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                wl = input("Использовать white-list? (д, н): ")
                if wl == "д":
                    print("white-list включен!")
                    config_text = config_text + "\nwhite-list=true"
                    wl = True
                elif wl == "н":
                    print("white-list выключен!")
                    config_text = config_text + "\nwhite-list=false"
                    wl = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                animals = input("Спавнить животных? (д, н): ")
                if animals == "д":
                    print("Спавн животных включен!")
                    config_text = config_text + "\nspawn-animals=true"
                    animals = True
                elif animals == "н":
                    print("Спавн животных выключен!")
                    config_text = config_text + "\nspawn-animals=false"
                    animals = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                hardcore = input("Хардкор включен? (д, н): ")
                if hardcore == "д":
                    print("Хардкор включен!")
                    config_text = config_text + "\nhardcore=true"
                    hardcore = True
                elif hardcore == "н":
                    print("Хардкор выключен!")
                    config_text = config_text + "\nhardcore=false"
                    hardcore = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                pirate = input("Можно ли будет зайти без лицензии Minecraft? (д, н): ")
                if pirate == "д":
                    print("Пиратский вход включен!")
                    config_text = config_text + "\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=false"
                    pirate = True
                elif pirate == "н":
                    print("Пиратский вход выключен!")
                    config_text = config_text + "\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=true"
                    pirate = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                pvp = input("Включено ли pvp? (д, н): ")
                if pvp == "д":
                    print("Pvp включено!")
                    config_text = config_text + "\nresource-pack=\npvp=true"
                    pvp = True
                elif pvp == "н":
                    print("Pvp выключено!")
                    config_text = config_text + "\nresource-pack=\npvp=false"
                    pvp = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                difficulty = int(input("Сложность (мирная (0) легкая (1) нормальная (2) сложная (3)): "))
                print("Сложность на сервере: " + str(difficulty))
                config_text = config_text + "\ndifficulty=" + str(difficulty)

                cb = input("Включены ли командные блоки? (д, н): ")
                if cb == "д":
                    print("Командные блоки включены!")
                    config_text = config_text + "\nenable-command-block=true"
                    cb = True
                elif cb == "н":
                    print("Командные блоки выключены!")
                    config_text = config_text + "\nenable-command-block=false"
                    cb = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                gamemode = int(input("Режим игры (выживание (0) креатив (1) приключение (2) спектатор (3)): "))
                print("Режим на сервере: " + str(gamemode))
                config_text = config_text + "\ngamemode=" + str(gamemode)

                players = int(input("Cлоты: "))
                print("Слоты: " + str(players))
                config_text = config_text + "\nplayer-idle-timeout=0\nmax-players=" + str(players)

                monsters = input("Включен ли спавн монстров? (д, н): ")
                if monsters == "д":
                    print("Cпавн монстров включен!")
                    config_text = config_text + "\nspawn-monsters=true"
                    monsters = True
                elif monsters == "н":
                    print("Cпавн монстров выключен!")
                    config_text = config_text + "\nspawn-monsters=false"
                    monsters = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                structures = input("Включена ли генерация структур? (д, н): ")
                if structures == "д":
                    print("Генерация структур включена!")
                    config_text = config_text + "\ngenerate-structures=true"
                    structures = True
                elif structures == "н":
                    print("Генерация структур выключена!")
                    config_text = config_text + "\ngenerate-structures=false"
                    structures = False
                else:
                    print("Я не понял. Попробуйте еще раз.")

                motd = input("Введите MOTD(описание) сервера(для кириллицы используйте сайт https://minecraft.tools/en/motd.php): ")
                print('Описание сервера: ' + motd)
                config_text = config_text + "\nview-distance=10\nmotd=" + motd

                print("Генерация конфига...")
                config = open('server.properties', 'w')
                config.write(config_text)
                config.close()

                config = open('eula.txt', 'w')
                config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                config.close()

                print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                easter_egg = open('ok :).txt', 'w')
                easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                easter_egg.close()

                time.sleep(3)
                webbrowser.open(url)
    elif choose == 3:
        version = input('Введите версию: ')
        url = 'https://cdn.getbukkit.org/spigot/spigot-'+ str(version) + '.jar'
        for i in range(len(versions)):
            if versions[i] == version:
                print("Генерация конфига...")

                config = open('server.properties', 'w')
                config.write("#Minecraft server properties\n#auto-generated in Dino\ngenerator-settings=\nuse-native-transport=true\nop-permission-level=4\nallow-nether=true\nlevel-name=world\nallow-flight=false\nprevent-proxy-connections=false\nserver-port=25565\nmax-world-size=29999984\nlevel-type=DEFAULT\nlevel-seed=\nforce-gamemode=false\nserver-ip=\nnetwork-compression-threshold=256\nmax-build-height=256\nspawn-npcs=true\nwhite-list=false\nspawn-animals=true\nhardcore=false\nsnooper-enabled=true\nresource-pack-sha1=\nonline-mode=true\nresource-pack=\npvp=true\ndifficulty=1\nenable-command-block=false\ngamemode=0\nplayer-idle-timeout=0\nmax-players=20\nspawn-monsters=true\ngenerate-structures=true\nview-distance=10\nmotd=A Minecraft Server")
                config.close()

                config = open('eula.txt', 'w')
                config.write('#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).\n#auto-generated in Dino\neula=true')
                config.close()

                print('Ура! Мы настроили твой сервер!\nТеперь давай скачаем ядро, это займет несколько минут\nСохрани его в папке с сервером, когда все скачается, перезапусти Dino.')

                easter_egg = open('ok :).txt', 'w')
                easter_egg.write('Ок, наверное ты решил порыться в файлах программы...\nЭтот файл служит для того, чтобы программа понимала, в каком режиме запускаться, в режиме запуска или создания.\nВообщем, спасибо что пользуешься нашей программой.\nВаши Gillio inc.')
                easter_egg.close()

                time.sleep(3)
                webbrowser.open(url)

    else:
        print('Я не понял :|')
        exit(0)
