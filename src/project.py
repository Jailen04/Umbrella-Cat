#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys, random
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((500, 500),0,32)

umbrella = pygame.image.load("umb.png"). convert_alpha()
new_width = 120
new_height = 120
shrunk_umbrella = pygame.transform.scale(umbrella, (new_width, new_height))
umbrella_rect = shrunk_umbrella.get_rect()
umbrella_pos = (200, 200)
umbrella_mask = pygame.mask.from_surface(shrunk_umbrella)
mask_image = umbrella_mask.to_surface()

def update(self):
    if pygame.mouse.get_pos():
        umbrella_rect.center = pygame.mouse.get_pos()

screen.blit(mask_image, umbrella_pos)

# a particle is...
# a thing that exists at a location
# typically moves around
# typically changes over time
# and typically disappears after a certain amount of time
 
# [loc, velocity, timer]
particles = []

# Loop ------------------------------------------------------- #
while True:
    
    # Background --------------------------------------------- #
    screen.fill((0,0,0))

    for i in range(3):
        particles.append([[random.randint(0, 500), 0], [0, 5], 1, []])

    # Update particles
    for particle in particles:
        # Store the position in the trail
        particle[3].append(particle[0][:])  # Save the current position

        # Update particle position
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        
        # Fade the particle (you can adjust the size here)
        particle[2] -= 0  # Particle "fades" by shrinking in size

        # Add gravity effect (falling down faster)
        particle[1][1] += 0.02


        max_trail_length = 3
        # Draw the particle trail
        for i, pos in enumerate(particle[3]):
            # Fade the trail over time by decreasing size
            size = max(1, int(particle[2] - (i * 0.1)))
            pygame.draw.circle(screen, (173, 216, 230), [int(pos[0]), int(pos[1])], size)
            fade_factor = max(0, 255 - (i * 50))

        trail_color = (173, 216, 230, fade_factor)
        trail_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(trail_surface, trail_color, (size, size), size)
        screen.blit(trail_surface, (pos[0] - size, pos[1] - size))

        if len(particle[3]) > max_trail_length:
            particle[3].pop(0)

        if particle[0][1] >= 650:
            #for trail in particle[3]:
                #particle[3].remove(trail)
                #del trail
            particles.remove(particle)
            #del particle

        particle_surface = pygame.Surface((5, 5), pygame.SRCALPHA)  # Small particle size
        pygame.draw.circle(particle_surface, (173, 216, 230), (2, 2), 2)

        particle_mask = pygame.mask.from_surface(particle_surface)
        trail_mask = pygame.mask.from_surface(trail_surface)

    # Collision ---------------------------------------------- #
    #offset_x = particle[0] - umbrella_rect.left
    #offset_y = particle[1] - umbrella_rect.top
    #if umbrella_mask.overlap(particle_mask,(offset_x,offset_y)):
        #print("collision")

    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
                
    # Update ------------------------------------------------- #
    pygame.display.update()
    mainClock.tick(60)