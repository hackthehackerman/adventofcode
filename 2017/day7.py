from util import tolines
import re
from collections import Counter

def part1():
    lines = tolines("input/day7")
    programs = {}
    parents = {}
    
    for line in lines:
        # Parse each line using regex
        match = re.match(r'(\w+) \((\d+)\)(?: -> ([\w, ]+))?', line)
        if match:
            name, weight, children = match.groups()
            programs[name] = {
                'weight': int(weight),
                'children': children.split(', ') if children else []
            }
            for child in programs[name]["children"]:
                parents[child] = name
                
    for name in programs:
        if name not in parents:
            print(name)
            break
            

def part2():
    lines = tolines("input/day7")
    programs = {}
    parents = {}
    
    for line in lines:
        # Parse each line using regex
        match = re.match(r'(\w+) \((\d+)\)(?: -> ([\w, ]+))?', line)
        if match:
            name, weight, children = match.groups()
            programs[name] = {
                'weight': int(weight),
                'children': children.split(', ') if children else []
            }
            for child in programs[name]["children"]:
                parents[child] = name
    
    root = None 
    for name in programs:
        if name not in parents:
            root = name
            break
    
    weights = {}
    
    def get_weight(name):
        if name in weights:
            return weights[name]
        weight = 0
        if programs[name]["children"] == []:
            weight = programs[name]["weight"]
        else:
            weight = programs[name]["weight"] + sum(get_weight(child) for child in programs[name]["children"])
        weights[name] = weight
        return weight
        

    while True:
        children = programs[root]["children"]
        children_weights = {child : get_weight(child) for child in children}
        c = Counter()
        for child in children_weights:
            c[children_weights[child]] += 1
        found = False
        for child in children:
            if c[children_weights[child]] == 1:
                root = child
                found = True
                continue
        if not found:
            break
    
    sibling_weights = [get_weight(child) for child in programs[parents[root]]["children"]]
    correct_weight = 0
    for weight in sibling_weights:
        if weight != get_weight(root):
            correct_weight = weight
    ret = programs[root]["weight"] + correct_weight - get_weight(root)
    print(ret)
            
    
    
    
part1()
part2()