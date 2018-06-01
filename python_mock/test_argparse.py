import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--mem-for-binary-diff", default=25)
options= parser.parse_args(sys.argv[1:])

print options
print options.mem_for_binary_diff