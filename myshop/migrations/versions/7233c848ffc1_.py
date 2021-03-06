"""empty message

Revision ID: 7233c848ffc1
Revises: f56ba0f2cd7a
Create Date: 2022-04-21 01:02:35.019349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7233c848ffc1'
down_revision = 'f56ba0f2cd7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('is_admin', sa.Boolean(), nullable=False))
    op.add_column('product', sa.Column('image_file', sa.String(length=20), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'image_file')
    op.drop_column('customer', 'is_admin')
    # ### end Alembic commands ###
