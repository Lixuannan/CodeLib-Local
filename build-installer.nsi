!define PRODUCT_NAME "CodeLib-Local"
!define PRODUCT_VERSION "v1.1.4"
!define PRODUCT_PUBLISHER "CodingCow Personal Office"
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
  SetOutPath "$INSTDIR"
  File "dist\CodeLib-Local\CodeLib-Local.exe"
  SetOutPath "$INSTDIR\_internal"
  File "dist\CodeLib-Local\_internal\python311.dll"
  File "dist\CodeLib-Local\_internal\select.pyd"
  File "dist\CodeLib-Local\_internal\pyexpat.pyd"
  File "dist\CodeLib-Local\_internal\_lzma.pyd"
  File "dist\CodeLib-Local\_internal\_bz2.pyd"
  File "dist\CodeLib-Local\_internal\_ssl.pyd"
  File "dist\CodeLib-Local\_internal\_hashlib.pyd"
  File "dist\CodeLib-Local\_internal\unicodedata.pyd"
  File "dist\CodeLib-Local\_internal\_decimal.pyd"
  File "dist\CodeLib-Local\_internal\_multiprocessing.pyd"
  File "dist\CodeLib-Local\_internal\_ctypes.pyd"
  File "dist\CodeLib-Local\_internal\_queue.pyd"
  File "dist\CodeLib-Local\_internal\_overlapped.pyd"
  File "dist\CodeLib-Local\_internal\_asyncio.pyd"
  File "dist\CodeLib-Local\_internal\_socket.pyd"
  File "dist\CodeLib-Local\_internal\_sqlite3.pyd"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-locale-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-math-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-environment-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-runtime-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-stdio-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-heap-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\zlib.dll"
  File "dist\CodeLib-Local\_internal\VCRUNTIME140.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-conio-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-filesystem-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-string-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-time-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-process-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-convert-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\MSVCP140.dll"
  File "dist\CodeLib-Local\_internal\VCRUNTIME140_1.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-crt-utility-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\liblzma.dll"
  File "dist\CodeLib-Local\_internal\LIBBZ2.dll"
  File "dist\CodeLib-Local\_internal\libssl-3-x64.dll"
  File "dist\CodeLib-Local\_internal\libcrypto-3-x64.dll"
  File "dist\CodeLib-Local\_internal\ffi.dll"
  File "dist\CodeLib-Local\_internal\python3.dll"
  File "dist\CodeLib-Local\_internal\sqlite3.dll"
  File "dist\CodeLib-Local\_internal\ucrtbase.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-synch-l1-2-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-profile-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-console-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-heap-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-debug-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-processthreads-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-memory-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-processthreads-l1-1-1.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-localization-l1-2-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-file-l2-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-timezone-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-sysinfo-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-synch-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-datetime-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-errorhandling-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-interlocked-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-rtlsupport-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-util-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-file-l1-2-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-handle-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-file-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-namedpipe-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-libraryloader-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-string-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\api-ms-win-core-processenvironment-l1-1-0.dll"
  File "dist\CodeLib-Local\_internal\data.db.template"
  File "dist\CodeLib-Local\_internal\base_library.zip"
  SetOutPath "$INSTDIR\_internal\PySide6"
  File "dist\CodeLib-Local\_internal\PySide6\opengl32sw.dll"
  File "dist\CodeLib-Local\_internal\PySide6\QtNetwork.pyd"
  File "dist\CodeLib-Local\_internal\PySide6\QtGui.pyd"
  File "dist\CodeLib-Local\_internal\PySide6\QtWidgets.pyd"
  File "dist\CodeLib-Local\_internal\PySide6\QtCore.pyd"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Network.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Core.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Gui.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6VirtualKeyboard.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Svg.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Pdf.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Widgets.dll"
  File "dist\CodeLib-Local\_internal\PySide6\VCRUNTIME140_1.dll"
  File "dist\CodeLib-Local\_internal\PySide6\MSVCP140.dll"
  File "dist\CodeLib-Local\_internal\PySide6\VCRUNTIME140.dll"
  File "dist\CodeLib-Local\_internal\PySide6\pyside6.abi3.dll"
  File "dist\CodeLib-Local\_internal\PySide6\MSVCP140_2.dll"
  File "dist\CodeLib-Local\_internal\PySide6\MSVCP140_1.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Qml.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6Quick.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6QmlModels.dll"
  File "dist\CodeLib-Local\_internal\PySide6\Qt6OpenGL.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\networkinformation"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\networkinformation\qnetworklistmanager.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\tls"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\tls\qcertonlybackend.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\tls\qschannelbackend.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\tls\qopensslbackend.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\platforms"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\platforms\qdirect2d.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\platforms\qwindows.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\platforms\qminimal.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\platforms\qoffscreen.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\imageformats"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qwbmp.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qwebp.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qsvg.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qico.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qpdf.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qjpeg.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qtga.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qtiff.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qgif.dll"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\imageformats\qicns.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\generic"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\generic\qtuiotouchplugin.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\platforminputcontexts"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\platforminputcontexts\qtvirtualkeyboardplugin.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\iconengines"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\iconengines\qsvgicon.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\plugins\styles"
  File "dist\CodeLib-Local\_internal\PySide6\plugins\styles\qwindowsvistastyle.dll"
  SetOutPath "$INSTDIR\_internal\PySide6\translations"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_fi.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_tr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_tr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_bg.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_bg.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_pt_PT.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_hr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_hr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_ru.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_pl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_gd.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_zh_CN.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_fa.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_zh_CN.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_fr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_ko.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_pt_BR.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_ja.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_ja.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_it.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_cs.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_es.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_de.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_fa.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_gl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_sk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_gd.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_ar.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_lv.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_de.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_lv.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_sk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_hu.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_ko.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_uk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_hu.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_pt_BR.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_da.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_es.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_he.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_zh_TW.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_ru.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_cs.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_nl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_tr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_pt_BR.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_sl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_zh_CN.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_it.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_zh_TW.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_da.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_bg.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_ar.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_en.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_lt.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_nl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_fr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_it.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_en.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_hr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_ru.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_fr.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_pl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_uk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_en.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_zh_TW.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_sv.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_ko.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_nn.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_he.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_nn.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_fi.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_de.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_sk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_hu.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_pl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_ca.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_nl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_ar.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_ja.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_sl.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_uk.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_ca.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qtbase_ca.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_nn.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_cs.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_es.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_da.qm"
  File "dist\CodeLib-Local\_internal\PySide6\translations\qt_help_gl.qm"
  SetOutPath "$INSTDIR\_internal\shiboken6"
  File "dist\CodeLib-Local\_internal\shiboken6\Shiboken.pyd"
  File "dist\CodeLib-Local\_internal\shiboken6\shiboken6.abi3.dll"
  File "dist\CodeLib-Local\_internal\shiboken6\VCRUNTIME140_1.dll"
  File "dist\CodeLib-Local\_internal\shiboken6\VCRUNTIME140.dll"
  File "dist\CodeLib-Local\_internal\shiboken6\MSVCP140.dll"
  SetOutPath "$INSTDIR\_internal\charset_normalizer"
  File "dist\CodeLib-Local\_internal\charset_normalizer\md__mypyc.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\charset_normalizer\md.cp311-win_amd64.pyd"
  SetOutPath "$INSTDIR\_internal\lxml"
  File "dist\CodeLib-Local\_internal\lxml\etree.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\lxml\_elementpath.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\lxml\sax.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\lxml\objectify.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\lxml\builder.cp311-win_amd64.pyd"
  SetOutPath "$INSTDIR\_internal\lxml\html"
  File "dist\CodeLib-Local\_internal\lxml\html\diff.cp311-win_amd64.pyd"
  File "dist\CodeLib-Local\_internal\lxml\html\clean.cp311-win_amd64.pyd"
  SetOutPath "$INSTDIR\_internal\lxml\isoschematron"
  SetOutPath "$INSTDIR\_internal\lxml\isoschematron\resources"
  SetOutPath "$INSTDIR\_internal\lxml\isoschematron\resources\xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl"
  SetOutPath "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_dsdl_include.xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_message.xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_svrl_for_xslt1.xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_abstract_expand.xsl"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\readme.txt"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_skeleton_for_xslt1.xsl"
  SetOutPath "$INSTDIR\_internal\lxml\isoschematron\resources\rng"
  File "dist\CodeLib-Local\_internal\lxml\isoschematron\resources\rng\iso-schematron.rng"
  SetOutPath "$INSTDIR\_internal\certifi"
  File "dist\CodeLib-Local\_internal\certifi\py.typed"
  File "dist\CodeLib-Local\_internal\certifi\cacert.pem"
