# Vanliga Problem – Och Hur Du Löser Dem

## 🔴 "error: Your local changes would be overwritten"

**Vad det betyder på svenska:**
> "Du har ändringar som inte är sparade. Om jag hämtar nya filer nu kan de försvinna!"

**Lösning:**
```
1. Spara dina ändringar först:
   git add .
   git commit -m "Mina ändringar"

2. Sen kan du hämta uppdateringar:
   git pull
```

**Förklaring för användaren:**
> "Git vill skydda ditt arbete. Tänk på det som att git säger: 'Vänta! Du har osparade anteckningar på skrivbordet. Låt mig inte råka sopa bort dem.'"

---

## 🔴 "CONFLICT: Merge conflict in [filnamn]"

**Vad det betyder på svenska:**
> "Du och någon annan har ändrat samma rad. Git vet inte vems version som gäller."

**Så här ser en konflikt ut i filen:**
```
<<<<<<< HEAD
Din version av texten
=======
Den andra personens version
>>>>>>> branch-namn
```

**Lösning steg för steg:**

1. **Öppna filen** som har konflikten
2. **Hitta markeringarna** (`<<<<<<<`, `=======`, `>>>>>>>`)
3. **Välj vilken version du vill ha** (eller kombinera dem)
4. **Ta bort markeringarna** (allt med `<`, `=`, `>`)
5. **Spara och commita:**
   ```
   git add .
   git commit -m "Löste konflikt i [filnamn]"
   ```

**Förklaring för användaren:**
> "Tänk dig att du och en kollega båda redigerat samma stycke i ett dokument. Nu får ni sitta ner tillsammans och bestämma vad som ska stå där. Det är allt en 'konflikt' är!"

---

## 🔴 "fatal: not a git repository"

**Vad det betyder på svenska:**
> "Den här mappen är inte kopplad till git."

**Lösning A – Om du vill starta git här:**
```
git init
```

**Lösning B – Om du är i fel mapp:**
```
Gå till rätt mapp med: cd rätt-mapp-namn
```

**Förklaring för användaren:**
> "Git-kommandon fungerar bara i mappar som 'känner till' git. Antingen behöver vi aktivera git här, eller så har du hamnat i fel mapp."

---

## 🔴 "Updates were rejected because the tip of your current branch is behind"

**Vad det betyder på svenska:**
> "Någon annan har lagt till saker på GitHub som du inte har på din dator."

**Lösning:**
```
1. Hämta ändringarna:
   git pull

2. Sen kan du ladda upp dina:
   git push
```

**Förklaring för användaren:**
> "Det är som att försöka lägga in sida 5 i en pärm där någon redan lagt in en ny sida 5. Du måste först se vad de lagt in, sen kan du lägga till ditt."

---

## 🔴 "Please enter a commit message"

**Vad som händer:**
Du hamnar i en konstig texteditor (oftast Vim) och vet inte hur du tar dig ut.

**Snabb lösning – Ta dig ut:**
```
Tryck: Esc
Skriv: :wq
Tryck: Enter
```

**Bättre lösning – Undvik det helt:**
Skriv alltid meddelandet direkt:
```
git commit -m "Ditt meddelande här"
           ↑
           Glöm inte citattecknen!
```

**Förklaring för användaren:**
> "Du hamnade i en gammal texteditor. Den är lite som att köra bil med manuell växellåda – kraftfull men förvirrande om man inte lärt sig. Vi tar den enkla vägen istället!"

---

## 🔴 "Permission denied (publickey)"

**Vad det betyder på svenska:**
> "GitHub känner inte igen din dator."

**Förklaring för användaren:**
> "Det är som att försöka komma in i en lägenhet utan nyckel. Vi behöver skapa en 'digital nyckel' och ge den till GitHub."

**Lösning – Byt till HTTPS istället för SSH:**
```
Det enklaste är att använda HTTPS-länken istället.
Gå till GitHub, klicka på 'Code', välj 'HTTPS', och kopiera länken.
```

---

## 🟡 "Jag committade till fel branch!"

**Ingen panik! Vi kan flytta committen:**

```
1. Skapa en ny branch från där du är:
   git branch rätt-branch-namn

2. Ta bort committen från fel branch (men behåll ändringarna):
   git reset HEAD~1

3. Byt till rätt branch:
   git checkout rätt-branch-namn

4. Commita där istället:
   git add .
   git commit -m "Ditt meddelande"
```

---

## 🟡 "Jag vill ångra min senaste commit"

**Om du INTE har pushat ännu:**
```
git reset HEAD~1

Dina ändringar finns kvar i filerna, men committen är borta.
Du kan göra en ny commit när du är redo.
```

**Om du redan HAR pushat:**
> "Då är det lite knepigare. Vi bör prata igenom det först så vi inte skapar problem för andra som jobbar i projektet."

---

## Tips för GitHub Buddy

**Allmänt förhållningssätt vid fel:**
1. 🧘 "Lugnt, det här löser vi"
2. 📖 Förklara vad felet betyder på vanlig svenska
3. ✅ Ge en tydlig lösning
4. 💡 Förklara hur man undviker det nästa gång

**Fråga alltid:**
> "Har du redan pushat till GitHub, eller finns ändringarna bara på din dator?"

Det påverkar vilken lösning som är bäst!
