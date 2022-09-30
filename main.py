def on_button_pressed_a():
    player.move(-1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global laser, laserr
    laser = game.create_sprite(player.get(LedSpriteProperty.X), 2)
    laserr = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    player.move(1)
input.on_button_pressed(Button.B, on_button_pressed_b)

er5 = 0
er4 = 0
er3 = 0
er2 = 0
er1 = 0
enemy = 0
e5: game.LedSprite = None
e4: game.LedSprite = None
e3: game.LedSprite = None
e2: game.LedSprite = None
e1: game.LedSprite = None
laser: game.LedSprite = None
laserr = 0
player: game.LedSprite = None
game.set_score(0)
player = game.create_sprite(2, 5)
laserr = 0

def on_forever():
    basic.pause(100)
    if laserr == 1:
        basic.pause(200)
        laser.change(LedSpriteProperty.Y, 1)
    if laser.is_touching(e1):
        e1.delete()
        laser.delete()
        game.add_score(10)
    elif laser.is_touching(e2):
        e1.delete()
        laser.delete()
        game.add_score(10)
    elif laser.is_touching(e3):
        e1.delete()
        laser.delete()
        game.add_score(10)
    elif laser.is_touching(e4):
        e1.delete()
        laser.delete()
        game.add_score(10)
    elif laser.is_touching(e5):
        e1.delete()
        laser.delete()
        game.add_score(10)
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

def on_forever3():
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
basic.forever(on_forever3)
