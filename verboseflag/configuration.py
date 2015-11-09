import logging

levels = [
    logging.INFO,
    logging.WARN,
    logging.DEBUG,
]

class VerbosityFilter:
    def __init__(self, verbosity, package_list, only_mine):
        if verbosity == 0:
            self.level = logging.ERROR
        else:
            self.level = levels[int(verbosity) % 3]
        self.packages = set(package_list)
        self.only_mine = bool(only_mine)

    def filter(self, record):
        is_my_package = any(record.name.startswith(name) for name in self.packages)

        if self.only_mine:
            if is_my_package:
                return record.level >= self.level
            else:
                return False
        else:
            if is_my_package:
                return True
            else:
                return record.level >= self.level

def configure_logging(verbosity, package_list):
    logging.basicConfig(level = logging.DEBUG)
    vf = VerbosityFilter(verbosity, package_list, verbosity <= 2)
    for handler in logging.root.handlers:
        handler.addFilter(vf)
