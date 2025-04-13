import pygame

pygame.init()

WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canvas Eraser")

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)


CELL_SIZE = 20
cols = WIDTH // CELL_SIZE
rows = HEIGHT // CELL_SIZE

grid = [[BLUE for _ in range(cols)] for _ in range(rows)]

ERASER_SIZE = 20
eraser = pygame.Rect(0, 0, ERASER_SIZE, ERASER_SIZE)


running = True
clock = pygame.time.Clock()

while running:
    screen.fill(GRAY)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.mouse.get_pressed()[0]: 
        mouse_x, mouse_y = pygame.mouse.get_pos()
        eraser.topleft = (mouse_x - ERASER_SIZE // 2, mouse_y - ERASER_SIZE // 2)

        for row in range(rows):
            for col in range(cols):
                cell_rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                if eraser.colliderect(cell_rect):
                    grid[row][col] = WHITE

    for row in range(rows):
        for col in range(cols):
            pygame.draw.rect(screen, grid[row][col], (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, (0, 0, 0), eraser, 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
