from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm, DarkModeForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd1fcf62fdf859ebebf6e3cd756aaaafc'
DARK_MODE = True
posts = [
    {
        'author': 'Test User',
        'title': 'Blog Post',
        'content': 'First post',
        'date': 'April 1 2020'
    },
    {
        'author': 'Test User123123',
        'title': 'Blog Post 2',
        'content': 'second post',
        'date': 'April 10 2020'
    }
]


@app.context_processor
def utility_processor():
    def dark_mode_class(dark_mode):
        if dark_mode:
            return 'dark-theme'
        else:
            return None

    return dict(dark_mode_class=dark_mode_class)


@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    text = 'Hello'
    form = DarkModeForm()
    form.validate_on_submit()
    text = str(form.toggle.data)
    if text == 'True':
        pass
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'admin456':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
