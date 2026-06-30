# GitHub Buddy

[![Support me on Patreon](https://img.shields.io/badge/Patreon-Support%20my%20work-FF424D?style=flat&logo=patreon&logoColor=white)](https://www.patreon.com/AndersBjarby)

Ett Claude Code-paket som hjälper nybörjare komma igång med git och GitHub utan teknisk jargong. Claude blir proaktiv: föreslår versionshantering innan man börjar koda, förklarar git-begrepp med vardagliga liknelser ("tidsmaskin" istället för repository) och håller lugnet när fel uppstår.

## Vad ingår

- **Agent** (`agents/project-starter.md`) – föreslår automatiskt att sätta upp versionshantering när användaren vill bygga något nytt
- **Skill** (`skills/github-buddy/`) – kunskap om hur man förklarar git/GitHub enkelt, med referensguider (vanliga problem, branches för nybörjare, dagligt arbetsflöde) och ett `friendly_status.py`-hjälpskript
- **Kommando** (`commands/nytt-projekt.md`) – slash-command `/nytt-projekt` för att starta en guidad projektsetup
- **CLAUDE.md** – projektinstruktioner som gör Claude proaktiv med commits, branches och begripliga felförklaringar

## Installation

Kopiera filerna till din Claude Code-konfiguration och starta om:

```bash
# Agents
cp agents/project-starter.md ~/.claude/agents/

# Skills
cp -r skills/github-buddy ~/.claude/skills/

# Commands
cp commands/nytt-projekt.md ~/.claude/commands/
```

Starta sedan om Claude Code (eller kör `/refresh`). För att göra Claude proaktiv i ett enskilt projekt kan du även lägga `CLAUDE.md` i projektroten, eller i `~/.claude/CLAUDE.md` för alla projekt.

## Teknik

Claude Code (agent, skill, slash-command och CLAUDE.md i Markdown) plus ett litet Python-hjälpskript. Innehållet är på svenska och kan anpassas till andra språk eller team-specifika arbetsflöden.
