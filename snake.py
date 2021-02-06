def drawGrid(w,rows,surface):
 pass


def reddrawWindow(surface):
    global rows, width
    win.fill((0,0,0))
    drawGrid(width, rows, surface)
    pygame.display.update()



def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0),(10,10))
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.dely(50) # we control the time - the snake is not moving too fast, as a result it can move
        clock.tick(10) # that is the speed
        reddrawWindow(win)