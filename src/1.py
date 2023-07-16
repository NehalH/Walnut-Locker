import fileinput
import re

spaces_regex = re.compile(r'    ')

for line in fileinput.input('grant.py', inplace=True):
    print(re.sub(spaces_regex, '\t', line.rstrip()))