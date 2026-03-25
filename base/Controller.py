class Controller:
    def valid_str(self, string: str):
        return isinstance(string, str) and string.strip() != ""