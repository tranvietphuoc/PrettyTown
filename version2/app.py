from flask import Flask, render_template, redirect, url_for, request, flash
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
PROJECT_DIR = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))
EXCEL_DIR = os.path.join(PROJECT_DIR, "DSHC.xls")


# authorize app with google
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    "./version2/prettyTown-fa1b06e865ad.json", scope
)
gc = gspread.authorize(credentials)

# read excel


# routes
@app.route("/get_address", methods=("GET", "POST"))
def get_address():
    pass
