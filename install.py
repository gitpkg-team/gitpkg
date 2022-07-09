from os import system

system("mkdir ~/.gitpkg")
system("cp -r bin ~/.gitpkg")
system("git clone https://github.com/gitpkg-team/index.git ~/.gitpkg/indexes/main")
system('echo "main" > index')
print("Successfully installed gitpkg!")