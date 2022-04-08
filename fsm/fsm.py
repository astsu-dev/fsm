from dataclasses import dataclass
from typing import Generic, Hashable, Mapping, TypeVar

ST = TypeVar("ST", bound=Hashable)
ET = TypeVar("ET", bound=Hashable)


@dataclass(frozen=True)
class State(Generic[ET, ST]):
    on: dict[ET, ST]


class InvalidEventError(Exception):
    """Will be raised if event is not exists for specific state."""


class StateMachine(Generic[ST, ET]):
    def __init__(self, initial: ST, states: Mapping[ST, State[ET, ST]]) -> None:
        self._states = states
        self._current = initial

    def send(self, event: ET) -> ST:
        try:
            new_state = self._states[self._current].on[event]
        except KeyError:
            raise InvalidEventError(event)
        self._current = new_state
        return new_state

    def transition(self, state: ST, event: ET) -> ST:
        try:
            return self._states[state].on[event]
        except KeyError:
            raise InvalidEventError(event)

    @property
    def current(self) -> ST:
        return self._current
