from typing import Literal

import pytest

from fsm import State, StateMachine, InvalidEventError


def test_state_machine_send() -> None:
    s: StateMachine[
        Literal["start", "finish", "help"], Literal["TOGGLE", "TO_HELP"]
    ] = StateMachine(
        initial="start",
        states={
            "start": State(on={"TOGGLE": "finish", "TO_HELP": "help"}),
            "finish": State(on={"TOGGLE": "start"}),
            "help": State(on={}),
        },
    )
    assert s.send("TOGGLE") == "finish"
    assert s.send("TOGGLE") == "start"
    assert s.send("TOGGLE") == "finish"
    assert s.send("TOGGLE") == "start"
    assert s.send("TO_HELP") == "help"


def test_state_machine_send_with_invalid_event() -> None:
    s: StateMachine[
        Literal["start", "finish", "help"], Literal["TOGGLE", "TO_HELP"]
    ] = StateMachine(
        initial="start",
        states={
            "start": State(on={"TOGGLE": "finish", "TO_HELP": "help"}),
            "finish": State(on={"TOGGLE": "start"}),
            "help": State(on={}),
        },
    )
    assert s.send("TOGGLE") == "finish"
    assert s.send("TOGGLE") == "start"
    assert s.send("TOGGLE") == "finish"
    assert s.send("TOGGLE") == "start"
    assert s.send("TO_HELP") == "help"
    with pytest.raises(InvalidEventError):
        s.send("TOGGLE")


def test_state_machine_transition() -> None:
    s: StateMachine[
        Literal["start", "finish", "help"], Literal["TOGGLE", "TO_HELP"]
    ] = StateMachine(
        initial="start",
        states={
            "start": State(on={"TOGGLE": "finish", "TO_HELP": "help"}),
            "finish": State(on={"TOGGLE": "start"}),
            "help": State(on={}),
        },
    )
    assert s.transition("finish", "TOGGLE") == "start"
    assert s.transition("start", "TOGGLE") == "finish"
    assert s.transition("start", "TO_HELP") == "help"


def test_state_machine_transition_with_invalid_event() -> None:
    s: StateMachine[
        Literal["start", "finish", "help"], Literal["TOGGLE", "TO_HELP"]
    ] = StateMachine(
        initial="start",
        states={
            "start": State(on={"TOGGLE": "finish", "TO_HELP": "help"}),
            "finish": State(on={"TOGGLE": "start"}),
            "help": State(on={}),
        },
    )
    with pytest.raises(InvalidEventError):
        s.transition("help", "TOGGLE")
