"""
Title     : XML 1 - Find the Score
Subdomain : XML
Domain    : Python
"""

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):
    total = len(node.attrib.keys())
    for child in node:
        if child:
            total += get_attr_number(child)
        else:
            total += len(child.attrib.keys())
    return total


if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
