"""empty message

Revision ID: acfff0cda608
Revises: 
Create Date: 2024-12-18 13:17:55.059515

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'acfff0cda608'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('numero', sa.Integer(), nullable=False),
    sa.Column('cpf', sa.Integer(), nullable=False),
    sa.Column('data_compra', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cliente')
    # ### end Alembic commands ###