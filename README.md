# BlockFrontManager
my version-manager of blockfront

## how to use
set enviroment variables in .env like this
```
BLOCKFRONT_PATH = "C/Users/username/AppData/Roaming/.minecraft/mods"
NEOFORGE_PATH = "C/Users/username/Documents/minecraft/blockfront"
```

then install library from requirements.txt, and use command like this
```
$ python3 ./main.py status
latest BlockFront URL: https://cdn.modrinth.com/data/hTexWmdS/versions/4fh84LES/BlockFront-1.21.1-0.6.0.2b-RELEASE.jar
BlockFront latest file:  BlockFront-1.21.1-0.6.0.2b-RELEASE.jar
BlockFront latest version:  0.6.0.2b

BlockFront requires NeoForge version: 21.1.77
required NeoForge URL: https://maven.NeoForged.net/releases/net/NeoForged/NeoForge/21.1.77/NeoForge-21.1.77-installer.jar
required NeoForge filename: NeoForge-21.1.77-installer.jar

system BlockFront version: 0.6.0.2b
system NeoForge version: 21.1.77

BlockFront is up to date
NeoForge is up to date
```

if you need to update, you can use update option like: 
```
$ python3 ./main.py update
getting latest BlockFront file: 0.6.0.2b
saved BlockFront to /mnt/c/Users/Username/AppData/Roaming/.minecraft/mods/BlockFront-1.21.1-0.6.0.2b-RELEASE.jar
BlockFront requires NeoForge 21.1.77
getting required NeoForge file: 21.1.77
saved NeoForge to /mnt/c/Users/Username/Documents/minecraft/BlockFront/NeoForge-21.1.77-installer.jar
```