"""Adding a reason field on order table to register cancelation reasons if exists

Revision ID: 9460c2316d92
Revises: 913dd39c61d3
Create Date: 2020-10-26 14:26:48.504025

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9460c2316d92'
down_revision = '913dd39c61d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reason', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('reason')

    # ### end Alembic commands ###