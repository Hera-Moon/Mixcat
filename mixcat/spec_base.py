from flask import Blueprint


class BlueprintWithApiSpec(Blueprint):
    def __init__(self, name, import_name, **kwargs):
        super().__init__(name, import_name, **kwargs)
        self.view_functions_with_spec = []

    def add_url_rule(self, rule, endpoint=None, view_func=None, **kwargs):
        super().add_url_rule(rule, endpoint=endpoint, view_func=view_func, **kwargs,)
        self.view_functions_with_spec.append(view_func)
