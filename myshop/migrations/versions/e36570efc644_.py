"""empty message

Revision ID: e36570efc644
Revises: b030c8c9a7fe
Create Date: 2022-04-24 01:33:23.560460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e36570efc644'
down_revision = 'b030c8c9a7fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('available', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'available')
    # ### end Alembic commands ###