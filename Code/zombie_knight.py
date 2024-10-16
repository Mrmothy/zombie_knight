from os.path import join
import pygame, random
#Use 2D vectors
vector = pygame.math.Vector2

#Initialize Pygame
pygame.init()

#Set display surface (Tile size is 32x32 so 1280/32 = 40 tiles wide and 736/32 = 23 tiles height)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#TODO Define classes
class Game():
    """A class to manage gameplay"""

    def __init__(self):
        """Initialize the game"""
        #Set constant variables
        self.STARTING_ROUND_TIME = 30

        #Set game values
        self.score = 0
        self.round_number = 1
        self.frame_count = 0
        self.round_time = self.STARTING_ROUND_TIME

        #Set fonts
        self.title_font = pygame.font.Font(join('Assets', 'fonts', 'Poultrygeist.ttf'), 48)
        self.HUD_font = pygame.font.Font(join('Assets', 'fonts', 'Pixel.ttf'), 24)

    def update(self):
        """Update the game"""
        #Update the round time every second
        self.frame_count += 1 
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

    def draw(self):
        """Draw the game HUD"""
        #Set Colors
        WHITE = (255, 255, 255)
        GREEN = (25, 200, 25)

        #Set Text
        score_text = self.HUD_font.render(f"Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, WINDOW_HEIGHT - 50)

        health_text = self.HUD_font.render(f"Health: {100}", True, WHITE)
        health_rect = health_text.get_rect()
        health_rect.topleft = (10, WINDOW_HEIGHT - 25)

        title_text = self.title_font.render("Zombie Knight", True, GREEN)
        title_rect = title_text.get_rect()
        title_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 25)

        round_text = self.HUD_font.render(f"Night: {self.round_number}", True, WHITE)
        round_rect = round_text.get_rect()
        round_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 50)

        time_text = self.HUD_font.render(f"Sunrise In: {self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, WINDOW_HEIGHT - 25)

        #Draw the HUD
        display_surface.blit(score_text, score_rect)
        display_surface.blit(health_text, health_rect)
        display_surface.blit(title_text, title_rect)
        display_surface.blit(round_text, round_rect)
        display_surface.blit(time_text, time_rect)

    def add_zombie(self):
        """Add a zombie to the game"""
        pass

    def check_collisions(self):
        """Check collisions that affect gameplay"""
        pass

    def check_round_completion(self):
        """Check if the player survived a single night"""
        pass

    def check_game_over(self):
        """Check to see if the player lost the game"""
        pass

    def start_new_round(self):
        """Start a new night"""
        pass

    def pause_game(self):
        """Pause the game"""
        pass

    def rest_game(self):
        """Rest the game"""
        pass

class Tile(pygame.sprite.Sprite):
    """A class to represent a 32x32 pixel area in our display"""

    def __init__(self, x, y, image_int, main_group, sub_group=""):
        """Initialize the tile"""
        super().__init__()
        #Load in the correct image and add it to the correct sub group
        #Dirt Tiles
        if image_int == 1:
            self.image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'tiles', 'Tile (1).png')), (32, 32))
        #Platform Tiles
        elif image_int == 2:
            self.image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'tiles', 'Tile (2).png')), (32, 32))
            sub_group.add(self)
        elif image_int == 3:
            self.image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'tiles', 'Tile (3).png')), (32, 32))
            sub_group.add(self)
        elif image_int == 4:
            self.image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'tiles', 'Tile (4).png')), (32, 32))
            sub_group.add(self)
        elif image_int == 5:
            self.image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'tiles', 'Tile (5).png')), (32, 32))
            sub_group.add(self)

        #Add every tile to the main group
        main_group.add(self)

        #Get the rect of the image and position with in the grid
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

