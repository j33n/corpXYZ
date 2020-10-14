"""empty message

Revision ID: 910d9cb12aea
Revises: 493f22028a9d
Create Date: 2020-10-13 17:50:48.735470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '910d9cb12aea'
down_revision = '493f22028a9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('companyEmail', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('companyName', sa.String(length=80), nullable=False))
    op.drop_constraint('user_email_key', 'user', type_='unique')
    op.create_unique_constraint(None, 'user', ['companyEmail'])
    op.create_unique_constraint(None, 'user', ['companyName'])
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.create_unique_constraint('user_email_key', 'user', ['email'])
    op.drop_column('user', 'companyName')
    op.drop_column('user', 'companyEmail')
    # ### end Alembic commands ###