import os
import platform
import logging

VERSION = "1.1.3"


def build_windows():
    logging.info("Building dir")
    for i in os.popen(
            "pyinstaller -y -D -w -n CodeLib-Local -i icon\\icon.ico --clean --hidden-import ui --hidden-import "
            "resources --hidden-import syncer --add-data .\\data.db.template;.\\ main.py"):
        print(i)

    logging.info("Creating build-installer.nsi")

    dist_files = dict()
    for root, dirs, files in os.walk("dist\\CodeLib-Local"):
        dist_files[root] = [
            os.path.join(root, f).replace('/', '\\').replace('dist\\CodeLib-Local', '').replace('dist/CodeLib-Local',
                                                                                                '') for f in files]

    with open("build-installer.nsi", "wt") as f:
        f.write(f"""!define PRODUCT_NAME \"CodeLib-Local\"
!define PRODUCT_VERSION \"{VERSION}\"
""")
        f.write(r'''!define PRODUCT_PUBLISHER "CodingCow Personal Office"
!define PRODUCT_WEB_SITE "https://github.com/Lixuannan/CodeLib-Local"
!define PRODUCT_DIR_REGKEY "Software\Microsoft\Windows\CurrentVersion\App Paths\CodeLib-Local.exe"
!define PRODUCT_UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${PRODUCT_NAME}"
!define PRODUCT_UNINST_ROOT_KEY "HKLM"
!define PRODUCT_STARTMENU_REGVAL "NSIS:StartMenuDir"

; MUI 1.67 compatible ------
!include "MUI.nsh"

; MUI Settings
!define MUI_ABORTWARNING
!define MUI_ICON "icon\icon.ico"
!define MUI_UNICON "icon\icon.ico"

; Welcome page
!insertmacro MUI_PAGE_WELCOME
; License page
!define MUI_LICENSEPAGE_CHECKBOX
!insertmacro MUI_PAGE_LICENSE "LICENSE"
; Directory page
!insertmacro MUI_PAGE_DIRECTORY
; Start menu page
var ICONS_GROUP
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "CodeLib-Local"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${PRODUCT_UNINST_ROOT_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${PRODUCT_UNINST_KEY}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${PRODUCT_STARTMENU_REGVAL}"
!insertmacro MUI_PAGE_STARTMENU Application $ICONS_GROUP
; Instfiles page
!insertmacro MUI_PAGE_INSTFILES
; Finish page
!define MUI_FINISHPAGE_RUN "$INSTDIR\CodeLib-Local.exe"
!insertmacro MUI_PAGE_FINISH

; Uninstaller pages
!insertmacro MUI_UNPAGE_INSTFILES

; Language files
!insertmacro MUI_LANGUAGE "SimpChinese"

; MUI end ------

Name "${PRODUCT_NAME} ${PRODUCT_VERSION}"
OutFile "dist\CodeLib-Local-Setup-${PRODUCT_VERSION}.exe"
InstallDir "$PROGRAMFILES\CodeLib-Local"
InstallDirRegKey HKLM "${PRODUCT_DIR_REGKEY}" ""
ShowInstDetails show
ShowUnInstDetails show

Section "MainSection" SEC01
''')
        for i in dist_files:
            path = i.replace('dist\\CodeLib-Local', '')
            f.write(f"  SetOutPath \"{'$INSTDIR' + path}\"\n".replace('/', '\\'))
            for j in dist_files[i]:
                f.write(f"  File \"{'dist/CodeLib-Local' + j}\"\n".replace('/', '\\'))

        f.write(r'''; Shortcuts
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  CreateDirectory "$SMPROGRAMS\$ICONS_GROUP"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\CodeLib-Local.lnk" "$INSTDIR\CodeLib-Local.exe"
  CreateShortCut "$DESKTOP\CodeLib-Local.lnk" "$INSTDIR\CodeLib-Local.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -AdditionalIcons
  SetOutPath $INSTDIR
  !insertmacro MUI_STARTMENU_WRITE_BEGIN Application
  WriteIniStr "$INSTDIR\${PRODUCT_NAME}.url" "InternetShortcut" "URL" "${PRODUCT_WEB_SITE}"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Website.lnk" "$INSTDIR\${PRODUCT_NAME}.url"
  CreateShortCut "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk" "$INSTDIR\uninst.exe"
  !insertmacro MUI_STARTMENU_WRITE_END
SectionEnd

Section -Post
  WriteUninstaller "$INSTDIR\uninst.exe"
  WriteRegStr HKLM "${PRODUCT_DIR_REGKEY}" "" "$INSTDIR\CodeLib-Local.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayName" "$(^Name)"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "UninstallString" "$INSTDIR\uninst.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayIcon" "$INSTDIR\CodeLib-Local.exe"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "DisplayVersion" "${PRODUCT_VERSION}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "URLInfoAbout" "${PRODUCT_WEB_SITE}"
  WriteRegStr ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}" "Publisher" "${PRODUCT_PUBLISHER}"
SectionEnd


Function un.onUninstSuccess
  HideWindow
  MessageBox MB_ICONINFORMATION|MB_OK "$(^Name) was successfully removed from your computer."
FunctionEnd

Function un.onInit
  MessageBox MB_ICONQUESTION|MB_YESNO|MB_DEFBUTTON2 "Are you sure you want to completely remove $(^Name) and all of its components?" IDYES +2
  Abort
FunctionEnd

Section Uninstall
  !insertmacro MUI_STARTMENU_GETFOLDER "Application" $ICONS_GROUP
''')
        for i in dist_files:
            for j in dist_files[i]:
                f.write(f"  Delete \"{'$INSTDIR' + j}\"\n".replace('/', '\\'))

        f.write(r'''  Delete "$INSTDIR\data.db"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\CodeLib-Local.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\CodeLib-Local.lnk"
''')
        for i in reversed(dist_files):
            path = i.replace('dist\\CodeLib-Local', '')
            f.write(f"  RMDir \"{'$INSTDIR' + path}\"\n".replace('/', '\\'))

        f.write(r'''  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd''')

        os.popen('build-installer.nsi')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    if platform.system() == 'Windows':
        build_windows()
