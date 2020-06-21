from app_files import app
from flask import render_template, request, redirect, url_for, make_response

# my name
first_name = "Luis"  # my name
last_name = "Riveron"

# title
title = "Developer"

@app.route('/')
def index():
    """This method is called when navigating to the root '/' of the website.

    Args:
        None.

    Raises:
        None.

    Returns:
        render_template using the 'index.html' and populating it with default values for portfolio
    """

    # when navigating to the website, render the index.html page with default data
    return render_template("index.html", first_name=first_name, last_name=last_name, title=title)

