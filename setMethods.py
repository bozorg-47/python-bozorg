demons = {"douma","muzan","akaza","kokushibo","hantengo","gyutaro","gyokku"}
demonSlayers = {"muzan","tanjiro","kokushibo","yurichi","gyomei","giyu","akaza","inosuke"}
demonslayersCharacter = demonSlayers.intersection(demons)
print(demonslayersCharacter)

charactersofDemonslayer = demons.symmetric_difference(demonSlayers)
print(charactersofDemonslayer)