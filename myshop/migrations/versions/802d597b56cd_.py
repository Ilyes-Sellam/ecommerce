"""empty message

Revision ID: 802d597b56cd
Revises: b631f5c8d56b
Create Date: 2022-04-19 22:50:25.397217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '802d597b56cd'
down_revision = 'b631f5c8d56b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'image_file')
    # ### end Alembic commands ###
