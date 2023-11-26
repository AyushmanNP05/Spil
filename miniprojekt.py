
def make_random_map(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    # Make everything grass initially
    for i in range(rows):
        for j in range(rows):
            grid[i][j].is_passable()

    # Add water randomly
    for _ in range(900):  # Adjust the number of water tiles as needed
        i, j = random.randint(0, rows - 1), random.randint(0, rows - 1)
        grid[i][j].is_impassable()

    return grid

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(BLACK)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

def main(win, width):
    ROWS = 50
    grid = make_random_map(ROWS, width)

    # Set random start and end points
    start_row, start_col = random.randint(0, ROWS - 1), random.randint(0, ROWS - 1)
    end_row, end_col = random.randint(0, ROWS - 1), random.randint(0, ROWS - 1)

    start = grid[start_row][start_col]
    end = grid[end_row][end_col]

    start.make_passable()
    end.make_passable()

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_random_map(ROWS, width)

                    start_row, start_col = random.randint(0, ROWS - 1), random.randint(0, ROWS - 1)
                    end_row, end_col = random.randint(0, ROWS - 1), random.randint(0, ROWS - 1)

                    start = grid[start_row][start_col]
                    end = grid[end_row][end_col]

                    start.make_passable()
                    end.make_passable()

    pygame.quit()

# Call the main function
main(WIN, WIDTH)
