import mesop as me
import mesop.labs as mel

@mel.web_component(path="./aucplot_component.js")
def aucplot_component(
  *,
  key: str | None = None,
):
  return mel.insert_web_component(
    name="aucplot-component",
    key=key
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
  aucplot_component()
