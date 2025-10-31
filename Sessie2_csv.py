import csv


# In deze subopgave maak ik van python code een csv bestand.

Lijst_kracht = [1.2, 1.8, 2.4, 2.7, 3.1]  
Lijst_afstand = [0.3, 0.4, 0.6, 0.8, 1.0]  

# CSV-bestand aanmaken en vullen
with open('arbeid_metingen.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Kracht (N)", "Afstand (m)", "Arbeid (J)"])  # kolomkoppen

    for F, s in zip(Lijst_kracht, Lijst_afstand):
        arbeid = F * s
        print(f"Kracht: {F} N, Afstand: {s} m, Arbeid: {arbeid:} J")
        writer.writerow([F, s, arbeid])

print("CSV-bestand 'arbeid_metingen.csv' aangemaakt, zie bestanden.")
