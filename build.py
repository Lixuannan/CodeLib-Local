import os


for i in os.popen("pyinstaller -y -D -w -n CodeLib-Local -i icon\\icon.ico --clean --hidden-import ui --hidden-import "
                  "resources --hidden-import syncer --add-data .\\data.db.template;.\\ main.py"):
    print(i)

s = ""
for root, dirs, files in os.walk("G:\\Project\\CodeLib-Local\\dist\\CodeLib-Local"):
    x = root.replace('G:\\Project\\CodeLib-Local\\dist\\CodeLib-Local', '')
    for file in files:
        t = f"Source: \"{os.path.join(root, file)}\"; DestDir: " + "\"{app}" + f"{x}\";"
        s += t + '\n'

with open("packaging.iss", "wt") as f:
    f.write("""; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "CodeLib-Local"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "CodingCow's Perosonal Office"
#define MyAppURL "https://github.com/lixuannan/CodeLib-Local"
#define MyAppExeName "CodeLib-Local.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{24AA0E85-23EA-4004-830B-FD7D32598DDC}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\\{#MyAppName}
DefaultGroupName={#MyAppName}
AllowNoIcons=yes
LicenseFile=G:\\Project\\CodeLib-Local\\LICENSE
; Remove the following line to run in administrative install mode (install for all users.)
PrivilegesRequired=lowest
PrivilegesRequiredOverridesAllowed=dialog
OutputDir=G:\\Project\\CodeLib-Local\dist
OutputBaseFilename=CodeLib-Local-Setup-Win
SetupIconFile=G:\\Project\\CodeLib-Local\\icon\\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "chinesesimplified"; MessagesFile: "compiler:Languages\\ChineseSimplified.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
""")
    f.write(s)
    f.write("""
[Icons]
Name: "{group}\\{#MyAppName}"; Filename: "{app}\\{#MyAppExeName}"
Name: "{group}\\{cm:ProgramOnTheWeb,{#MyAppName}}"; Filename: "{#MyAppURL}"
Name: "{group}\\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\\{#MyAppName}"; Filename: "{app}\\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

""")

# os.popen("packaging.iss")