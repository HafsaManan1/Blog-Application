"""User Model

Revision ID: d48dc28cb4e7
Revises: c7ff47b37e50
Create Date: 2024-09-06 16:52:34.170193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd48dc28cb4e7'
down_revision = 'c7ff47b37e50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=20), nullable=False))
        batch_op.create_unique_constraint('uq_users_username', ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
