# coding: utf-8
"""
# Les fonctions ci-dessous ont vocation à dessiner l'interface du jeu.
"""
import curses
import neighbourhood


def init_curses(width=20, height=20, pos=(0, 0)):
  curses.initscr()
  curses.noecho()
  curses.cbreak()
  curses.curs_set(0)
  
  window = curses.newwin(width+2, height+2, pos[0], pos[1])
  window.border(0)
  window.keypad(1)
  return window


def close_curses():
  curses.echo()
  curses.nocbreak()
  curses.curs_set(1)
  curses.endwin()
  

def initialize(config=None, width=20, height=20):
  space = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(0)
    space.append(row)
  
  for i, j in config:
    space[i][j] = 1
  return space


def display(space, win):
  # L'énumération permet de sortir un indice (nline) et un item (line) de space
  for nline, line in enumerate(space):
    for ncell, cell in enumerate(line):
      if cell == 0:
        win.addstr(nline+1, ncell+1, ".") # Cellule morte
      else:
        win.addstr(nline+1, ncell+1, "*") # Cellule vivante


def transition(space, width=20, height=20):
  # On prépare un espace vierge pour la mise à jour du plateau
  space_next = []
  for i in range(height):
    row = []
    for j in range(width):
      row.append(0)
    space_next.append(row)
    
  for row in range(height):
    for col in range(width):
      n = neighbourhood.neighbours(space, row, col)
      # Si une cellule est morte et a 3 voisins, une cellule naît
      if space[row][col] == 0 and n == 3:
        space_next[row][col] = 1
      # Si une cellule est vivante et a 2 à 3 voisins, elle reste en vie
      elif space[row][col] == 1 and (n == 2 or n == 3):
        space_next[row][col] = 1
    # Toutes les autres cellules meurent/restent mortes
  return space_next

if __name__ == "__main__":
  # Configuration de base en U. Vous pouvez changer le point de départ ici !
  u = (
    (8, 8),
    (8, 10),
    (9, 8),
    (9, 10),
    (10, 8),
    (10, 9),
    (10, 10))
    
  # Initialisation de la fenêtre
  win = init_curses()
  space = initialize(u)
  while True:
    display(space, win)
    # Il faut appuyer sur la barre espace pour faire les transitions
    key = win.getch()
    if key == 27:
      break
    space = transition(space)
  close_curses()
