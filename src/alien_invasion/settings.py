class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.text_color = (0, 0, 0)
        self.font = "freesansbold.ttf"
        self.ship_speed = 10
        self.clock = 60

        # Bullet Settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_max_num = 100

        # Alien Settings
        self.aliens_num = 40
        self.alien_margin_x = 5
        self.alien_margin_y = 10
        self.alien_move_x_speed = 1
        self.alien_move_y_speed = 10
        self.alien_bullet_color = (255, 0, 0)
        self.alien_shoot_every_in_seconds = 1

