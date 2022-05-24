import argparse
import pandas as pd
import sys

def something():
    print("hi")

def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(help="possible commands", dest="command")
	validate_parser = subparsers.add_parser("validate", help="")

	if len(sys.argv) == 1:
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()

	if args.command == "validate":
		something()

if __name__ == "__main__":
	main()
