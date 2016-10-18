"""empty message

Revision ID: dce9c92f5bfc
Revises: 55785fb198e7
Create Date: 2016-10-18 08:42:30.467809

"""

# revision identifiers, used by Alembic.
revision = 'dce9c92f5bfc'
down_revision = '55785fb198e7'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reported_cases', sa.Column('reported_date', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reported_cases', 'reported_date')
    ### end Alembic commands ###