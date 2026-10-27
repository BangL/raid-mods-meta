"""Updates the versions of all mods in their meta json (see release.py)."""
import os
import subprocess
import sys

META_DIR = os.path.dirname(os.path.abspath(__file__))

# identifier -> directory name in mods/
mods = {
    "3dpings": "3DPings",
    "assaultinforaid": "AssaultInfoRAID",
    "banghud-raid": "BangHUD-RAID",
    "bangls-skinpack": "BangL's SkinPack (SkinLib)",
    "bernadettas-profile-tools": "Bernadetta Style Profile Tools",
    "betterserverbrowser": "BetterServerBrowser",
    "botshavefeelingsreborn": "BotsHaveFeelingsReborn",
    "bountyhunter": "BountyHunter",
    "bountygrinder": "BountyGrinder",
    "crowbarmelee": "CrowbarMelee",
    "devtools-raid": "DevTools-RAID",
    "enhancedhitmarkers-raid": "EnhancedHitmarkersRAID",
    "extraachievs": "ExtraAchievs",
    "fieldrepairs": "Field Repairs",
    "extraraidinfo": "ExtraRaidInfo",
    "guiiconsexplorer": "GuiIconsExplorer",
    "hitlersynced": "HitlerSynced",
    "iter-raid": "Iter",
    "lootfixer": "LootFixer",
    "outlawintelpeekerreborn": "OutlawIntelPeekerReborn",
    "playerinfo": "PlayerInfo",
    "randommissionhotkey": "RandomMissionHotkey",
    "readyuplockfix": "ReadyUpLockFix",
    "reloadthenrun-raid": "ReloadThenRunRAID",
    "statsscreen": "StatsScreen",
    "thirdperson": "ThirdPerson",
    "wolfganghud": "WolfgangHUD",
    "savegamedumper": "SaveGameDumper",
    "luadebugapi": "LuaDebugAPI",
    "wolfganghud-devtools": "WolfgangHUD-DevTools",
}

for ident, name in mods.items():
    print("release: " + name)
    subprocess.run([sys.executable, os.path.join(META_DIR, "release.py"), ident, name], check=False)

subprocess.run(["git", "status", "--short"], cwd=META_DIR, check=False)
