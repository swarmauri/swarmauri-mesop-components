from pydantic import BaseModel
from typing import Any, Callable

import mesop as me
import mesop.labs as mel

@mel.web_component(path="./counter_component.js")
def counter_component(
  *,
  value: int,
  on_decrement: Callable[[mel.WebEvent], Any],
  key: str | None = None,
):
  return mel.insert_web_component(
    name="quickstart-counter-component",
    key=key,
    events={
      "decrementEvent": on_decrement,
    },
    properties={
      "value": value,
    },
  )


@me.page(
  path="/",
  security_policy=me.SecurityPolicy(
    allowed_script_srcs=[
      "https://cdn.jsdelivr.net",
    ]
  ),
)
def page():
  counter_component(
    value=me.state(State).value,
    on_decrement=on_decrement,
  )


@me.stateclass
class State:
  value: int = 10


class ChangeValue(BaseModel):
  value: int


def on_decrement(e: mel.WebEvent):
  # Creating a Pydantic model from the JSON value of the WebEvent
  # to enforce type safety.
  decrement = ChangeValue(**e.value)
  me.state(State).value = decrement.value