"""Updates the versions of all mods in their meta json (see release.py)."""
import os
import subprocess
import sys

META_DIR = os.path.dirname(os.path.abspath(__file__))

# identifier -> directory name in mods/
mods = {
    "3dpings": "3DPings",
    "banghud-raid": "BangHUD-RAID",
    "bernadettas-profile-tools": "Bernadetta Style Profile Tools",
    "betterserverbrowser": "BetterServerBrowser",
    "botshavefeelingsreborn": "BotsHaveFeelingsReborn",
    "bountygrinder": "BountyGrinder",
    "enhancedhitmarkers-raid": "EnhancedHitmarkersRAID",
    "guiiconsexplorer": "GuiIconsExplorer",
    "lootfixer": "LootFixer",
    "outlawintelpeekerreborn": "OutlawIntelPeekerReborn",
    "playerinfo": "PlayerInfo",
    "randommissionhotkey": "RandomMissionHotkey",
    "reloadthenrun-raid": "ReloadThenRunRAID",
    "wolfganghud": "WolfgangHUD",
}

for ident, name in mods.items():
    print("release: " + name)
    subprocess.run([sys.executable, os.path.join(META_DIR, "release.py"), ident, name], check=False)

subprocess.run(["git", "status", "--short"], cwd=META_DIR, check=False)
