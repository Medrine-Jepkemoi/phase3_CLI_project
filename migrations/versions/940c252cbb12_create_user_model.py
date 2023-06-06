"""Create user model

Revision ID: 940c252cbb12
Revises: 
Create Date: 2023-06-06 13:40:51.460012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '940c252cbb12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('admin_fname', sa.String(), nullable=True),
    sa.Column('admin_lname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('admin_id')
    )
    op.create_table('categories',
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('category_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('category_id')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('customer_fname', sa.String(), nullable=True),
    sa.Column('customer_lname', sa.String(), nullable=True),
    sa.Column('customer_mobile', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('orderitems',
    sa.Column('orderitem_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('totalprice', sa.Integer(), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.customer_id'], ),
    sa.PrimaryKeyConstraint('orderitem_id')
    )
    op.create_table('products',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(), nullable=True),
    sa.Column('product_description', sa.String(), nullable=True),
    sa.Column('product_price', sa.Integer(), nullable=True),
    sa.Column('product_amount', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admins.admin_id'], ),
    sa.ForeignKeyConstraint(['category_id'], ['categories.category_id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    op.drop_table('orderitems')
    op.drop_table('customers')
    op.drop_table('categories')
    op.drop_table('admins')
    # ### end Alembic commands ###
