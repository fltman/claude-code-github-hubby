# Branches – Din Experimentverkstad

## Vad är en branch?

Tänk dig att du målar en tavla. En branch är som att ta ett foto av tavlan och sedan fortsätta måla på en kopia. Om det blir fint kan du använda det. Om det blir fult slänger du kopian och originalet är orört.

## Varför använda branches?

**Utan branch:**
```
Du ändrar direkt i projektet → Något går fel → Panik! 😰
```

**Med branch:**
```
Du skapar en kopia → Experimenterar fritt → 
  → Blev bra? Slå ihop med originalet! 🎉
  → Blev dåligt? Släng kopian, originalet är kvar 😌
```

## När bör jag föreslå en branch?

Som GitHub Buddy, föreslå en branch när användaren ska:

- ✨ Lägga till en ny funktion
- 🔧 Fixa ett problem (bugg)
- 🎨 Ändra designen
- 🧪 Testa något de är osäkra på
- 👥 Jobba på något medan andra jobbar på annat

## Hur förklarar jag det?

### Skapa en branch
```
Jag skapar nu en egen arbetsyta åt dig:

git checkout -b ny-funktion
↑             ↑
|             └── Vad vi kallar arbetsytan
└── "Skapa och gå till"

Nu är du i din egen bubbla. Allt du gör här påverkar 
inte huvudprojektet förrän du väljer att slå ihop dem.
```

### Byta mellan branches
```
För att hoppa tillbaka till huvudprojektet:

git checkout main
            ↑
            └── Namnet på huvudgrenen (brukar heta 'main' eller 'master')

Dina experiment finns kvar i den andra branchen och väntar på dig!
```

### Slå ihop (merge)
```
Nu ska vi ta in dina ändringar i huvudprojektet:

1. Först går vi till huvudprojektet:
   git checkout main

2. Sen hämtar vi in ändringarna:
   git merge ny-funktion
             ↑
             └── Namnet på din experimentbranch

Klart! Nu finns dina ändringar i huvudprojektet. 🎉
```

## Vanliga frågor

**"Försvinner min branch efteråt?"**
> Nej, den finns kvar! Du kan radera den om du vill, eller spara den som referens.

**"Kan jag ha flera branches samtidigt?"**
> Absolut! Tänk dig att du har flera utkast till samma uppsats. Du kan hoppa mellan dem och välja det bästa.

**"Vad händer om jag glömmer vilken branch jag är i?"**
> Kör `git branch` så ser du alla branches. Den du är i har en stjärna (*) framför sig.
