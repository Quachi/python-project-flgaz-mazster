"""
      file routes: routes file
"""
from flask import Blueprint, render_template, request, redirect, url_for
from models.message import Message
from controller.message import get_message, add_message


# Set up a Blueprint
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')


@main_bp.route('/')
def home():
    """
      function home: show route index
    """
    return 'Bienvenue !'


@main_bp.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """
      function save_gazouille: save gazouille or show form to add a gaz
    """
    if request.method == 'POST':
        print(request.form)
        add_message(request.form)
        return redirect(url_for('main_bp.timeline'))
        # return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')


@main_bp.route('/timeline', methods=['GET'])
def timeline():
    """
      function timeline: show all gazouille from oldest to latest
      Return
      -------
      template
      render html template
    """
    messages = get_message()
    return render_template("timeline.html", messages=messages)


@main_bp.route('/timeline/<username>', methods=['GET'])
def timeline_user(username):
    """
      function timeline: show all gazouille to one user
      Return
      -------
      template
      render html template timeline
    """
    messages = Message.query.filter_by(name=username)
    return render_template("timeline.html", messages=messages)


@main_bp.after_request
def add_header(response):
    header = response.headers
    response.cache_control.max_age = 300
    header['Access-Control-Allow-Origin'] = [
        '195.154.176.62',
        '80.214.66.162',
        '92.184.97.65',
        '195.5.249.37'
    ]
    return response
