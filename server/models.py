
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Customer(db.Model, SerializerMixin):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)

    #Relationship
    reviews = db.relationship('Review', back_populates='customer', cascade='all, delete-orphan')

    serialize_rules = ('-reviews.customer',)

    # Define items relationship through Review
    items = association_proxy('reviews', 'item', creator=lambda item: Review(item=item))

   # The association_proxy
    item_names = association_proxy('items', 'name')

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}')>"

class Item(db.Model, SerializerMixin):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    price = db.Column(db.Float, nullable=True)
    #Relationship
    reviews = db.relationship('Review', back_populates='item', cascade='all, delete-orphan')

    serialize_rules = ('-reviews.item',)

class Review(db.Model, SerializerMixin):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=True)
    comment = db.Column(db.String(255))
    #Foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id') ,nullable=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=True)


    #Relationships
    customer = db.relationship('Customer', back_populates='reviews')
    item = db.relationship('Item', back_populates='reviews')

    serialize_rules = ('-customer.reviews', '-item.reviews',)

