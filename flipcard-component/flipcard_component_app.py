from pydantic import BaseModel
from typing import Any, Callable

import mesop as me
import mesop.labs as mel

@mel.web_component(path="./flipcard_component.js")
def counter_component(
  *,
  answer: int,
  on_toggle: Callable[[mel.WebEvent], Any],
  key: str | None = None,
):
  return mel.insert_web_component(
    name="flipcard-component",
    key=key,
    events={
      "toggleEvent": on_toggle,
    },
    properties={
      "answer": answer,
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
    answer=me.state(State).answer,
    on_toggle=on_toggle,
  )


@me.stateclass
class State:
  answer: bool = False


class ChangeAnswer(BaseModel):
  answer: bool


def on_toggle(e: mel.WebEvent):
  # Creating a Pydantic model from the JSON value of the WebEvent
  # to enforce type safety.
  toggle = ChangeAnswer(**e.value)
  me.state(State).answer = toggle.answer