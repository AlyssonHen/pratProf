import math
print('teste script')


def hipot(triangulo):
    cA = triangulo['catetoA']
    cO = triangulo['catetoO']
    hipot = (cA * cA) + (cO * cO)
    hipot = math.sqrt(hipot)
    hipot = round(hipot, 2)
    return hipot

medidas = {
    'catetoA': 10,
    'catetoO': 32
}

print(hipot(medidas))