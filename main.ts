controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (padCounter > 0) {
        game.splash("You have " + convertToText(padCounter) + " pads left.")
    } else {
        game.over(true)
    }
})
scene.onOverlapTile(SpriteKind.Player, sprites.dungeon.buttonTeal, function (sprite, location) {
    if (pinkibull.tileKindAt(TileDirection.Center, sprites.dungeon.buttonTeal)) {
        tiles.setTileAt(tiles.locationOfSprite(pinkibull), sprites.dungeon.buttonOrange)
        padCounter += -1
    }
})
let padCounter = 0
let pinkibull: Sprite = null
pinkibull = sprites.create(img`
    1 3 3 3 3 3 3 1 3 3 3 3 3 3 3 1 
    3 3 1 3 3 3 3 3 3 3 3 3 3 1 3 3 
    3 3 3 3 3 3 3 1 3 3 3 1 3 3 3 3 
    3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
    1 3 3 1 3 3 3 3 3 3 3 3 1 1 3 3 
    3 3 3 3 3 3 3 3 1 3 3 3 3 3 3 3 
    3 3 3 3 1 3 3 3 3 3 3 3 3 3 1 3 
    3 3 3 3 3 3 3 1 3 3 1 3 3 3 3 3 
    3 1 3 3 3 3 3 3 3 3 3 3 3 1 3 3 
    3 3 3 3 3 3 3 3 3 1 3 3 3 3 3 3 
    3 3 3 3 1 3 3 3 3 3 3 3 3 3 3 3 
    3 3 3 3 3 3 3 3 3 3 3 3 3 1 3 3 
    3 3 3 3 3 3 3 3 1 3 3 3 3 3 3 3 
    1 3 3 1 3 3 1 3 3 3 3 3 3 3 3 3 
    3 3 3 3 3 3 3 3 1 3 3 3 1 3 3 3 
    1 3 3 3 3 3 3 1 3 3 3 3 3 3 3 1 
    `, SpriteKind.Player)
controller.moveSprite(pinkibull)
tiles.setTilemap(tilemap`level1`)
scene.cameraFollowSprite(pinkibull)
tiles.placeOnRandomTile(pinkibull, sprites.dungeon.stairWest)
tiles.coverAllTiles(sprites.dungeon.buttonOrange, sprites.castle.tileGrass1)
padCounter = 18
