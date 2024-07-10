from flask import Flask, render_template

from pathlib import Path

import yaml
from collections import namedtuple
import markdown

HERE = Path(__file__).parent

app = Flask(
  "homemadebycvg",
  template_folder= HERE / "templates",
  static_folder= HERE / "templates/static",
  static_url_path=""
)

app.config["TEMPLATES_AUTO_RELOAD"] = True

with open(HERE / "makes.yaml") as fp:
  config = yaml.safe_load(fp)

for make in config["makes"].values():
  make["description"] = markdown.markdown(make.pop("description", ""))

Button = namedtuple("Button", "name title icon")

buttons = [
  Button("info",      "get more info...",          "info-circle"),
  Button("run",       "try it...",                 "display"),
  Button("docs",      "read the docs...",          "book"),
  Button("pypi",      "see the module on PyPi...", "box-seam"),
  Button("github",    "see the code on GitHub...", "github" ),
  Button("instagram", "as seen on Instagram...",   "instagram" )
]

@app.route("/")
def home():
  return render_template("index.html", makes=config["makes"], buttons=buttons)
