from flask import Flask, render_template

from pathlib import Path

import yaml

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

@app.route("/")
def home():
  return render_template("index.html", makes=config["makes"])
