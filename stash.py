
while running:

    draw_screen(WIN)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos_x, pos_y = pos

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False



    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        pos_y -= 8
    if keys[pygame.K_DOWN]:
        pos_y += 8
    if keys[pygame.K_LEFT]:
        pos_x -= 8
    if keys[pygame.K_RIGHT]:
        pos_x += 8

    clock.tick(FPS)
    pygame.display.update()
