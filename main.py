def on_a_pressed():
    if padCounter > 0:
        game.splash("", "")
    else:
        pass
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile(sprite, location):
    global padCounter
    if pinkibull.tile_kind_at(TileDirection.CENTER, sprites.dungeon.button_teal):
        tiles.set_tile_at(tiles.location_of_sprite(pinkibull),
            sprites.dungeon.button_orange)
        padCounter += -1
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.button_teal,
    on_overlap_tile)

padCounter = 0
pinkibull: Sprite = None
pinkibull = sprites.create(img("""
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
    """),
    SpriteKind.player)
controller.move_sprite(pinkibull)
tiles.set_tilemap(tilemap("""
    level1
"""))
scene.camera_follow_sprite(pinkibull)
tiles.place_on_random_tile(pinkibull, sprites.dungeon.stair_west)
tiles.cover_all_tiles(sprites.dungeon.button_orange, sprites.castle.tile_grass1)
padCounter = 18