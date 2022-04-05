import re


class CodeLinesChangedHelper:
    def isSrc(filename: str, test: bool = False) -> bool:
        extension = re.search("(\w)+$", filename).group()
        if (extension == "ts" or extension == "js" or extension == "py"):
            if (filename.lower().find("test", 0, 4) == -1) != test:
                return True
        return False