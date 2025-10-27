#!/usr/bin/env python3
import random
import re

def toxify(code):
    variables = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', code)
    for var in set(variables):
        code = code.replace(var, random.choice(["toxibunny", "pixelheart", "sarah_wuz_here", "chaos_gremlin"]))
    return code

if __name__ == "__main__":
    print("💖 *You’ve been toxified!* 💖")
    print(toxify("int main = 0; // this used to be serious code"))