; Shortcuts
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
  Delete "$INSTDIR\CodeLib-Local.exe"
  Delete "$INSTDIR\_internal\python311.dll"
  Delete "$INSTDIR\_internal\select.pyd"
  Delete "$INSTDIR\_internal\pyexpat.pyd"
  Delete "$INSTDIR\_internal\_lzma.pyd"
  Delete "$INSTDIR\_internal\_bz2.pyd"
  Delete "$INSTDIR\_internal\_ssl.pyd"
  Delete "$INSTDIR\_internal\_hashlib.pyd"
  Delete "$INSTDIR\_internal\unicodedata.pyd"
  Delete "$INSTDIR\_internal\_decimal.pyd"
  Delete "$INSTDIR\_internal\_multiprocessing.pyd"
  Delete "$INSTDIR\_internal\_ctypes.pyd"
  Delete "$INSTDIR\_internal\_queue.pyd"
  Delete "$INSTDIR\_internal\_overlapped.pyd"
  Delete "$INSTDIR\_internal\_asyncio.pyd"
  Delete "$INSTDIR\_internal\_socket.pyd"
  Delete "$INSTDIR\_internal\_sqlite3.pyd"
  Delete "$INSTDIR\_internal\api-ms-win-crt-locale-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-math-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-environment-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-runtime-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-stdio-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-heap-l1-1-0.dll"
  Delete "$INSTDIR\_internal\zlib.dll"
  Delete "$INSTDIR\_internal\VCRUNTIME140.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-conio-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-filesystem-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-string-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-time-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-process-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-convert-l1-1-0.dll"
  Delete "$INSTDIR\_internal\MSVCP140.dll"
  Delete "$INSTDIR\_internal\VCRUNTIME140_1.dll"
  Delete "$INSTDIR\_internal\api-ms-win-crt-utility-l1-1-0.dll"
  Delete "$INSTDIR\_internal\liblzma.dll"
  Delete "$INSTDIR\_internal\LIBBZ2.dll"
  Delete "$INSTDIR\_internal\libssl-3-x64.dll"
  Delete "$INSTDIR\_internal\libcrypto-3-x64.dll"
  Delete "$INSTDIR\_internal\ffi.dll"
  Delete "$INSTDIR\_internal\python3.dll"
  Delete "$INSTDIR\_internal\sqlite3.dll"
  Delete "$INSTDIR\_internal\ucrtbase.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-synch-l1-2-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-profile-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-console-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-heap-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-debug-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-processthreads-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-memory-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-processthreads-l1-1-1.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-localization-l1-2-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-file-l2-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-timezone-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-sysinfo-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-synch-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-datetime-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-errorhandling-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-interlocked-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-rtlsupport-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-util-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-file-l1-2-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-handle-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-file-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-namedpipe-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-libraryloader-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-string-l1-1-0.dll"
  Delete "$INSTDIR\_internal\api-ms-win-core-processenvironment-l1-1-0.dll"
  Delete "$INSTDIR\_internal\data.db.template"
  Delete "$INSTDIR\_internal\base_library.zip"
  Delete "$INSTDIR\_internal\PySide6\opengl32sw.dll"
  Delete "$INSTDIR\_internal\PySide6\QtNetwork.pyd"
  Delete "$INSTDIR\_internal\PySide6\QtGui.pyd"
  Delete "$INSTDIR\_internal\PySide6\QtWidgets.pyd"
  Delete "$INSTDIR\_internal\PySide6\QtCore.pyd"
  Delete "$INSTDIR\_internal\PySide6\Qt6Network.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Core.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Gui.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6VirtualKeyboard.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Svg.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Pdf.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Widgets.dll"
  Delete "$INSTDIR\_internal\PySide6\VCRUNTIME140_1.dll"
  Delete "$INSTDIR\_internal\PySide6\MSVCP140.dll"
  Delete "$INSTDIR\_internal\PySide6\VCRUNTIME140.dll"
  Delete "$INSTDIR\_internal\PySide6\pyside6.abi3.dll"
  Delete "$INSTDIR\_internal\PySide6\MSVCP140_2.dll"
  Delete "$INSTDIR\_internal\PySide6\MSVCP140_1.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Qml.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6Quick.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6QmlModels.dll"
  Delete "$INSTDIR\_internal\PySide6\Qt6OpenGL.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\networkinformation\qnetworklistmanager.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\tls\qcertonlybackend.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\tls\qschannelbackend.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\tls\qopensslbackend.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\platforms\qdirect2d.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\platforms\qwindows.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\platforms\qminimal.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\platforms\qoffscreen.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qwbmp.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qwebp.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qsvg.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qico.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qpdf.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qjpeg.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qtga.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qtiff.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qgif.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\imageformats\qicns.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\generic\qtuiotouchplugin.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\platforminputcontexts\qtvirtualkeyboardplugin.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\iconengines\qsvgicon.dll"
  Delete "$INSTDIR\_internal\PySide6\plugins\styles\qwindowsvistastyle.dll"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_fi.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_tr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_tr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_bg.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_bg.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_pt_PT.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_hr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_hr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_ru.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_pl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_gd.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_zh_CN.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_fa.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_zh_CN.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_fr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_ko.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_pt_BR.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_ja.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_ja.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_it.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_cs.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_es.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_de.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_fa.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_gl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_sk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_gd.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_ar.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_lv.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_de.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_lv.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_sk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_hu.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_ko.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_uk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_hu.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_pt_BR.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_da.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_es.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_he.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_zh_TW.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_ru.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_cs.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_nl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_tr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_pt_BR.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_sl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_zh_CN.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_it.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_zh_TW.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_da.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_bg.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_ar.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_en.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_lt.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_nl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_fr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_it.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_en.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_hr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_ru.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_fr.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_pl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_uk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_en.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_zh_TW.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_sv.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_ko.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_nn.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_he.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_nn.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_fi.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_de.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_sk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_hu.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_pl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_ca.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_nl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_ar.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_ja.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_sl.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_uk.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_ca.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qtbase_ca.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_nn.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_cs.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_es.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_da.qm"
  Delete "$INSTDIR\_internal\PySide6\translations\qt_help_gl.qm"
  Delete "$INSTDIR\_internal\shiboken6\Shiboken.pyd"
  Delete "$INSTDIR\_internal\shiboken6\shiboken6.abi3.dll"
  Delete "$INSTDIR\_internal\shiboken6\VCRUNTIME140_1.dll"
  Delete "$INSTDIR\_internal\shiboken6\VCRUNTIME140.dll"
  Delete "$INSTDIR\_internal\shiboken6\MSVCP140.dll"
  Delete "$INSTDIR\_internal\charset_normalizer\md__mypyc.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\charset_normalizer\md.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\etree.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\_elementpath.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\sax.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\objectify.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\builder.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\html\diff.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\html\clean.cp311-win_amd64.pyd"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_dsdl_include.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_message.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_svrl_for_xslt1.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_abstract_expand.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\readme.txt"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_skeleton_for_xslt1.xsl"
  Delete "$INSTDIR\_internal\lxml\isoschematron\resources\rng\iso-schematron.rng"
  Delete "$INSTDIR\_internal\certifi\py.typed"
  Delete "$INSTDIR\_internal\certifi\cacert.pem"
  Delete "$INSTDIR\data.db"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Uninstall.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\Website.lnk"
  Delete "$DESKTOP\CodeLib-Local.lnk"
  Delete "$SMPROGRAMS\$ICONS_GROUP\CodeLib-Local.lnk"
  RMDir "$INSTDIR\_internal\certifi"
  RMDir "$INSTDIR\_internal\lxml\isoschematron\resources\rng"
  RMDir "$INSTDIR\_internal\lxml\isoschematron\resources\xsl\iso-schematron-xslt1"
  RMDir "$INSTDIR\_internal\lxml\isoschematron\resources\xsl"
  RMDir "$INSTDIR\_internal\lxml\isoschematron\resources"
  RMDir "$INSTDIR\_internal\lxml\isoschematron"
  RMDir "$INSTDIR\_internal\lxml\html"
  RMDir "$INSTDIR\_internal\lxml"
  RMDir "$INSTDIR\_internal\charset_normalizer"
  RMDir "$INSTDIR\_internal\shiboken6"
  RMDir "$INSTDIR\_internal\PySide6\translations"
  RMDir "$INSTDIR\_internal\PySide6\plugins\styles"
  RMDir "$INSTDIR\_internal\PySide6\plugins\iconengines"
  RMDir "$INSTDIR\_internal\PySide6\plugins\platforminputcontexts"
  RMDir "$INSTDIR\_internal\PySide6\plugins\generic"
  RMDir "$INSTDIR\_internal\PySide6\plugins\imageformats"
  RMDir "$INSTDIR\_internal\PySide6\plugins\platforms"
  RMDir "$INSTDIR\_internal\PySide6\plugins\tls"
  RMDir "$INSTDIR\_internal\PySide6\plugins\networkinformation"
  RMDir "$INSTDIR\_internal\PySide6\plugins"
  RMDir "$INSTDIR\_internal\PySide6"
  RMDir "$INSTDIR\_internal"
  RMDir "$INSTDIR"
  DeleteRegKey ${PRODUCT_UNINST_ROOT_KEY} "${PRODUCT_UNINST_KEY}"
  DeleteRegKey HKLM "${PRODUCT_DIR_REGKEY}"
  SetAutoClose true
SectionEnd