# coding: utf-8
"""
Dans ce script sont contenues les fonctions relatives
au calcul du voisinage des cellules.
"""
def neighbours(space, row, col):
  # On détermine les limites du "plateau"
  max_border_row = len(space) - 1
  max_border_col = len(space[0]) - 1
  
  # On définit la fonction pour détecter le voisinage d'une cellule
  # Il est tout à fait autorisé de créer une fonction
  # dans une fonction. Notons que si la fonction interne a
  # accès aux variables max_border_row et max_border_col de
  # la fonction parente, les variables accessibles/définies dans neighbour
  # sont pour leur part inaccessibles en-dehors de neighbour.
  
  def neighbour(row, col):
    if row == -1:
      row = max_border_row
    # elif = else if en Python
    elif row > max_border_row:
      row = 0
    
    if col == -1:
      col = max_border_col
    elif col > max_border_col:
      col = 0
    return space[row][col]

  neighbourhood = neighbour(row, col-1) + neighbour(row-1, col-1)
  neighbourhood += neighbour(row-1, col) + neighbour(row-1, col+1)
  neighbourhood += neighbour(row, col+1) + neighbour(row+1, col+1)
  neighbourhood += neighbour(row+1, col) + neighbour(row+1, col-1)
  return neighbourhood
