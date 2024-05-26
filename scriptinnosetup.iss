; Script de base pour l'installation de Mona Technology Menu d'extinction windows xp

[Setup]
AppName=Menu d'extinction Windows XP
AppVersion=1.0.0
DefaultDirName={pf}\Menu d'extinction Windows XP
DefaultGroupName=Menu d'extinction Windows XP
UninstallDisplayIcon={app}\{#AppName}.exe
OutputDir=Output

[Files]
Source: "chemin_vers_votre_exe\VotreExe.exe"; DestDir: "{app}"
Source: "chemin_vers_vos_assets\*"; DestDir: "{app}\assets"; Flags: recursesubdirs

[Icons]
Name: "{commondesktop}\Menu d'extinction Windows XP"; Filename: "{app}\VotreExe.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\VotreExe.exe"; Description: "Lancer Menu d'extinction Windows XP"; Flags: nowait postinstall skipifsilent
