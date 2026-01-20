#!/usr/bin/env python3
"""
friendly_status.py - Ger en nybörjarvänlig översikt av git-status

Användning: python3 friendly_status.py [sökväg-till-repo]

Skriptet analyserar git-status och presenterar det på ett enkelt sätt
med emojis och förklaringar istället för teknisk jargong.
"""

import subprocess
import sys
import os


def run_git(cmd, cwd=None):
    """Kör ett git-kommando och returnera output."""
    try:
        result = subprocess.run(
            ["git"] + cmd,
            capture_output=True,
            text=True,
            cwd=cwd
        )
        return result.stdout.strip(), result.stderr.strip(), result.returncode
    except FileNotFoundError:
        return "", "Git är inte installerat", 1


def get_friendly_status(repo_path="."):
    """Generera en nybörjarvänlig statusrapport."""
    
    # Kolla om det är ett git-repo
    stdout, stderr, code = run_git(["rev-parse", "--git-dir"], repo_path)
    if code != 0:
        return {
            "is_repo": False,
            "message": "📁 Den här mappen är inte ett git-projekt ännu."
        }
    
    report = {
        "is_repo": True,
        "branch": "",
        "staged": [],
        "modified": [],
        "untracked": [],
        "ahead": 0,
        "behind": 0,
        "clean": True
    }
    
    # Vilken branch?
    stdout, _, _ = run_git(["branch", "--show-current"], repo_path)
    report["branch"] = stdout or "ingen branch"
    
    # Status på filer
    stdout, _, _ = run_git(["status", "--porcelain"], repo_path)
    if stdout:
        report["clean"] = False
        for line in stdout.split("\n"):
            if not line:
                continue
            status = line[:2]
            filename = line[3:]
            
            if status[0] in "MADRCT":
                report["staged"].append(filename)
            if status[1] in "MD":
                report["modified"].append(filename)
            if status == "??":
                report["untracked"].append(filename)
    
    # Ahead/behind remote
    stdout, _, code = run_git(["rev-list", "--count", "--left-right", "@{upstream}...HEAD"], repo_path)
    if code == 0 and stdout:
        parts = stdout.split("\t")
        if len(parts) == 2:
            report["behind"] = int(parts[0])
            report["ahead"] = int(parts[1])
    
    return report


def format_report(report):
    """Formatera rapporten till läsbar text."""
    
    if not report["is_repo"]:
        return report["message"]
    
    lines = []
    lines.append("=" * 50)
    lines.append("📊 LÄGESRAPPORT FÖR DITT PROJEKT")
    lines.append("=" * 50)
    lines.append("")
    
    # Branch
    lines.append(f"🌿 Du jobbar i: {report['branch']}")
    lines.append("")
    
    # Status
    if report["clean"]:
        lines.append("✨ Allt är sparat och i ordning!")
    else:
        if report["staged"]:
            lines.append(f"📦 Redo att sparas ({len(report['staged'])} filer):")
            for f in report["staged"][:5]:
                lines.append(f"   • {f}")
            if len(report["staged"]) > 5:
                lines.append(f"   ... och {len(report['staged']) - 5} till")
            lines.append("")
        
        if report["modified"]:
            lines.append(f"✏️  Ändrade (ej förberedda) ({len(report['modified'])} filer):")
            for f in report["modified"][:5]:
                lines.append(f"   • {f}")
            if len(report["modified"]) > 5:
                lines.append(f"   ... och {len(report['modified']) - 5} till")
            lines.append("")
        
        if report["untracked"]:
            lines.append(f"🆕 Nya filer (git känner inte till dem) ({len(report['untracked'])} filer):")
            for f in report["untracked"][:5]:
                lines.append(f"   • {f}")
            if len(report["untracked"]) > 5:
                lines.append(f"   ... och {len(report['untracked']) - 5} till")
            lines.append("")
    
    # Sync status
    if report["ahead"] > 0:
        lines.append(f"⬆️  Du har {report['ahead']} sparläge(n) som inte laddats upp till GitHub")
        lines.append("   Tips: Kör 'git push' för att ladda upp dem")
        lines.append("")
    
    if report["behind"] > 0:
        lines.append(f"⬇️  Det finns {report['behind']} uppdatering(ar) på GitHub som du inte hämtat")
        lines.append("   Tips: Kör 'git pull' för att hämta dem")
        lines.append("")
    
    if report["ahead"] == 0 and report["behind"] == 0 and report["clean"]:
        lines.append("☁️  Synkad med GitHub – allt stämmer överens!")
    
    lines.append("")
    lines.append("=" * 50)
    
    # Förslag baserat på status
    lines.append("💡 FÖRSLAG:")
    
    if report["modified"] or report["untracked"]:
        lines.append("   → Du har ändringar. Vill du spara dem?")
        lines.append("     Kör: git add .  (förbered allt)")
        lines.append("     Sen: git commit -m \"beskrivning\"")
    elif report["staged"]:
        lines.append("   → Du har förberett ändringar. Dags att spara!")
        lines.append("     Kör: git commit -m \"beskrivning\"")
    elif report["ahead"] > 0:
        lines.append("   → Dina sparlägen finns bara lokalt. Ladda upp dem!")
        lines.append("     Kör: git push")
    elif report["behind"] > 0:
        lines.append("   → Hämta de senaste ändringarna först!")
        lines.append("     Kör: git pull")
    else:
        lines.append("   → Allt ser bra ut! Fortsätt jobba. 🎉")
    
    lines.append("=" * 50)
    
    return "\n".join(lines)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "."
    report = get_friendly_status(path)
    print(format_report(report))
