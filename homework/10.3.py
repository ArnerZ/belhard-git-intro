import json
import yaml

tt = {
    'age': 34,
    'name': 'Sergey',
    'children': [
        {
            'age': 7,
            'name': 'Anton'
        }
    ],
    'married': True,
    'city': None
}

print(tt)
tt_sorting = json.dumps(tt)
print(tt_sorting)
tt_desorting = json.loads(tt_sorting)
print(tt_desorting)

with open("file_json.txt", "w") as f:
    json.dump(tt, f)

with open("file_json.txt", "r") as f:
    tt_desorting_file = json.load(f)
print(tt_desorting_file)


tt_sorting_yaml = yaml.dump(tt)
print(tt_sorting_yaml)
tt_desorting_yaml = yaml.full_load(tt_sorting_yaml)
print(tt_desorting_yaml)

with open("file_yaml.txt", "w") as f:
    yaml.dump(tt, f)

with open("file_yaml.txt", "r") as f:
    tt_desorting_yaml = yaml.safe_load(f)
print(tt_desorting_yaml)