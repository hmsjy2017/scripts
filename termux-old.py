#!/data/data/com.termux/files/usr/bin/python
import os

def shellExec(command):
    return int(os.system(command) / 256) # if shell exit status is 1, os.system will return 256

def exec(command, error):
    if shellExec(command) != 0:
        print(error)
        os._exit(1)
        
def rm_old_lists():
    if os.path.exists('$PREFIX/etc/apt/sources.list.d/science.list')==True:
        os.remove('$PREFIX/etc/apt/sources.list.d/science.list')
    if os.path.exists('$PREFIX/etc/apt/sources.list.d/game.list')==True:
        os.remove('$PREFIX/etc/apt/sources.list.d/game.list')
    
def logo():
    print(" _______                                ____  _     _ ")
    print("|__   __|                              / __ \| |   | |")
    print("   | | ___ _ __ _ __ ___  _   ___  __ | |  | | | __| |")
    print("   | |/ _ \ '__| '_ ` _ \| | | \ \/ / | |  | | |/ _` |")
    print("   | |  __/ |  | | | | | | |_| |>  <  | |__| | | (_| |")
    print("   |_|\___|_|  |_| |_| |_|\__,_/_/\_\  \____/|_|\__,_|")
    print('')
    print("Termux repository for Android 5/6")
    print('')
    print('\033[1mChoose a mirror:\033[0m\n')
    print('1. Tsinghua (Beijing, China)')
    print('2. BFSU (Beijing, China)')
    print('3. ISCAS (Beijing, China)')
    print('4. NJU (Nanjing, China)\n')
#    print('5. OneDrive (Singapore)\n')
    print('\033[1mOther options:\033[0m\n')
    print('5. Exit')
    print('')

def update():
    print('Updating APT lists...')
    exec('apt update || exit 1', "Failed to update APT lists!")
    print('Done!')

if __name__ == "__main__":
    copyright = logo()

    try:
        option = input('\nPlease select the action to be performed: ')
    except EOFError:
        pass

    try:
        if int(option) == 1:
            rm_old_lists()
            exec('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/t/te/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/t/te/termux-old/science-packages-21 science stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/t/te/termux-old/game-packages-21 games stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/t/te/termux-old/unstable-packages-21 unstable main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.tuna.tsinghua.edu.cn/osdn/storage/g/t/te/termux-old/x11-packages-21 x11 main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            update()

        elif int(option) == 2:
            rm_old_lists()
            exec('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/t/te/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/t/te/termux-old/science-packages-21 science stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/t/te/termux-old/game-packages-21 games stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/t/te/termux-old/unstable-packages-21 unstable main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirrors.bfsu.edu.cn/osdn/storage/g/t/te/termux-old/x11-packages-21 x11 main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            update()

        elif int(option) == 3:
            rm_old_lists()
            exec('echo "deb https://mirror.iscas.ac.cn/osdn/storage/g/t/te/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.iscas.ac.cn/osdn/storage/g/t/te/termux-old/science-packages-21 science stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.iscas.ac.cn/osdn/storage/g/t/te/termux-old/game-packages-21 games stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.iscas.ac.cn/osdn/storage/g/t/te/termux-old/unstable-packages-21 unstable main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.iscas.ac.cn/osdn/storage/g/t/te/termux-old/x11-packages-21 x11 main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            update()

        elif int(option) == 4:
            rm_old_lists()
            exec('echo "deb https://mirror.nju.edu.cn/osdn/storage/g/t/te/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.nju.edu.cn/osdn/storage/g/t/te/termux-old/science-packages-21 science stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.nju.edu.cn/osdn/storage/g/t/te/termux-old/game-packages-21 games stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.nju.edu.cn/osdn/storage/g/t/te/termux-old/unstable-packages-21 unstable main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            exec('echo "deb https://mirror.nju.edu.cn/osdn/storage/g/t/te/termux-old/x11-packages-21 x11 main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
            update()

#        elif int(option) == 5:
#            rm_old_lists()
#            exec('echo "deb https://fc.iamsjy.com/termux-old/termux-packages stable main" > $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
#            exec('echo "deb https://fc.iamsjy.com/termux-old/science-packages-21 science stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
#            exec('echo "deb https://fc.iamsjy.com/termux-old/game-packages-21 games stable" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
#            exec('echo "deb https://fc.iamsjy.com/termux-old/unstable-packages-21 unstable main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
#            exec('echo "deb https://fc.iamsjy.com/termux-old/x11-packages-21 x11 main" >> $PREFIX/etc/apt/sources.list || exit 1', "Failed to create package list!")
#            update()

        elif int(option) == 5:
            os._exit(0)
        else:
            print('Illegal input option. Please re-enter.')

    except ValueError:
        print('Illegal input option. Please re-enter.')
