import math

tel_cislo = (input("Na jaké číslo chcete odeslat zprávu?")).replace(" ", "")
CENA = 3

def zadejTel(tel: str) -> bool:
  if len(tel) == 9:
    return True
  elif len(tel) == 13 and tel[:4] == "+420":
    return True
  else: 
    return False

def cenaZpravy(text: str) -> int: 
  cena = math.ceil(len(text) / 180) * CENA
  return cena
  
if zadejTel(tel_cislo):
  text_zpravy = input("Jaký je text zprávy, který chcete poslat?")
  if len(text_zpravy) > 0:
    print(f"Cena odeslané zprávy bude {cenaZpravy(text_zpravy)} Kč.")
  else:
    print("Nezadal/a jste žádný text.")
else: 
  print("Zadané číslo není v požadovaném formátu.")
  
