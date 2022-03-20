'''
@Time    : 2021/1/27 19:38
@Author  : 19045845
'''


class Registry:
    def __init__(self, name):
        self._name = name
        self._module_dict = dict()

    @property
    def name(self):
        return self._name

    @property
    def module_dict(self):
        return self._module_dict

    def get(self, key):
        return self._module_dict.get(key, None)

    def _register_module(self, model_func):
        module_name = model_func.__name__
        if module_name in self._module_dict:
            raise KeyError('{} is already registered in {}'.format(
                module_name, self.name))

        self._module_dict[module_name] = model_func

    def register_module(self, func):
        self._register_module(func)
        return func


Animal = Registry("animal")


@Animal.register_module
def run(word1,word2):
    print("runing" + word1 + word2 )


Animal.get("run")("wangwang","11111111111")
