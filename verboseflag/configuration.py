import logging

def configure_logging(verbosity):
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

    for handler in logging.root.handlers:
        pass

    # Next line is wrong.
    logging.basicConfig(level = my_levels[verbosity])
