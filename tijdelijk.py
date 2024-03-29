from helper import decoreer

def print_aanbieding():
  prijzen = {
    "aardbei": 3,
    "vanille": 4,
    "chocolade": 5
  }

  # Gebruik de sleutel "aardbei" om de prijs op te halen
  aanbieding = prijzen["aardbei"] * 0.8

  # Formateer de reclametekst met de berekende aanbiedingsprijs
  reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts €{aanbieding}"

  # Verwijder 0 tot 2 decimalen achter de komma
  reclame_tekst2 = reclame_tekst[:-14]

  # Capitalize
  reclame_tekst3 = reclame_tekst2.upper()

  # List 
  reclame_tekst4 = reclame_tekst3.split()

  # For loop
  for el in reclame_tekst4:      
    if len(el) > 4:
      print(el.upper())

    else:
      print(el.lower())

decoreer("Aanbieidng")

print_aanbieding()



  