import json
from pprint import pprint

def load_candidates():
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        candidates = {}
        for i in data:
            candidates[i['id']] = i
        pprint(candidates)
        return data


