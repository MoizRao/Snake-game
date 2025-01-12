import pygame
import time
import random
from pygame.locals import *

class Snake:
  def __init__(self, screen):
    self.screen = screen
    img = pygame.image.load("block.png")
    self.block = pygame.transform.scale(img,(15,15))
    self.x_list = [210, 208, 206, 204, 202, 200, 198, 196, 194, 192]
    self.y_list = [100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
    self.direction = "right"
    self.length = 10
    self.increase_length = False

  @property
  def direction(self):
    return self._direction
  @direction.setter
  def direction(self, value):
    self._direction = value

  def set_xy_coordinates(self):
    
    temp_x = self.x_list[-1]
    temp_y = self.y_list[-1]
    self.x_list = right_shift(self.x_list)
    self.y_list = right_shift(self.y_list)
    if self.increase_length:
      self.length += 3
      self.increase_length = False
      self.x_list.append(temp_x)
      self.y_list.append(temp_y)
      self.x_list.append(temp_x - 2)
      self.y_list.append(temp_y - 2)
      self.x_list.append(temp_x - 4)
      self.y_list.append(temp_y - 4)
    
    if self.direction == "right":
      self.x_list[0] += 2
    elif self.direction == "left":
      self.x_list[0] -= 2
    elif self.direction == "up":
      self.y_list[0] -= 2
    elif self.direction == "down":
      self.y_list[0] += 2
    
  def draw_snake(self):
    self.set_xy_coordinates()
    for i in range(self.length):
      self.screen.blit(self.block, (self.x_list[i], self.y_list[i]))

  def check_self_collision(self):
    for i in range(4, self.length):
      if self.x_list[0] == self.x_list[i] and self.y_list[0] == self.y_list[i]:
        return True
    return False


class Game:
  def __init__(self):
    pygame.init()
    self.width = 400
    self.height = 350
    self.food_x = random.randint(25, self.width - 25)
    self.food_y = random.randint(25, self.height - 25)
    img = pygame.image.load("ball.png")
    bg = pygame.image.load("snake_bg.jpg")
    resized = pygame.transform.scale(bg, (self.width, self.height))
    self.bg = resized.copy()
    self.bg.set_alpha(50)
    self.surface = pygame.display.set_mode((self.width, self.height))
    self.food = pygame.transform.scale(img,(30,22))
    self.snake = Snake(self.surface)
    self.game_over = False
    self.score = 0
    self.food_eaten = True
    self.food_x_list =[]
    self.food_y_list =[]
    self.game_starting_pause = True
    self.pause_game = False

  def draw_bg(self):
    self.surface.blit(self.bg, (0,0))

  def check_if_game_over(self):
    if self.snake.x_list[0] >= self.width - 2 or self.snake.y_list[0] >= self.height - 2:
      self.game_over = True
    elif self.snake.x_list[0] <= 2 or self.snake.y_list[0] <=2:
      self.game_over = True
    elif self.snake.check_self_collision():
      self.game_over = True

  def set_food_position(self):
    while True:
      x = random.randint(40, self.width - 40)
      y = random.randint(40, self.height - 40)
      if valid_xy(x, y,self.snake.x_list, self.snake.y_list):
        break

    self.food_x = x
    self.food_y = y
    self.food_x_list = generate_list(self.food_x, 30)
    self.food_y_list = generate_list(self.food_y, 22)
  
  def generate_food(self):
    if self.food_eaten:
      self.food_eaten = False
      self.set_food_position()
      
    self.surface.blit(self.food, (self.food_x, self.food_y))

  def check_if_food_eaten(self):
    if self.snake.x_list[0] in self.food_x_list and self.snake.y_list[0] in self.food_y_list:
      self.food_eaten = True
      self.score += 1  
      self.snake.increase_length = True
  
  def move_snake(self):
    self.draw_bg()
    self.snake.draw_snake()
    pygame.display.flip()
    self.check_if_game_over()

  def display_text(self, text):
    self.surface.fill((0,0,0))
    border_color = (255,255,255)
    border_thickness = 5
    pygame.draw.rect(self.surface, border_color, self.surface.get_rect(), border_thickness)
    font = pygame.font.SysFont("aerial", 30)
    line = font.render(text, True, (255,255,255))
    self.surface.blit(line, (self.width/2 - line.get_width()/2, self.height/2 - line.get_height()/2))
    pygame.display.flip()
    time.sleep(5)
    
  def execute(self):
    self.draw_bg()
    
    while not self.game_over:
      
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.game_over = True
          
        elif event.type == KEYDOWN:
          if event.key == K_ESCAPE:
            self.game_over = True
            
          elif event.key == K_UP:
            if self.snake.direction != "down":
              self.snake.direction = "up" 
 
          elif event.key == K_DOWN:
            if self.snake.direction != "up":
              self.snake.direction = "down"
            
          elif event.key == K_RIGHT:
            if self.snake.direction != "left":
              self.snake.direction = "right"
            
          elif event.key == K_LEFT:
            if self.snake.direction != "right":
              self.snake.direction = "left"
              
          elif event.key == K_p:
            flag = True
            while flag:
              for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_c:
                  flag = False
 
      self.move_snake()
      if self.game_starting_pause:
        self.game_starting_pause = False
        time.sleep(3)
      self.generate_food()
      self.check_if_food_eaten()
      time.sleep(0.015 - (self.score * 0.00011))

    self.display_text(f"You Scored {self.score}")
    self.display_text("Game Over")

def right_shift(arr):
  for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]
  return arr

def valid_xy(x, y, xl, yl):
  for i in range(len(xl)):
    if x == xl[i] and y == yl[i]:
      return False
  return True

def generate_list(start, length):
  arr = []
  for i in range(length):
    arr.append(start + i)
  return arr

def main():
  game = Game()
  game.execute()

if __name__ == "__main__":
  main()
