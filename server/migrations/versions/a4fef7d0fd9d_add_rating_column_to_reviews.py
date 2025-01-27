"""Add rating column to reviews

Revision ID: a4fef7d0fd9d
Revises: eeadc41867b8
Create Date: 2025-01-24 13:18:36.546067

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4fef7d0fd9d'
down_revision = 'eeadc41867b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('items', 'price',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.add_column('reviews', sa.Column('rating', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reviews', 'rating')
    op.alter_column('items', 'price',
               existing_type=sa.FLOAT(),
               nullable=True)
    op.alter_column('items', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('customers', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
