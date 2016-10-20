"""empty message

Revision ID: 25e04c860601
Revises: 015fa797609a
Create Date: 2016-10-20 10:03:11.322198

"""

# revision identifiers, used by Alembic.
revision = '25e04c860601'
down_revision = '015fa797609a'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reported_cases', sa.Column('closed_date', sa.Date(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reported_cases', 'closed_date')
    ### end Alembic commands ###
