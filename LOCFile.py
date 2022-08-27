# Jerrin Shirks

def nameof(*args):
    return [name for name in globals() if globals()[name] is args[0]][0]



class LOCFile:

    class InvalidLanguageException(Exception):
        pass

    class KeyNotFoundException(Exception):
        pass

    def __init__(self):

        self.ValidLanguages = [
            "cs-CS", "cs-CZ", "da-CH", "da-DA",
            "da-DK", "de-AT", "de-DE", "el-EL",
            "el-GR", "en-AU", "en-CA", "en-EN",
            "en-GB", "en-GR", "en-IE", "en-NZ",
            "en-US", "es-ES", "es-MX", "fi-BE",
            "fi-CH", "fi-FI", "fr-FR", "fr-CA",
            "it-IT", "ja-JP", "ko-KR", "la-LAS",
            "no-NO", "nb-NO", "nl-NL", "nl-BE",
            "pl-PL", "pt-BR", "pt-PT", "ru-RU",
            "sk-SK", "sv-SE", "tr-TR", "zh-CN",
            "zh-HK", "zh-SG", "zh-TW", "zh-CHT",
            "zh-HanS", "zh-HanT",
        ]

        _lockeys = {}
        _languages = [None] * len(self.ValidLanguages)

        self.LocKeys = _lockeys
        self.Languages = [] # _languages

    def initialize(self, language, locKeyValuePairs):
        self.AddLanguage(language)
        for locKeyValue in locKeyValuePairs:
            self.AddLocKey(locKeyValue, locKeyValuePairs[locKeyValue])

    def GetTranslation(self, locKey):
        if locKey not in self.LocKeys:
            self.LocKeys[locKey] = {}
        return self.LocKeys[locKey]

    # Dictionary<str, str> (str)
    def GetLocEntries(self, locKey):
        if locKey not in self.LocKeys:
            raise self.KeyNotFoundException("Loc key not found")
        return self.LocKeys[locKey]

    # public bool (str)
    def HasLocEntry(self, locKey):
        return locKey in self.LocKeys

    # public str (str, str)
    def GetLocEntry(self, locKey, language):
        if locKey not in self.LocKeys:
            raise self.KeyNotFoundException(nameof(locKey))
        if language not in self.Languages:
            raise self.KeyNotFoundException("Language Entry not found")

        if self.GetTranslation(locKey)[language] is None:
            return str()
        else:
            return self.GetTranslation(locKey)[language]

    # public void (str, str), or public void (str, str, str)
    def SetLocEntry(self, *args):
        if len(args) == 2:
            locKey, value = args
            for language in self.Languages:
                self.GetTranslation(locKey)[language] = value

        elif len(args) == 3:
            locKey, language, value = args
            if language not in self.Languages:
                raise self.KeyNotFoundException(nameof(language))
            self.GetTranslation(locKey)[language] = value

    # public bool (str, str)
    def AddLocKey(self, locKey, value):
        if locKey not in self.LocKeys:
            return False
        for language in self.Languages:
            self.SetLocEntry(locKey, language, value)
        return True

    # public bool (str)
    def RemoveLocKey(self, locKey):
        if locKey not in self.LocKeys:
            return False
        remove_key = self.LocKeys.pop(locKey, None)
        return remove_key is not None

    # public void (str)
    def AddLanguage(self, language):
        if language not in self.ValidLanguages:
            raise self.InvalidLanguageException("Invalid language", language)
        if language not in self.Languages:
            raise self.InvalidLanguageException("Language already exists", language)
        self.Languages.append(language)
        for key in self.LocKeys.keys():
            self.SetLocEntry(key, language, "")

    # public void (str)
    def RemoveLanguage(self, language):
        if language not in self.ValidLanguages:
            raise self.InvalidLanguageException("Invalid language", language)
        if language not in self.Languages:
            raise self.InvalidLanguageException("Language doesn't exist", language)

        try:
            self.Languages.remove(language)
            for translation in self.LocKeys.values():
                translation.remove(language)

        except ValueError:
            pass  # do nothing!
