from collections import defaultdict

class StringCounter():
    def __init__(self):
        self._strings = defaultdict(int)

    def count(self, string):
        self._strings[string] += 1

    def remove(self, string):
        try:
            del d[string]
        except Exception:
            pass

    def clear(self):
        self._strings = defaultdict(int)

    def sorted_keys(self):
        return sorted(self._strings, key=self._strings.get, reverse=True)

    def __getattr__(self, string):
        return self._strings[string]


