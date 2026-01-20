# Ett Enkelt Dagligt Arbetsflöde

## Morgonrutin (när du börjar jobba)

### Steg 1: Hämta uppdateringar
```
Först kollar vi om någon annan gjort ändringar:

git pull

Det är som att kolla brevlådan innan du börjar dagen.
```

**Om det står "Already up to date":**
> "Perfekt! Inga nyheter, du har senaste versionen."

**Om det kommer en massa text:**
> "Fint! Nu har du hämtat andras ändringar. Ditt projekt är uppdaterat."

## Under dagen (medan du jobbar)

### Steg 2: Gör dina ändringar
Jobba som vanligt! Skapa filer, ändra kod, experimentera.

### Steg 3: Kolla läget ibland
```
git status

Det här visar vad som hänt sedan senaste sparläget.
Röd text = ändringar som inte är "förberedda" för sparning
Grön text = ändringar som är redo att sparas
```

### Steg 4: Spara regelbundet
Rekommendation: Spara varje gång du gjort något som "fungerar".

```
1. Förbered ändringarna:
   git add .
   (Punkten betyder "allt som ändrats")

2. Skapa sparläget:
   git commit -m "Kort beskrivning av vad du gjorde"
```

**Bra commit-meddelanden:**
- ✅ "Lade till sökfunktion"
- ✅ "Fixade bugg i inloggningen"
- ✅ "Uppdaterade startsidan"

**Mindre bra:**
- ❌ "Ändringar"
- ❌ "asdf"
- ❌ "Fixade grejer"

## Kvällsrutin (när du slutar för dagen)

### Steg 5: Ladda upp till GitHub
```
git push

Nu finns dina sparlägen säkert i molnet!
```

**Varför är detta viktigt?**
- 💻 Om din dator kraschar finns allt på GitHub
- 👥 Kollegor kan se dina ändringar
- 📱 Du kan fortsätta jobba från en annan dator

## Sammanfattning – Daglig Checklista

```
□ Morgon:  git pull          (hämta andras ändringar)
□ Jobb:    gör dina grejer
□ Ofta:    git status        (kolla läget)
□ Ofta:    git add .         (förbered ändringar)
□ Ofta:    git commit -m ""  (spara)
□ Kväll:   git push          (ladda upp)
```

## Tips för GitHub Buddy

Påminn användaren vänligt:

- **Efter en timme utan commit:** "Du har jobbat ett tag! Dags för ett sparläge?"
- **Innan lunch/möte:** "Bra tillfälle att pusha så att allt är säkert!"
- **Om de verkar stressade:** "Ta det lugnt, vi tar ett steg i taget."
