import pygame

pygame.init()

colors = {
    "red": (255,0,0),
    "white": (200,200,200),
    "black": (0,0,0),
    "gray": (100,100,100)
}

screen = pygame.display.set_mode((550,545))
running = True

pygame.display.set_caption("PyJa Cross", "https://cdn-icons-png.flaticon.com/512/124/124034.png?w=360")
# icon = pygame.image.load("logo.png")
# pygame.display.set_icon(icon)

font = pygame.font.SysFont(None, 50)

squareSide = 60

words = [
    "pygame",
    "joptionpane"
]

hints = [
    "Biblioteca para criar jogos em python.",
    "Pacote para interfaces gráficas em java."
]

blocks = [
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "j", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "o", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "p", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "t", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "i", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "o", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "n", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "p", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": True, "letter": "p", "written": "P" },{ "enabled": True, "letter": "y", "written": "Y" },{ "enabled": True, "letter": "g", "written": "" },{ "enabled": True, "letter": "a", "written": "" },{ "enabled": True, "letter": "m", "written": "" },{ "enabled": True, "letter": "e", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "n", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },],
    [{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": True, "letter": "e", "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },{ "enabled": False, "letter": "" , "written": "" },]
]

def drawSheet(selected):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            if blocks[i][j]["enabled"]:
                # print(i,j)
                if (j,i) == selected:
                    pygame.draw.rect(screen, colors["red"], (j * 50, i * 50, squareSide, squareSide))
                else:
                    pygame.draw.rect(screen, colors["white"], (j * 50, i * 50, squareSide, squareSide))

            else:
                pygame.draw.rect(screen, colors["gray"], (j * 50, i * 50, squareSide, squareSide))

            pygame.draw.rect(screen, colors["black"], (j * 50, i * 50, squareSide, squareSide), 2)

            letter = font.render(blocks[i][j]["written"], True, colors["red"])
            screen.blit(letter, (j * 50 + 167, i * 50 + 117))

def updateGrid(selected):
    drawSheet(selected)
    pygame.display.update()

def updateSelected(selected, direction):
    x,y = selected or (0,0)

    if direction == "down":

        i = y
        while True:
            if i == len(blocks) - 1:
                i = 0
            else:
                i += 1

            if blocks[i][x]["enabled"]:
                y = i
                break

    elif direction == "up":
        i = y
        while True:
            if i == 0:
                i = len(blocks) - 1
            else:
                i -= 1

            if blocks[i][x]["enabled"]:
                y = i
                break

    elif direction == "right":
        i = x
        while True:
            if i == len(blocks[y]) - 1:
                i = 0
            else:
                i += 1

            if blocks[y][i]["enabled"]:
                x = i
                break

    elif direction == "left":
        i = x
        while True:
            if i == 0 :
                i = len(blocks[y]) - 1
            else:
                i -= 1

            if blocks[y][i]["enabled"]:
                x = i
                break

    return (x,y)

selected = (3,0)

while running:

    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        selected = updateSelected(selected, "down")
    if keys[pygame.K_UP]:
        selected = updateSelected(selected, "up")
    if keys[pygame.K_RIGHT]:
        selected = updateSelected(selected, "right")
    if keys[pygame.K_LEFT]:
        selected = updateSelected(selected, "left")

    updateGrid(selected)

pygame.quit()