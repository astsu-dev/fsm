# Finite State Machine

Fully typed finite state machine in Python.

## Quick Start

```python
from typing import Literal

from fsm import State, StateMachine

light_machine: StateMachine[
    Literal["red", "yellow_to_green", "yellow_to_red", "green"], Literal["SWITCH"]
] = StateMachine(
    initial="red",
    states={
        "red": State(on={"SWITCH": "yellow_to_green"}),
        "yellow_to_green": State(on={"SWITCH": "green"}),
        "yellow_to_red": State(on={"SWITCH": "red"}),
        "green": State(on={"SWITCH": "yellow_to_red"}),
    },
)
assert light_machine.send("SWITCH") == "yellow_to_green"
assert light_machine.send("SWITCH") == "green"
assert light_machine.send("SWITCH") == "yellow_to_red"
assert light_machine.send("SWITCH") == "red"
assert light_machine.current == "red"
# raises fsm.InvalidEventError
# light_machine.send("INVALID_EVENT")  # type checker error: invalid event

assert light_machine.transition("red", "SWITCH") == "yellow_to_green"
assert light_machine.transition("green", "SWITCH") == "yellow_to_red"
assert light_machine.transition("yellow_to_red", "SWITCH") == "red"
# light_machine.transition("yellow_to_yellow", "SWITCH")  # type checker error: invalid state
```
