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
        args = subcom1_parser.parse_args()
        print("commande 1 !")
        print(subcom1_parser.arg_parser_1)

    elif args.command == "subcom2" :
        args = subcom2_parser.parse_args()
        print("commande 2 !")
        print(subcom2_parser.arg_parser_2)



