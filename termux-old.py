#!/data/data/com.termux/files/usr/bin/python
import os

def shellExec(command):
    return int(os.system(command) / 256) # if shell exit status is 1, os.system will return 256

def exec(command, error):
    if shellExec(command) != 0:
        print(error)
        os._exit(1)

def logo():
    print(" _______                                ____  _     _ ”）
    print("|__   __|                              / __ \| |   | |")
    print("   | | ___ _ __ _ __ ___  _   ___  __ | |  | | | __| |")
    print("   | |/ _ \ '__| '_ ` _ \| | | \ \/ / | |  | | |/ _` |")
    print("   | |  __/ |  | | | | | | |_| |>  <  | |__| | | (_| |")
    print("   |_|\___|_|  |_| |_| |_|\__,_/_/\_\  \____/|_|\__,_|")
          
    print("Termux repository for Android 5/6")
    print('')
    print('\033[1mChoose a mirror:\033[0m\n')
    print('1. Tsinghua (Beijing, China)')
    print('2. BFSU (Beijing, China)')
    print('3. ISCAS (Beijing, China)')
    print('4. NJU (Nanjing, China)')
    print('5. OneDrive (Singapore)')
    print('\033[1mOther options:\033[0m\n')
    print('0. Exit')
    print('')

def update():
    print('Updating APT lists...')
    exec('apt update || exit 1', "Failed to update APT lists!")
    print('Done!')


    try:
        option = input('\nPlease select the action to be performed: ')
    except EOFError:
        pass

    try:
        if int(option) == 1:
            add_gpg_key()
            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            update()

        elif int(option) == 2:
            add_gpg_key()
            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            update()

        elif int(option) == 3:
            add_gpg_key()
            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            update()

        elif int(option) == 4:
            add_gpg_key()
            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            update()

        elif int(option) == 5:
            add_gpg_key()
            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 stable main" >> $PREFIX/etc/apt/sources.list')
            update()

        elif int(option) == 6:
            os._exit(0)
        else:
            print('Illegal input option. Please re-enter.')

    except ValueError:
        print('Illegal input option. Please re-enter.')
