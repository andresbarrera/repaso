from cachipun import * # cachipun es la función que determina el ganador y lo retorna
def torneo_cachipun(torneo):
    if type(torneo[0][0]) is str and type(torneo[1][0]) is str:
        return ganador_cachipun(torneo)
    if type(torneo[0][0]) is list and type(torneo[1][0]) is str:
        return ganador_cachipun([ganador_cachipun(torneo[0][0]), torneo[1]])
    if type(torneo[0][0]) is str and type(torneo[1][0]) is list:
        return ganador_cachipun([torneo[0], ganador_cachipun(torneo[1][0])])
    if type(torneo[0][0]) is list and type(torneo[1][0]) is list:
        return ganador_cachipun([torneo_cachipun(torneo[0]), torneo_cachipun(torneo[1])])
# Ejemplo de torneo_cachipun : [[["A","t"],["B","p"]],[["C","r"],["D","p"]]]
