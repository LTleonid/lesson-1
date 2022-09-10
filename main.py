def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

enemy = 0
e5: game.LedSprite = None
er5 = 0
e4: game.LedSprite = None
er4 = 0
e3: game.LedSprite = None
er3 = 0
e2: game.LedSprite = None
er2 = 0
e1: game.LedSprite = None
er1 = 0
player: game.LedSprite = None
game.set_score(0)
player = game.create_sprite(2, 5)

def on_forever():
    basic.pause(500)
    if er1 == 1:
        e1.change(LedSpriteProperty.Y, 1)
        if e1.get(LedSpriteProperty.Y) == 4:
            e1.delete()
            game.game_over()
    if er2 == 1:
        e2.change(LedSpriteProperty.Y, 1)
        if e2.get(LedSpriteProperty.Y) == 4:
            e2.delete()
            game.game_over()
    if er3 == 1:
        e3.change(LedSpriteProperty.Y, 1)
        if e3.get(LedSpriteProperty.Y) == 4:
            e3.delete()
            game.game_over()
    if er4 == 1:
        e4.change(LedSpriteProperty.Y, 1)
        if e4.get(LedSpriteProperty.Y) == 4:
            e4.delete()
            game.game_over()
    if er5 == 1:
        e5.change(LedSpriteProperty.Y, 1)
        if e5.get(LedSpriteProperty.Y) == 4:
            e5.delete()
            game.game_over()
basic.forever(on_forever)

def on_forever2():
    global enemy, e1, er1, e2, er2, e3, er3, e4, er4, e5, er5
    basic.pause(1000)
    enemy = randint(0, 4)
    if enemy == 0:
        e1 = game.create_sprite(enemy, 0)
        er1 = 1
    if enemy == 1:
        e2 = game.create_sprite(enemy, 0)
        er2 = 1
    if enemy == 2:
        e3 = game.create_sprite(enemy, 0)
        er3 = 1
    if enemy == 3:
        e4 = game.create_sprite(enemy, 0)
        er4 = 1
    if enemy == 4:
        e5 = game.create_sprite(enemy, 0)
        er5 = 1
    basic.pause(500)
basic.forever(on_forever2)
