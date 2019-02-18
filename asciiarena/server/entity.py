from .mobile import Mobile
from .arena_element import ArenaElement

from .spells.fire_ball import FireBall # remove when skill works properly

class Entity(ArenaElement):
    def __init__(self, character, position):
        super().__init__(position)
        self._control = None
        self._character = character
        self._buff_list = []


    def get_control(self):
        return self._control


    def set_control(self, control):
        self._control = control


    def get_character(self):
        return self._character


    def get_buff_list(self):
        return self._buff_list


    def cast(self, skill):
        cast_position = self.get_position() + self.get_direction_vec()
        return FireBall(int, self, cast_position)


    def add_buff(self, buff):
        pass


    def remove_buff(self, buff):
        pass


    def update(self, state):
        super().update_movement(state.get_ground(), state.get_entity_list())
        if self._control:
            self._control.update(state)


    def on_mobile_collision(self, entity):
        return True


    def on_ground_collision(self, position, terrain):
        return True

