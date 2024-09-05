import mesop as me
from typing import Any, Callable

import mesop.labs as mel

@mel.web_component(path="./code_mirror_editor_component.js")
def code_mirror_editor_component(
  *,
  code: str = "",
  on_editor_blur: Callable[[mel.WebEvent], Any] | None = None,
  height: str = "100%",
  width: str = "100%",
  key: str | None = None,
):
  events = {}
  if on_editor_blur:
    events["editorBlurEvent"] = on_editor_blur

  return mel.insert_web_component(
    name="code-mirror-editor-component",
    key=key,
    events=events,
    properties={
      "code": code,
      "height": height,
      "width": width,
    },
  )


@me.stateclass
class State:
  code: str = "# Add your Python code here."


@me.page(
  path="/",
  stylesheets=[
    "https://cdnjs.cloudflare.com/ajax/libs/codemirror/6.65.7/codemirror.min.css"
  ],
  security_policy=me.SecurityPolicy(
    allowed_connect_srcs=[
      "https://cdnjs.cloudflare.com",
      "*.fonts.gstatic.com",
    ],
    allowed_script_srcs=[
      "https://cdnjs.cloudflare.com",
      "*.fonts.gstatic.com",
      "https://cdn.jsdelivr.net",
    ],
  ),
)
def page():
  state = me.state(State)
  with me.box(
    style=me.Style(
      display="grid",
      padding=me.Padding.all(20),
      gap=10,
      grid_template_rows="1fr 1fr",
      height="100vh",
    )
  ):
    code_mirror_editor_component(code=state.code, on_editor_blur=on_editor_blur)
    with me.box(style=me.Style(overflow_y="scroll", overflow_x="scroll")):
      me.text(
        "Type in some text in the editor. When the editor loses focus, the text below will be updated."
      )
      me.button(
        "Reset Code",
        type="flat",
        style=me.Style(margin=me.Margin.symmetric(vertical=30)),
        on_click=on_reset,
      )
      me.text("Code Output", type="headline-5")
      with me.box(
        style=me.Style(
          background="#fff",
          padding=me.Padding.all(20),
          border=me.Border.all(
            me.BorderSide(width=1, style="solid", color="#ececec")
          ),
        )
      ):
        me.code(state.code)


def on_reset(e: me.ClickEvent):
  state = me.state(State)
  state.code = "# Add your Python code here."


def on_editor_blur(e: mel.WebEvent):
  state = me.state(State)
  state.code = e.value["code"]