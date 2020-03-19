import os
import curses
opciones = ["Agregar Paciente", "Modificar Paciente", "Borrar Paciente","Ver Registro de Paciente ","Exportar","SDFSDF"]
def menu(stdscr):
    attributes = {}
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    attributes['normal'] = curses.color_pair(1)

    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
    attributes['highlighted'] = curses.color_pair(2)

    c = 0  # last character read
    option = 0  # the current option that is marked
    while c != 10:  # Enter in ascii
        stdscr.erase()
        stdscr.addstr("SELECCIONE SU OPCION\n", curses.A_UNDERLINE)
        for i in range(len(opciones)):
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            stdscr.addstr("{0}.-- ".format(i + 1))
            stdscr.addstr(opciones[i] + '\n', attr)
        c = stdscr.getch()
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(opciones) - 1:
            option += 1

    stdscr.addstr("You chose {0}".format(opciones[option]))
    stdscr.getch()

def limpiarPantalla():
    os.system('cls')
