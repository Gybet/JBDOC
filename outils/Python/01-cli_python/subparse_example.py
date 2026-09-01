import argparse

if __name__ == "__main__":


    parser = argparse.ArgumentParser(prog = "subarpse_example")

    #passage en mode sous parsers
    subparsers = parser.add_subparsers(dest = "command", required = True)

    #creation des sous parsers
    subcom1_parser = subparsers.add_parser("subcom1")
    subcom2_parser = subparsers.add_parser("subcom2")


    #definition des args pour chaque sous parser
    subcom1_parser.add_argument("arg_parser_1")
    subcom2_parser.add_argument("arg_parser_2")


    args = parser.parse_args()

    if args.command == "subcom1" : 
        print("commande 1 !")

    elif args.command == "subcom2" :
        print("commande 2 !")



