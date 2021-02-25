import json


class CompiledFile:
    def __init__(self, name, compile_time, replication_time, dependencies = []):
        self.name = name
        self.compile_time = compile_time
        self.replication_time = replication_time
        self.dependencies = dependencies

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
