n=int(input())
aux=0
dic={"Tetrahedron":4,
    "Cube":6,
    "Octahedron":8,
    "Dodecahedron":12,
    "Icosahedron":20 }
for i in range(n):
    s=input()
    aux+=dic[s]
print(aux)
