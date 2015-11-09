def add_arguments(argparser, dest = 'verbosity'):
    argparser.add_argument('--verbose', '-v', action='count', dest = dest, default = 0,
                           help = 'Verbosity level, maximum of five Vs')
