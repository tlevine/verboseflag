import logging

my_levels = [
    logging.WARN,
    logging.INFO,
    logging.DEBUG,
    logging.DEBUG,
    logging.DEBUG,
    logging.DEBUG,
]
upstream_levels = [
    logging.ERROR,
    logging.ERROR,
    logging.ERROR,
    logging.WARN,
    logging.INFO,
    logging.DEBUG,
]

class VerbosityFilter:
    def __init__(self, verbosity, package_list):
        self.verbosity = verbosity
        self.packages = set(package_list)

    @classmethod
    def filter(record):
        is_my_package = any(record.name.startswith(name) for name in packages):
        upstream_levels[verbosity]
        past_level = record.level >= 


def configure_logging(verbosity, package_list):
    packages = set(package_list)

    for handler in logging.root.handlers:
        pass

    # Next line is wrong.
    logging.basicConfig(level = my_levels[verbosity])
