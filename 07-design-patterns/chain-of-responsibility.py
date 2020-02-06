def logger(content):
    print(content)
    return content


def my_filter(content):
    return filter(lambda e: len(e) > 2, content)


def augment(data):
    return map(lambda e: e + "*", data)


class Chain(object):
    def __init__(self, functions=None):
        self._functions = []
        if functions is not None:
            self._functions += functions

    def execute(self, content):
        for func in self._functions:
            content = func(content)
        return content


chain = Chain([logger, my_filter, augment])
processed_content = chain.execute(['jeh', 'jh', 'ph', 'phh', 'ajph'])
print(list(processed_content))
