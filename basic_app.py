import datetime
from flask import Flask, request, render_template,session,Response
from flask_babelex import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_user import current_user, login_required, roles_required, UserManager, UserMixin
from model import entities
from database import connector
import json
import os

db = connector.Manager()
engine = db.createEngine()

# Class-based application configuration
class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'sqlite:///basic_app.sqlite'  # File-based SQL database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'jonathanprieto738@gmail.com'
    MAIL_PASSWORD = 'Pokemon 1289'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@onlinelibrarype.com>'

    # Flask-User settings
    USER_APP_NAME = "Online Library Peru"  # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True  # Enable email authentication
    USER_ENABLE_USERNAME = False  # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@onlinelibrarype.com"


def create_app():
    """ Flask application factory """

    # Create Flask app load app.config
    app = Flask(__name__)
    app.config.from_object(__name__ + '.ConfigClass')

    # Initialize Flask-BabelEx
    babel = Babel(app)

    # Initialize Flask-SQLAlchemy
    db = SQLAlchemy(app)

    # Define the User data-model.
    # NB: Make sure to add flask_user UserMixin !!!
    class User(db.Model, UserMixin):
        __tablename__ = 'users'
        id = db.Column(db.Integer, primary_key=True)
        active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')

        # User authentication information. The collation='NOCASE' is required
        # to search case insensitively when USER_IFIND_MODE is 'nocase_collation'.
        email = db.Column(db.String(255, collation='NOCASE'), nullable=False, unique=True)
        email_confirmed_at = db.Column(db.DateTime())
        password = db.Column(db.String(255), nullable=False, server_default='')

        # User information
        first_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')
        last_name = db.Column(db.String(100, collation='NOCASE'), nullable=False, server_default='')

        # Define the relationship to Role via UserRoles
        roles = db.relationship('Role', secondary='user_roles')

    # Define the Role data-model
    class Role(db.Model):
        __tablename__ = 'roles'
        id = db.Column(db.Integer(), primary_key=True)
        name = db.Column(db.String(50), unique=True)

    # Define the UserRoles association table
    class UserRoles(db.Model):
        __tablename__ = 'user_roles'
        id = db.Column(db.Integer(), primary_key=True)
        user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
        role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

    # Setup Flask-User and specify the User data-model
    user_manager = UserManager(app, db, User)

    # Create all database tables
    db.create_all()

    # Create 'member@example.com' user with no roles
    if not User.query.filter(User.email == 'member@example.com').first():
        user = User(
            email='member@example.com',
            email_confirmed_at=datetime.datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        db.session.add(user)
        db.session.commit()

    # Create 'admin@example.com' user with 'Admin' and 'Agent' roles
    if not User.query.filter(User.email == 'admin@example.com').first():
        user = User(
            email='admin@example.com',
            email_confirmed_at=datetime.datetime.utcnow(),
            password=user_manager.hash_password('Password1'),
        )
        user.roles.append(Role(name='Admin'))
        user.roles.append(Role(name='Agent'))
        db.session.add(user)
        db.session.commit()

    # The Home page is accessible to anyone
    @app.route('/')
    def home_page():
        return render_template("index.html")

    # The Members page is only accessible to authenticated users
    @app.route('/biblioteca')
    @login_required  # Use of @login_required decorator
    def biblioteca():
        return render_template("biblioteca.html")

    @app.route('/biblioteca2')
    @login_required  # Use of @login_required decorator
    def biblioteca2():
        return render_template("biblioteca2.html")

    # The Admin page requires an 'Admin' role.
    @app.route('/nuevolibro')
    @roles_required('Admin')  # Use of @roles_required decorator
    def admin_new_libro():
        return render_template("nuevolibro.html")

    @app.route('/actualizarlibro')
    @roles_required('Admin')
    def admin_updatelibro():
        return render_template("updatelibro.html")

    @app.route('/libro', methods=['Post'])
    def create_book():
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        imagen = request.files['imagen']
        archivo = request.files['archivo']
        nombreimagen=imagen.filename
        nombrearchivo = archivo.filename
        rutaimagen=os.path.abspath(nombreimagen)
        rutaarchivo=os.path.abspath(nombrearchivo)
        libro = entities.Libro(titulo=titulo,
                             autor=autor,
                             genero=genero,
                             imagen=imagen.read(),
                             archivo=archivo.read(),
                             nombreimagen=nombreimagen,
                             nombrearchivo=nombrearchivo,
                             rutaimagen=rutaimagen,
                             rutaarchivo=rutaarchivo)
        session = db.Session(engine)
        session.add(libro)
        session.commit()
        return render_template('success.html')

    @app.route('/libro/<id>', methods=['PUT'])
    def update_book(id):
        session = db.Session(engine)
        libros = session.query(entities.Libro).filter(entities.Libro.id == id)

        for libro in libros:
            libro.titulo = request.form['titulo']
            libro.autor = request.form['autor']
            libro.genero = request.form['genero']
            libro.imagen = request.files['imagen']
            libro.archivo = request.files['archivo']
            nombreimagen=imagen.filename
            nombrearchivo = archivo.filename
            libro.nombreimagen=nombreimagen
            libro.nombrearchivo = nombrearchivo
            libro.rutaimagen=os.path.abspath(nombreimagen)
            libro.rutaarchivo=os.path.abspath(nombrearchivo)
            session.add(libro)
        session.commit()
        return render_template('success.html')

    @app.route('/imagen/<id>', methods=['GET'])
    def imagen(id):
        db_session = db.Session(engine)
        libros = db_session.query(entities.Libro).filter(entities.Libro.id == id)
        data = []
        for libro in libros:
            data.append(libro)
            break
        return Response(data[0].imagen, mimetype='image/png')

    @app.route('/archivo/<id>', methods=['GET'])
    def archivo(id):
        db_session = db.Session(engine)
        libros = db_session.query(entities.Libro).filter(entities.Libro.id == id)
        data = []
        for libro in libros:
            data.append(libro)
            break
        return Response(data[0].archivo, mimetype='application/pdf')

    @app.route('/libros', methods=['GET'])
    @roles_required('Admin')
    def libros():
        db_session = db.Session(engine)
        libros = db_session.query(entities.Libro)
        data = []
        for libro in libros:
            data.append(libro)
        return Response(json.dumps(data,
                                   cls=connector.AlchemyEncoder),
                        mimetype='application/json')

    return app


# Start development web server
if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=8080, debug=True)