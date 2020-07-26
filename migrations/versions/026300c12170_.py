"""empty message

Revision ID: 026300c12170
Revises: 
Create Date: 2020-07-25 20:48:31.144051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '026300c12170'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bairro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_bairro', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome_bairro')
    )
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('senha', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('alimentos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome_alimento', sa.String(length=30), nullable=False),
    sa.Column('validade', sa.DateTime(), nullable=False),
    sa.Column('ali_idbairro', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ali_idbairro'], ['bairro.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('alimentos')
    op.drop_table('login')
    op.drop_table('bairro')
    # ### end Alembic commands ###
