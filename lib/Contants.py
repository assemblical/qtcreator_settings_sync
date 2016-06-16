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

    # sync config file
    SYNC_CONFIG_FILE = ""

    # config ini file categories
    CONFIG_INI_FILE_CATEGORIES = []

    @staticmethod
    def init():

        Constants.SYNC_CONFIG_FILE = os.path.dirname(__file__) + '/../config.json'
        Constants.EXPORTER_DIR = os.path.dirname(os.path.realpath(__file__)) + "/../exported"
        Constants.EXPORTER_CONFIG_FILE = Constants.EXPORTER_DIR + "/QtCreator.ini"

        # os specific storage paths
        if Constants.OS == Constants.WINDOWS:
            Constants.QTCREATOR_CONFIG_DIR = os.environ["APPDATA"] + "\\QtProject\\"
            Constants.QTCREATOR_CONFIG_FILE = Constants.QTCREATOR_CONFIG_DIR + "QtCreator.ini"
        if Constants.OS == Constants.MACOS:
            print("TODO")
        if Constants.OS == Constants.LINUX:
            print("TODO")

'''
    possible ini file categories
    INI_FILE_CATEGORIES = [
        "General",
        "CppCodeStyleSettings",
        "QmlJSTabPreferences",
        "Navigation",
        "OutputPaneVisibility",
        "OutputPanePlaceHolder",
        "StatusBar",
        "Find",
        "SearchResults",
        "ProjectExplorer",
        "bazaar",
        "CVS",
        "Git",
        "Mercurial",
        "Console",
        "Subversion",
        "DebugMode",
        "QML.Inpector",
        "CDB2",
        "GenericProject",
        "CompleterHistory",
        "%General",
        "MainWindow",
        "RecentFiles",
        "Directories",
        "EditorManager",
        "Help",
        "ExternalTools",
        "Analyzer",
        "QbsProjectManager",
        "Core",
        "FakeVim",
        "FakeVimExCommand",
        "FakeVimUserCommand",
        "KeyboardShortcuts",
        "TextEditor",
        "TextSnippetsSettings",
        "CppTools",
        "Debugger.Perspective.Cpp",
        "textTabPreferences",
        "textMarginSettings",
        "AndroidConfiguration",
        "ClangStaticAnalyzer",
    ]
'''
