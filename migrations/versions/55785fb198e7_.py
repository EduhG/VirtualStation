"""empty message

Revision ID: 55785fb198e7
Revises: 84ad4ea62b49
Create Date: 2016-10-17 16:54:33.353964

"""

# revision identifiers, used by Alembic.
revision = '55785fb198e7'
down_revision = '84ad4ea62b49'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('complaint_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('complaint', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('complaint')
    )
    op.create_table('reported_cases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_method', sa.String(length=100), nullable=True),
    sa.Column('id_number', sa.String(length=64), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('other_names', sa.String(length=100), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('phone_number', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('reg_date', sa.String(length=20), nullable=True),
    sa.Column('complaint_type', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id_number')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reported_cases')
    op.drop_table('complaint_types')
    ### end Alembic commands ###
