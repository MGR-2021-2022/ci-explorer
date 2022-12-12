import re


class CodeLinesChangedHelper:
    def isSrc(filename: str, test: bool = False) -> bool:
        extension = re.search("(\w)+$", filename)
        if extension is None:
            return False
        extension = extension.group()

        if extension == "ts" or extension == "js" or extension == "jsx" or extension == "py" or extension == "cpp" or extension == "h" or extension == "go" or extension == "php"\
                or extension == "dart" or extension == "rs":
            if (filename.lower().find("test") == -1) != test:
                return True
        return False