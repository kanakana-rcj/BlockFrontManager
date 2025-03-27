# BlockFrontManager
BlockFrontManager is version-manager of blockfront, which is the mod of MineCraft.

## Using language
<img src="https://img.shields.io/badge/-python-blue?style=flat&logo=python&logoColor=yellow">

## Supported OS
GNU/Linux 3.2.0, and Windows 11.

For Linux, you can use main.bin. For windows, you can use main.exe.

## how to use
### setting env
set enviroment variables in .env 
```
BLOCKFRONT_PATH = "C/Users/username/AppData/Roaming/.minecraft/mods"
NEOFORGE_PATH = "C/Users/username/Documents/minecraft/blockfront"
```

### using command
You can use command with following options: "status", and "update".

With "status" option, you can collect information of Blockfront and neoforge.
```bash
$ python ./main.py status

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

With "update" option, you can update your BlockFront and Neoforge.
```bash
$ python ./main.py update
getting latest BlockFront file: 0.6.0.2b
saved BlockFront to /mnt/c/Users/Username/AppData/Roaming/.minecraft/mods/BlockFront-1.21.1-0.6.0.2b-RELEASE.jar
BlockFront requires NeoForge 21.1.77
getting required NeoForge file: 21.1.77
saved NeoForge to /mnt/c/Users/Username/Documents/minecraft/BlockFront/NeoForge-21.1.77-installer.jar
```