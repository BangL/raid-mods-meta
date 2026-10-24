"""Writes the version of a mod (from its supermod.xml) into its meta json.

usage: release.py <identifier> <mod dir name>
"""
import json
import os
import sys
import re

META_DIR = os.path.dirname(os.path.abspath(__file__))
MODS_DIR = os.path.join(META_DIR, "..", "mods")

if len(sys.argv) != 3:
    print("usage: " + sys.argv[0] + " <identifier> <name>")
    sys.exit(1)

json_file = os.path.join(META_DIR, sys.argv[1] + ".json")
mod_file = os.path.join(MODS_DIR, sys.argv[2], "supermod.xml")

with open(json_file, "r") as f:
    data = json.load(f)
old_version = data[0].get("version")

# a regex instead of an XML parser: the game's parser is more lenient than a strict one
with open(mod_file, "r", encoding="utf-8") as f:
    mod_tag = re.search(r"<mod\b[^>]*>", f.read())
version_match = mod_tag and re.search(r'\bversion="([^"]*)"', mod_tag.group(0))
new_version = version_match and version_match.group(1)
if not new_version:
    print("no version in " + mod_file)
    sys.exit(1)

print("old version: " + str(old_version))
print("new version: " + new_version)
data[0]["version"] = new_version

with open(json_file, "w") as f:
    json.dump(data, f)
