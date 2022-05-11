"""Add caretaker model

Revision ID: 98aa38545ab9
Revises: 95bbc272ba58
Create Date: 2022-05-10 10:16:33.214773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98aa38545ab9'
down_revision = '95bbc272ba58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('caretaker',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('caretaker')
    # ### end Alembic commands ###