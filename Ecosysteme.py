
#Configuration initiale 
GRID_SIZE=30
INITIAL_SHEEP=50
INITIAL_WOLVES=10
INITIAL_GRASS_COVERAGE=0.3 #30% de la grille

#Energie 
SHEEP_INITIAL_ENERGY=20
WOLF_INITIAL_ENERGY=40
SHEEP_ENERGY_FROM_GRASS=15
# WOLF_ENERGY_


class mouton :
    """
    Stocker ses cordonnées, son niveau d'énergie, son age

    se deplace aléatoirement

    se reproduit seul

    """