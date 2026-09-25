import sys
import json

values_file = sys.argv[1]
tests_file = sys.argv[2]
report_file = sys.argv[3]

with open(values_file, 'r') as f:
    values = json.load(f)

values = values['values']

with open(tests_file, 'r') as f:
    tests = json.load(f)

def add_values(test):
    if 'id' in test:
        for value in values:
            if value['id'] == test['id']:
                test['value'] = value['value']

    if 'values' in test:
        for item in test['values']:
            add_values(item)

for test in tests['tests']:
    add_values(test)

with open(report_file, 'w') as f:
    json.dump(tests, f, indent=4)