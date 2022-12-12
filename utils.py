import json
import random

names = {}
with open('names.json') as f:
    names = json.load(f)

chores = {}
with open('chores.json') as f:
    chores = json.load(f)