class Player(pygame.sprite.Sprite):
    """A class the user can control"""

    def __init__(self, x, y, platform_group, portal_group, bullet_group):
        """Initialize the player"""
        super().__init__()

        #Set constant variables 
        self.HORIZONTAL_ACCELERATION = 2
        self.HORIZONTAL_FRICTION = 0.15
        self.VERTICAL_ACCELERATION = 0.8  #Gravity
        self.VERTICAL_JUMP_SPEED = 18  #Determines how high the player can jump
        self.STARTING_HEALTH = 100

        #Animation Frames
        self.move_right_sprites = []
        self.move_left_sprites = []
        self.idle_right_sprites = []
        self.idle_left_sprites = []
        self.jump_right_sprites = []
        self.jump_left_sprites = []
        self.attack_right_sprites = []
        self.attack_left_sprites = []

        #Moving
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (2).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (3).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (1).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (4).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (5).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (6).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (7).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (8).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (9).png')), (64, 64)))
        self.move_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'run', 'Run (10).png')), (64, 64)))
        for sprite in self.move_right_sprites:
            self.move_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Idling 
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (1).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (2).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (3).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (4).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (5).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (6).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (7).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (8).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (9).png')), (64, 64)))
        self.idle_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'idle', 'Idle (10).png')), (64, 64)))
        for sprite in self.idle_right_sprites:
            self.idle_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Jumping
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (1).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (2).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (3).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (4).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (5).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (6).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (7).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (8).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (9).png')), (64, 64)))
        self.jump_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'jump', 'Jump (10).png')), (64, 64)))
        for sprite in self.jump_right_sprites:
            self.jump_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Attacking
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (1).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (2).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (3).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (4).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (5).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (6).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (7).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (8).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (9).png')), (64, 64)))
        self.attack_right_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'player', 'attack', 'Attack (10).png')), (64, 64)))
        for sprite in self.attack_right_sprites:
            self.attack_left_sprites.append(pygame.transform.flip(sprite, True, False))

        #Load image and get rect
        self.current_sprite = 0
        self.image = self.idle_right_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Attach sprite group
        self.platform_group = platform_group
        self.portal_group = portal_group
        self.bullet_group = bullet_group

        #Animation booleans
        self.animat_jump = False
        self.animat_fire = False

        #Load Sounds and set Volumes
        self.jump_sound = pygame.mixer.Sound(join('Assets', 'sounds', 'jump_sound.wav'))
        self.jump_sound.set_volume(.25)
        self.slash_sound = pygame.mixer.Sound(join('Assets', 'sounds', 'slash_sound.wav'))
        self.slash_sound.set_volume(.25)
        self.portal_sound = pygame.mixer.Sound(join('Assets', 'sounds', 'portal_sound.wav'))
        self.portal_sound.set_volume(.25)
        self.hit_sound = pygame.mixer.Sound(join('Assets', 'sounds', 'player_hit.wav'))
        self.hit_sound.set_volume(.25)

        #Kinematics vectors
        self.position = vector(x, y)
        self.velocity = vector(0, 0)
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #Set initial player values
        self.health = self.STARTING_HEALTH
        self.starting_x = x
        self.starting_y = y

    def update(self):
        """Update the player"""
        self.move()
        self.check_collisions()
        self.check_animations()

    def move(self):
        """Move the player"""
        #Set the acceleration vector
        self.acceleration = vector(0, self.VERTICAL_ACCELERATION)

        #If user is pressing a key, set the x-component of the acceleration to be non-zero
        keys =  pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acceleration.x = -1*self.HORIZONTAL_ACCELERATION
        elif keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION

        #Calculate new kinematics values: (4, 1) + (2, 8) = (6, 9)
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration
        self.position += self.velocity + 0.5*self.acceleration

        #Update rect based on kinematics and wrap around movement
        if self.position.x < 0:
            self.position.x = WINDOW_WIDTH
        elif self.position.x > WINDOW_WIDTH:
            self.position.x = 0

        self.rect.bottomleft = self.position

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass

    def check_animations(self):
        """Check to see if jump or fire animations should run"""
        pass

    def jump(self):
        """Jump upwards if on a platform"""
        pass

    def fire(self):
        """Fire a (bullet)"""
        pass

    def reset(self):
        """Reset the player's position"""
        pass

    def animate(self):
        """Animate the player's actions"""
        pass

class Bullet(pygame.sprite.Sprite):
    """A projectile launched by the player"""

    def __init__(self):
        """Initialize the bullet"""
        pass

    def update(self):
        """Update the bullet"""
        pass

class Zombie(pygame.sprite.Sprite):
    """An enemy class to move across the screen"""

    def __init__(self):
        """Initialize the zombie"""
        pass
    
    def update(self):
        """Update the zombie"""
        pass

    def move(self):
        """Move the zombie"""
        pass

    def check_collisions(self):
        """Check for collisions with platforms and portals"""
        pass

    def check_animations(self):
        """Check to see if death or rise animations should run"""
        pass

    def reset(self):
        """Reset the zombie's position"""
        pass

    def animate(self):
        """Animate the zombie's actions"""
        pass

class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animater. A Ruby will be generated here"""

    def __init__(self, x, y, main_group):
        """Initialize the ruby maker"""
        super().__init__()

        #Animation frames
        self.ruby_sprites = []

        #Rotating 
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile000.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile001.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile002.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile003.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile004.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile005.png')), (64,64)))
        self.ruby_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'ruby', 'tile006.png')), (64,64)))

        #Load image and get rect
        self.current_sprite = 0 
        self.image = self.ruby_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Add to the main group for drawing purposes
        main_group.add(self)

    def update(self):
        """Update the ruby maker"""
        self.animate(self.ruby_sprites, .25)

    def animate(self, sprite_list, speed):
        """Animate the ruby maker"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]

