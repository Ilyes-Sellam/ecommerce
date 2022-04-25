"""empty message

Revision ID: dc5203695412
Revises: cb7b4a43aa7c
Create Date: 2022-04-25 05:21:37.679898

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc5203695412'
down_revision = 'cb7b4a43aa7c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'image_file')
    # ### end Alembic commands ###
