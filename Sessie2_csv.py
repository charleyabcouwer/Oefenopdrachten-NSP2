Lijst_kracht = [1.2, 1.8, 2.4, 2.7, 3.1] # N
Lijst_afstand = [0.3, 0.4, 0.6, 0.8, 1.0] # m 

# repeat
#   print F, s, W

for F, s in zip(Lijst_kracht, Lijst_afstand):

    kracht = F
    afstand = s
    arbeid = F * s

    print(f"Kracht: {kracht} N, Afstand: {afstand} m, Arbeid:{arbeid} W")
