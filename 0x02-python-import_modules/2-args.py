#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
argc = len(argv)
if argc < 2:
    print("{} arguments.".format(argc - 1))
else:
    if argc == 2:
        print("1 argument:")
    elif argc == 3:
        print("2 arguments:")
    else:
        print("{} arguments:".format(argc - 1))
    for n in range(1, argc):
        print("{}: {}".format(n, argv[n]))
