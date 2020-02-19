from app import create_app
from flask import render_template

app = create_app()
app.app_context().push()


if __name__ == '__main__':
    app.run()
