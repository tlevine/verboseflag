def add_arguments(argparser, dest = 'verbosity'):
    argparser.add_argument('--verbose', '-v', action='count', dest = dest,
                           help = 'Verbosity level, maximum of five Vs')
