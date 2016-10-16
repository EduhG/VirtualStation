"""empty message

Revision ID: 84ad4ea62b49
Revises: 9365c44d1249
Create Date: 2016-10-12 16:49:50.512308

"""

# revision identifiers, used by Alembic.
revision = '84ad4ea62b49'
down_revision = '9365c44d1249'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'email')
    ### end Alembic commands ###