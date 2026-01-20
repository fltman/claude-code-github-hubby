# GitHub Buddy – Komplett Paket för Nybörjare

Ett paket som hjälper nybörjare komma igång med git och GitHub, utan teknisk jargong.

## Vad ingår

```
github-buddy-complete/
├── agents/
│   └── project-starter.md    ← Proaktiv agent för nya projekt
├── skills/
│   └── github-buddy/
│       ├── SKILL.md          ← Huvudkunskap om git/GitHub
│       ├── references/       ← Detaljerade guider
│       └── scripts/          ← Hjälpskript
└── commands/
    └── nytt-projekt.md       ← Slash-command för att starta projekt
```

## Installation i Claude Code

### 1. Kopiera filerna till rätt ställe

```bash
# Agents
cp agents/project-starter.md ~/.claude/agents/

# Skills  
cp -r skills/github-buddy ~/.claude/skills/

# Commands
cp commands/nytt-projekt.md ~/.claude/commands/
```

### 2. Starta om Claude Code

```bash
# Avsluta och starta om, eller kör:
/refresh
```

## Hur det fungerar

### Agenten (Proaktiv)
När användaren säger något som "jag vill bygga en app" kommer agenten automatiskt föreslå att sätta upp versionshantering INNAN de börjar koda.

### Skillen (Kunskap)
När git/GitHub nämns laddas kunskap om hur man förklarar saker på ett enkelt sätt.

### Kommandot (Explicit)
Användaren kan skriva `/nytt-projekt` för att explicit starta en guidad projektsetup.

## Exempel

**Innan (utan paketet):**
```
Användare: jag vill bygga en miniräknare
Claude: Okej! Här är koden... [dumpar kod]
```

**Efter (med paketet):**
```
Användare: jag vill bygga en miniräknare
Claude: Kul! 🧮 Innan vi börjar – vill du ha en "tidsmaskin" 
        för projektet? Med versionshantering kan du alltid 
        gå tillbaka om något går fel...
```

## Anpassa

Redigera filerna för att passa ditt team:
- Ändra språk (översätt till engelska etc.)
- Lägg till företagsspecifika git-workflows
- Anpassa liknelserna
