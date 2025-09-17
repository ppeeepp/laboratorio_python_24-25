#turtle program vol.2
import turtle


def make_window(bkg_color, title):
  """Crea una finestra con background e titolo e ritorna la nuova finestra"""
  w = turtle.Screen()
  w.bgcolor(bkg_color)
  w.title(title)
  return w


def make_turtle(pen_color, pen_size):
  """Crea una nuova tartaruga dato un colore e dimensione del tratto e ritorna la nuova tartaruga"""
  t = turtle.Turtle()
  t.color(pen_color)
  t.pensize(pen_size)
  return t


#fine turtle program vol.2


# disegno un triangolo
def draw_triangle(turtle_name, steps):
  for i in range(3):
    turtle_name.forward(steps)
    turtle_name.left(120)


# disegno un rettangolo
def draw_rectangle(turtle_name, width, heigth):
  for i in range(2):
    turtle_name.forward(width)
    turtle_name.left(90)
    turtle_name.forward(heigth)
    turtle_name.left(90)

# disegno un quadrato
def draw_square(turtle_name, side):
  draw_rectangle(turtle_name, side, side)

#2. disegno una croce
def draw_cross(turtle_name, steps):
  move(turtle_name, steps/3)
  for i in range(4):
    turtle_name.forward(steps/3)
    turtle_name.left(90)
    turtle_name.forward(steps/3)
    turtle_name.right(90)
    turtle_name.forward(steps/3)
    turtle_name.left(90)


#3. Disegnate su schermo la figura richiesta all’utente tramite la funzione input()
#   permettendo di scegliere tra “triangolo”, “quadrato”, “rettangolo” e “croce”
def draw_figure(turtle_name, steps):
  figure = input("Seleziona la figura da disegnare:\n")
  match figure:
    case "triangolo":
      draw_triangle(turtle_name, steps)
    case "quadrato":
      draw_square(turtle_name, steps)
    case "rettangolo":
      draw_rectangle(turtle_name, steps)
    case "croce":
      draw_cross(turtle_name, steps)
    case _:
      print("Input non valido")

#funzioni per spostare il cursore di tot passi
def move(turtle_name, steps):
  turtle_name.penup()
  turtle_name.forward(steps)
  turtle_name.pendown()

def init(turtle_name, pos_x, pos_y):
  turtle_name.penup()
  turtle_name.goto(pos_x, pos_y)
  turtle_name.pendown()

# 5. Disegnate 5 quadrati concentrici, ognuno 9 passi più grande del precedente.
#    Per farlo utilizzate un loop e la funzione draw_square() che disegna il quadrato
def draw_five_squares(turtle_name, init_size):
  cen_x = 0     #x del centro
  cen_y = 0     #y del centro
  for i in range(5):
    size = init_size + i * 9
    top_x = cen_x - size / 2
    top_y = cen_y + size / 2
    init(turtle_name, top_x, top_y)
    draw_square(turtle_name, size)

#6. Disegnate questa figura.
#   chiedendo all’utente, tramite la funzione input(),
#   la dimensione di partenza e il numero di “lati” da disegnare
def spiral(turtle_name):
  sides = int(input('imposta il numero di lati della spirale:\n'))
  dim = int(input('imposta la dimensione iniziale delle figure:\n'))
  for i in range(sides):
    turtle_name.pencolor('green')
    draw_triangle(turtle_name, dim)
    move(turtle_name, dim*1.5)
    turtle_name.pencolor('violet')
    draw_square(turtle_name, dim)
    move(turtle_name, dim*1.5)
    turtle_name.pencolor('blue')
    draw_cross(turtle_name, dim)
    # mi riposiziono
    turtle_name.right(90)
    move(turtle_name, dim)

    turtle_name.right(90)
    move(turtle_name, dim/3)
    turtle_name.left(90)
    dim = dim*1.5


window = make_window("lightgreen", "Turtle Program")
t = make_turtle('blue', 3)
init(t, 0, 0)
spiral(t)

window.mainloop()
