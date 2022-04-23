"""empty message

Revision ID: e408d588b5ae
Revises: 
Create Date: 2022-04-17 01:38:22.750145

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e408d588b5ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart')
    op.drop_table('order')
    op.drop_table('order_product')
    op.drop_table('customer')
    op.drop_table('product')
    op.drop_table('categorie')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorie',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('categorie_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('pr_categorie_description', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='categorie_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('product_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('pr_name', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('pr_price', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('pr_color', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('pr_size', sa.VARCHAR(length=50), autoincrement=False, nullable=True),
    sa.Column('pr_description', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('categorie_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['categorie_id'], ['categorie.id'], name='product_categorie_id_fkey'),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='product_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='product_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('customer',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('customer_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('adsress', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='customer_pkey'),
    sa.UniqueConstraint('email', name='customer_email_key'),
    sa.UniqueConstraint('username', name='customer_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('order_product',
    sa.Column('order_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name='order_product_order_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='order_product_product_id_fkey')
    )
    op.create_table('order',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='order_customer_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='order_pkey')
    )
    op.create_table('cart',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('customer_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], name='cart_customer_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='cart_product_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='cart_pkey'),
    sa.UniqueConstraint('customer_id', name='cart_customer_id_key')
    )
    # ### end Alembic commands ###