from flask import Flask, render_template

from pathlib import Path

import yaml

app = Flask(
  "homemadebycvg",
  template_folder="templates",
  static_folder="templates/static",
  static_url_path=""
)

app.config["TEMPLATES_AUTO_RELOAD"] = True

with open(Path(__file__).parent / "makes.yaml") as fp:
  config = yaml.safe_load(fp)

@app.route("/")
def home():
  return render_template("index.html", makes=config["makes"])
