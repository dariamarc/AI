from repo.Edge import Edge
from repo.Reader import Reader
from service.ACO import ACO


def main():
    reader = Reader("hardE.txt")
    net = reader.readNetwork()

    '''
    Parametrii problemei:
    noNodes - numarul de noduri din graf
    mat - matricea de adiacenta
    phMat - matricea feromonilor
    pheromone - cantitatea de feromon lasata de catre o furnica
    q0 - parametrul folosit pentru alegerea unui oras
    alpha, beta - parametrii din formula
    phEvap - rata de evaporare a feromonului (folosita la final, intre 2 iteratii, cand cea mai buna furnica traverseaza
             inca o data pentru a intari feromonul
    phDecay - coeficientul de degradare a feromonului (folosit in update-urile locale)
    '''
    phMat = [[0.5 for i in range(net['noNodes'])] for j in range(net['noNodes'])]

    problParams = {'noNodes': net['noNodes'], 'mat' : net['mat'], 'phMat' : phMat, 'pheromone': 0.5, 'q0' : 0.9, 'alpha' : 1, 'beta' : 3, 'phEvap' : 0.1, 'phDecay' : 0.1}

    params = {'colonySize' : 30, 'noSteps' : 300}

    aco = ACO(problParams, params)


    print("1 - graf normal")
    print("2 - graf dinamic")
    x = int(input())
    if x == 1:
        aco.aco()
    else:
        aco.aco_dynamic()




main()