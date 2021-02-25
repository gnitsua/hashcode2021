import json
from dataclasses import dataclass
from typing import List

from CompiledFile import CompiledFile

@dataclass
class Input:
    targets:List
    servers:List

    def __init__(self, targets, servers, compiled_files):
        self.targets = targets
        self.servers = servers
        self.compiled_files = compiled_files

    @staticmethod
    def parse(filename):
        with open("./inputs/" + filename, "r") as file:
            input_info_line = file.readline().strip("\n").split(" ")
            assert (len(input_info_line) == 3)
            num_files, num_targets, servers = input_info_line  # ignore number of files

            compiled_files = {}

            for _ in range(0, int(num_files)):  # read in each file
                file_info_line = file.readline().strip("\n").split(" ")  # read in first line of file info
                assert (len(file_info_line) == 3)

                file_dependency_line = file.readline().strip("\n").split(" ")  # now read in dependencies
                assert (len(file_dependency_line) > 0)

                compiled_files[file_info_line[0]] = CompiledFile(file_info_line[0],
                                                                 int(file_info_line[1]),
                                                                 int(file_info_line[2]))

                if (file_dependency_line[0] != '0'):  # has dependencies
                    assert (len(file_dependency_line) > 1)
                    dependencies = file_dependency_line[1:]  # strip off the count

                    compiled_files[file_info_line[0]].dependencies = dependencies

            targets = []

            for _ in range(0, int(num_targets)):
                target_info_line = file.readline().strip("\n").split(" ")
                assert (len(target_info_line) == 3)

                targets.append({
                    "name": target_info_line[0],
                    "deadline": int(target_info_line[1]),
                    "points": int(target_info_line[1])
                })

        return Input(targets, servers, compiled_files)

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