class Ruby(pygame.sprite.Sprite):
    """A class the player must collect to earn points and health"""

    def __init__(self):
        """Initialize a ruby"""
        pass

    def update(self):
        """Update the ruby"""
        pass

    def move(self):
        """Move the ruby"""
        pass

    def check_collisions(self):
        """Check collisions with platforms and portals"""
        pass

    def animate(self):
        """Animate the ruby"""
        pass

class Portal(pygame.sprite.Sprite):
    """A class that if collided with will transport you"""

    def __init__(self, x, y, color, portal_group):
        """Initialize the portal"""
        super().__init__()

        #Animation frames
        self.portal_sprites = []

        #Portal animation
        if color == "green":
            #Green portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile000.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile001.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile002.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile003.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile004.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile005.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile006.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile007.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile008.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile009.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile010.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile011.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile012.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile013.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile014.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile015.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile016.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile017.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile018.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile019.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile020.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'green', 'tile021.png')), (72,72)))
        else:
            #Purple Portal
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile000.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile001.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile002.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile003.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile004.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile005.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile006.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile007.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile008.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile009.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile010.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile011.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile012.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile013.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile014.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile015.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile016.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile017.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile018.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile019.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile020.png')), (72,72)))
            self.portal_sprites.append(pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'portals', 'purple', 'tile021.png')), (72,72)))

        #Load an image and get rect
        self.current_sprite = random.randint(0, len(self.portal_sprites)-1)
        self.image = self.portal_sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x, y)

        #Add to Portal Group
        portal_group.add(self)

    def update(self):
        """Update the portal"""
        self.animate(self.portal_sprites, .1)

    def animate(self, sprite_list, speed):
        """Animate the portal"""
        if self.current_sprite < len(sprite_list) -1:
            self.current_sprite += speed
        else:
            self.current_sprite = 0
        
        self.image = sprite_list[int(self.current_sprite)]

#Create sprite group    
my_main_tile_group = pygame.sprite.Group()
my_platform_group = pygame.sprite.Group()

my_player_group = pygame.sprite.Group()
my_bullet_group = pygame.sprite.Group()

my_zombie_group = pygame.sprite.Group()

my_portal_group = pygame.sprite.Group()
my_ruby_group = pygame.sprite.Group()

#Create a tile map 
#0 -> No Tile, 1 -> Dirt, 2-5 -> Platforms, 6 -> Ruby Maker, 7-8 -> Portals, 9 -> Player
#23 rows and 40 columns
tile_map = [
#    1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0],
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#Generate tile objects from the tile map
#Loop through the 23 lists (rows) in the tile map (i moves us down)
for i in range(len(tile_map)):
    #Loop through the 40 elements in a given list (cols) (j moves us across the map)
    for j in range(len(tile_map[i])):
        #Dirt tile
        if tile_map[i][j] == 1:
            Tile(j*32, i*32, 1, my_main_tile_group)
        #Platform Tiles
        elif tile_map[i][j] == 2:
            Tile(j*32, i*32, 2, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 3:
            Tile(j*32, i*32, 3, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 4:
            Tile(j*32, i*32, 4, my_main_tile_group, my_platform_group)
        elif tile_map[i][j] == 5:
            Tile(j*32, i*32, 5, my_main_tile_group, my_platform_group)
        #Ruby Maker
        elif tile_map[i][j] == 6:
            RubyMaker(j*32, i*32, my_main_tile_group)
        #Portals
        elif tile_map[i][j] == 7:
            Portal(j*32, i*32, "green", my_portal_group)
        elif tile_map[i][j] == 8:
            Portal(j*32, i*32, "purple", my_portal_group)
        #Player
        elif tile_map[i][j] == 9:
            my_player = Player(j*32 - 32, i*32 + 32, my_platform_group, my_portal_group, my_bullet_group)
            my_player_group.add(my_player)

#Load in a background image (must resize image)
background_image = pygame.transform.scale(pygame.image.load(join('Assets', 'images', 'background.png')),(1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0, 0)

#Create a game object
my_game = Game()

#Main Game Loop
running = True
while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit background image to screen
    display_surface.blit(background_image, background_rect)

    #Draw tiles and Update Ruby maker
    my_main_tile_group.update()
    my_main_tile_group.draw(display_surface)

    my_portal_group.update()
    my_portal_group.draw(display_surface)

    my_player_group.update()
    my_player_group.draw(display_surface)

    #Update and the game
    my_game.update()
    my_game.draw()

    #Update The display and tick clock
    pygame.display.update()
    clock.tick(FPS)


#End game loop
pygame.quit()