#!/usr/bin/env python3
"""nt"""

def tree(data, initial=True):
    """Format of data is {element:{child_dict},}
    e.g. {"top": {"sub1": {"subsub1": {}}, "sub2": {}}}"""
    ret = []
    for member, child_dict in data.items():
        ret.append(member)
        if child_dict:
            for i, (name, value) in enumerate(child_dict.items()):
                last = i == len(child_dict) - 1
                subtree = tree({name: value}, initial=False)
                for j, line in enumerate(subtree):
                    if j == 0:
                        if last:
                            ret.append(f"└─ {line}")
                        else:
                            ret.append(f"├─ {line}")
                    else:
                        if last:
                            ret.append(f"   {line}")
                        else:
                            ret.append(f"│  {line}")
    if initial:
        ret = "\n".join(ret)
    return ret


def main():
    """main call"""
    print(tree({"top": {"sub1": {"subsub1": {}}, "sub2": {}}}))


if __name__ == "__main__":
    main()
