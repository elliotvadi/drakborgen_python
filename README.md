# drakborgen_python
Skolprojekt.
Ett skolprojekt är att skapa ett textbaserat rollspel. 
Jag tänker delvis eller helt basera detta textbaserade 
rollspel på den moderna brädpelsklassikern 'Drakborgen' 
eftersom det är strukturerat på så sätt att spelet är spelledare. 
Spelets många regler innebär även att spelet har en dynamisk och 
engagerande karaktär, vilket bör passa väldigt bra för ett datorspel. 
Spelet har många slumpade element, vilket gör spelvärlden mer levande. 

Om allting skiter sig så kommer jag att fokusera på att försöka göra en variant av 'Drakskatten' istället.


# Uppdatering 08/12/2021
Jag har kommit fram till att projektet kommer att vara löst baserat på Drakskatten och Drakborgen. Detta beror i grund och botten 
på att jag ej har tillgång till många av Drakborgens komponenter, vilket innebär att jag inte helt kan basera mitt spel på det. Därför tänker jag
istället löst basera mitt spel på både Drakborgen och Drakskatten. Jag tänker basera en del av händelseförloppet och vissa funktioner på Drakborgen,
men övriga funktioner (i synnerhet rum och fiender) kommer att baseras på Drakborgen. 

Jag funderar i nuläget på att ha en linjär "karta" som spelet utspelar sig på, men där rum och övriga utrymmen kommer att slumpas. Rummens innehåll samt
händelser i rummen kommer jag förmodligen hämta från Drakborgen, medans örviga detaljer så som rummens funktion sannolikt kommer hämtas från Drakskatten.

Alternativet till en linjär "karta" skulle vara att man även kan gå åt olika riktningar, så som höger och vänster, men att riktning (om valbart)
väljs av spelaren eller datorn. Detta skulle göra spelet mer levande. Detta kräver dock emellertid att man använder sig av någon form av koordinatsystem
för att hålla koll på var spelaren är, och för att se till att "kartan" håller sig innanför "spelplanen", samt så att man inte fastnar.


# Uppdatering 09/12/2021 
Följande element kommer att hämtas från Drakborgen (Preliminärt): 
* Fällkort
* Kistor med tillhörande kort
* Stupad krigare med tillhörande kort
* Draken och skattkammaren
* Rumsletning (med lönndörr, som leder till annat rum)
* Flaskor
* Monster
* Stridssystemet
* Magiska ringar (möjligen även magiska amuletter)
* Jättespindel (Kanske)
* Dörrar med tillhörande dörrfällor (Kanske)
* Spelkaraktärer, med tillhörande färdigheter
* Guldföremål
* 22 rundor totalt
* Facklan slocknar (Kanske)
* Totalt sett 10 rum
* Övriga spelregler


# Uppdatering 21/12/2021
Jag har nu beslutat mig för att inte längre ha en helt slumpad spelplan. Detta beror på att det tycks bli väldigt svårt att programmera en helt slumpad plan, om man inte vill göra saker och ting alltför komplicerade. Jag har därför valt att ha en bestämt layout, men där rummen i sig är slumpade. Jag funderar även på att i alla fall preliminärt skära ner på antalet spelbara karaktärer för att underlätta för testning av spelet. 
