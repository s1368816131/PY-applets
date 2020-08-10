from howdoi import howdoi

query = "pdf to word"
parser = howdoi.get_parser()
args = vars(parser.parse_args(query.split(' ')))

output = howdoi.howdoi(args)