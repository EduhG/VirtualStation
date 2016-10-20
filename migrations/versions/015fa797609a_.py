"""empty message

Revision ID: 015fa797609a
Revises: 452a5f72303f
Create Date: 2016-10-20 10:01:27.807999

"""

# revision identifiers, used by Alembic.
revision = '015fa797609a'
down_revision = '452a5f72303f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('case_notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ref_id', sa.Integer(), nullable=True),
    sa.Column('notes', sa.String(length=10000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('case_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('complaint', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('complaint')
    )
    op.drop_table('complaint_types')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('complaint_types',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('complaint', sa.VARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('complaint')
    )
    op.drop_table('case_types')
    op.drop_table('case_notes')
    ### end Alembic commands ###