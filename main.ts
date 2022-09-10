input.onButtonPressed(Button.A, function () {
    player.move(-1)
})
input.onButtonPressed(Button.AB, function () {
    if (1 == shoot) {
        if (0 == player.get(LedSpriteProperty.X)) {
            basic.showLeds(`
                # . . . .
                # . . . .
                # . . . .
                # . . . .
                # . . . .
                `)
            basic.pause(500)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
                `)
            a1 = 0
        }
        if (1 == player.get(LedSpriteProperty.X)) {
            basic.showLeds(`
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                . # . . .
                `)
            basic.pause(500)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . # . . .
                `)
            a2 = 0
        }
        if (2 == player.get(LedSpriteProperty.X)) {
            basic.showLeds(`
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                . . # . .
                `)
            basic.pause(500)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
                `)
            a3 = 0
        }
        if (3 == player.get(LedSpriteProperty.X)) {
            basic.showLeds(`
                . . . # .
                . . . # .
                . . . # .
                . . . # .
                . . . # .
                `)
            basic.pause(500)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . # .
                `)
            use4 = 0
        }
        if (4 == player.get(LedSpriteProperty.X)) {
            basic.showLeds(`
                . . . . #
                . . . . #
                . . . . #
                . . . . #
                . . . . #
                `)
            basic.pause(500)
            basic.showLeds(`
                . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . . . #
                `)
            use5 = 0
        }
        shoot = 0
    }
})
input.onButtonPressed(Button.B, function () {
    player.move(1)
})
let er5 = 0
let e5: game.LedSprite = null
let er4 = 0
let e4: game.LedSprite = null
let er3 = 0
let e3: game.LedSprite = null
let er2 = 0
let e2: game.LedSprite = null
let er1 = 0
let e1: game.LedSprite = null
let enemy = 0
let player: game.LedSprite = null
let a1: number;
let a2: number;
let a3: number;
let use4: number;
let use5: number;
let shoot: number;
game.setScore(0)
player = game.createSprite(2, 5)
basic.forever(function () {
    basic.pause(1000)
    enemy = randint(0, 4)
    if (enemy == 0) {
        e1 = game.createSprite(enemy, 0)
        er1 = 1
    }
    if (enemy == 1) {
        e2 = game.createSprite(enemy, 0)
        er2 = 1
    }
    if (enemy == 2) {
        e3 = game.createSprite(enemy, 0)
        er3 = 1
    }
    if (enemy == 3) {
        e4 = game.createSprite(enemy, 0)
        er4 = 1
    }
    if (enemy == 4) {
        e5 = game.createSprite(enemy, 0)
        er5 = 1
    }
    basic.pause(500)
})
basic.forever(function () {
    basic.pause(500)
    if (er1 == 1) {
        e1.change(LedSpriteProperty.Y, 1)
        if (e1.get(LedSpriteProperty.Y) == 4) {
            e1.delete()
            game.gameOver()
        }
    }
    if (er2 == 1) {
        e2.change(LedSpriteProperty.Y, 1)
        if (e2.get(LedSpriteProperty.Y) == 4) {
            e2.delete()
            game.gameOver()
        }
    }
    if (er3 == 1) {
        e3.change(LedSpriteProperty.Y, 1)
        if (e3.get(LedSpriteProperty.Y) == 4) {
            e3.delete()
            game.gameOver()
        }
    }
    if (er4 == 1) {
        e4.change(LedSpriteProperty.Y, 1)
        if (e4.get(LedSpriteProperty.Y) == 4) {
            e4.delete()
            game.gameOver()
        }
    }
    if (er5 == 1) {
        e5.change(LedSpriteProperty.Y, 1)
        if (e5.get(LedSpriteProperty.Y) == 4) {
            e5.delete()
            game.gameOver()
        }
    }
})
