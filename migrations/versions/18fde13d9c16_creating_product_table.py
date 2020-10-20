"""Creating product table

Revision ID: 18fde13d9c16
Revises: 26ed4eaa5802
Create Date: 2020-10-20 17:06:35.573161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18fde13d9c16'
down_revision = '26ed4eaa5802'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('price', sa.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###
