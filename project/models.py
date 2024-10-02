"""Model."""

from project.app import db


class Post(db.Model):
    """Post."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        """INIT."""
        self.title = title
        self.text = text

    def __repr__(self):
        """INIT."""
        return f"<title {self.title}>"
