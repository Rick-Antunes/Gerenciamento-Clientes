"""empty message

Revision ID: 8a55e7e42a3f
Revises: c32aab99a7c7
Create Date: 2025-01-10 13:14:25.822137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a55e7e42a3f'
down_revision = 'c32aab99a7c7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_cadastro', sa.DateTime(), nullable=True))
        batch_op.drop_column('data_compra')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cliente', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data_compra', sa.DATE(), nullable=True))
        batch_op.drop_column('data_cadastro')

    # ### end Alembic commands ###
