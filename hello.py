from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from forms import NameForm


app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'sdkjfhiudshfiudshfhsduifiushdnfsdfnisduf'

@app.route('/', methods=['GET', 'POST'])
def index():
    # name = None
    # form = NameForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = ''
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), current_time=datetime.utcnow())


@app.route('/user/<name>/')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500
