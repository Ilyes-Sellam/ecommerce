"""empty message

Revision ID: 955ed6c60207
Revises: 802d597b56cd
Create Date: 2022-04-19 22:53:07.677670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '955ed6c60207'
down_revision = '802d597b56cd'
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