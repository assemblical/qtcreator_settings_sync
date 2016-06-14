import platform
import os


class Constants:
    # os
    WINDOWS = "Windows"
    LINUX = "Linux"
    MACOS = "TODO"

    OS = platform.system()

    # file system
    EXPORTER_DIR = ""
    EXPORTER_CONFIG_FILE = ""

    QTCREATOR_CONFIG_DIR = ""
    QTCREATOR_CONFIG_FILE = ""

    @staticmethod
    def init():
        if Constants.OS == Constants.WINDOWS:
            Constants.EXPORTER_DIR = os.path.dirname(os.path.realpath(__file__)) + "\\exported"
            Constants.EXPORTER_CONFIG_FILE = Constants.EXPORTER_DIR + "\\QtCreator.ini"

            Constants.QTCREATOR_CONFIG_DIR = os.environ["APPDATA"] + "\\QtProject\\"
            Constants.QTCREATOR_CONFIG_FILE = Constants.QTCREATOR_CONFIG_DIR + "QtCreator.ini"
        if Constants.OS == Constants.MACOS:
            print("TODO")
        if Constants.OS == Constants.LINUX:
            print("TODO")

    # ini file categories
    INI_FILE_CATEGORIES = {
        "GENERAL": "[General]",
        "CPPCODESTYLESETTINGS": "[CppCodeStyleSettings]",
        "QMLJSTABPREFERENCES": "[QmlJSTabPreferences]",
        "NAVIGATION": "[Navigation]",
        "OUTPUTPANEVISBILITY": "[OutputPaneVisibility]",
        "OUTPUTPANEPLACEHOLDER": "[OutputPanePlaceHolder]",
        "STATUSBAR": "[StatusBar]",
        "FIND": "[Find]",
        "SEARCHRESULTS": "[SearchResults]",
        "PROJECTEXPLORER": "[ProjectExplorer]",
        "BAZAAR": "[bazaar]",
        "CVS": "[CVS]",
        "GIT": "[Git]",
        "MERCURIAL": "[Mercurial]",
        "CONSOLE": "[Console]",
        "SUBVERSION": "[Subversion]",
        "DEBUGMODE": "[DebugMode]",
        "QMLINSPECTOR": "[QML.Inspector]",
        "CDB2": "[CDB2]",
        "GENERICPROJECT": "[GenericProject]",
        "COMPLETERHISTORY": "[CompleterHistory]",
        "%GENERAL": "[%General]",
        "MAINWINDOW": "[MainWindow]",
        "RECENTFILES": "[RecentFiles]",
        "DIRECTORIES": "[Directories]",
        "EDITORMANAGER": "[EditorManager]",
        "HELP": "[Help]",
        "EXTERNALTOOLS": "[ExternalTools]",
        "ANALYZER": "[Analyzer]",
        "QBSPROJECTMANAGER": "[QbsProjectManager]",
        "CORE": "[Core]",
        "FAKEVIM": "[FakeVim]",
        "FAKEVIMEXCOMMAND": "[FakeVimExCommand]",
        "FAKEVIMUSERCOMMAND": "[FakeVimUserCommand]",
        "KEYBOARDSHORTCUTS": "[KeyboardShortcuts]",
        "TEXTEDITOR": "[TextEditor]",
        "TEXTSNIPPETSSETTINGS": "[TextSnippetsSettings]",
        "CPPTOOLS": "[CppTools]",
        "DEBUGGERPERSPECTIVECPP": "[Debugger.Perspective.Cpp]",
        "TEXTTABPREFERENCES": "[textTabPreferences]",
        "TEXTMARGINSETTINGS": "[textMarginSettings]",
        "ANDROIDCONFIGURATION": "[AndroidConfiguration]",
        "CLANGSTATICANALYZER": "[ClangStaticAnalyzer]"
    }
