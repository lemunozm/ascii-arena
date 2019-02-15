from .mobile import Mobile
from .entity import Entity
from .spell import Spell

from common.logging import logger
from common.direction import Direction
from common.util.vec2 import Vec2

import time

class ArenaState:
    def __init__(self, step, ground, entity_list, spell_list):
        self._step = step
        self._ground = ground
        self._entity_list = entity_list
        self._spell_list = spell_list

    def get_step(self):
        return self._step


    def get_ground(self):
        return self._ground


    def get_entity_list(self):
        return self._entity_list


    def get_spell_list(self):
        return self._spell_list


    def get_entity_at(self, position):
        for entity in self._entity_list:
            if entity.get_position() == position:
                return entity

        return None


class Control():
    def __init__(self, controllable):
        self._controllable = controllable

    def update(self, state):
        pass


class MobileControl(Control):
    def __init__(self, mobile):
        super().__init__(mobile)
        self._last_movement_time_stamp = 0


    def _compute_movement(self):
        if self._controllable.is_moving():
            current = time.time()
            if current - self._last_movement_time_stamp > 1.0 / self._controllable.get_speed():
                self._last_movement_time_stamp = current
                return Direction.as_vector(self._controllable.get_direction())

        return Vec2.zero()


    def update(self, state):
        super().update(state)

        movement = self._compute_movement()
        if movement != Vec2.zero():
            new_position = self._controllable.get_position() + movement
            if not state.get_ground().is_blocked(new_position) and not state.get_entity_at(new_position):
                self._controllable.set_position(new_position)


class EntityControl(MobileControl):
    def __init__(self, entity):
        super().__init__(entity)


    def update(self, state):
        super().update(state)


class SpellControl(MobileControl):
    def __init__(self, spell):
        super().__init__(spell)


    def update(self, state):
        super().update(state)


class PlayerControl(MobileControl):
    def __init__(self, entity):
        super().__init__(entity)
        self._last_cast_skill = None


    def move(self, direction):
        self._controllable.enable_moving(True)
        if direction != self._controllable.get_direction():
            self._controllable.set_direction(direction)
            self._last_movement_time_stamp = 0


    def cast(self, skill):
        self._last_cast_skill = skill


    def update(self, state):
        previous_position = self._controllable.get_position()

        super().update(state)
        self._controllable.enable_moving(False)
        if self._last_cast_skill != None:
            spell = self._controllable.cast(self._last_cast_skill)
            if spell:
                logger.debug("Player '{}' at step {} casts {}".format(self._controllable.get_character(), state.get_step(), self._last_cast_skill))
            self._last_cast_skill = None

        new_position = self._controllable.get_position()
        if previous_position != new_position:
            logger.debug("Player '{}' at step {} moves {}".format(self._controllable.get_character(), state.get_step(), new_position - previous_position))


