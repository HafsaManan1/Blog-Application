"""removed slug

Revision ID: 65ab9b01991c
Revises: 371b014854d5
Create Date: 2024-09-16 00:12:11.699495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '65ab9b01991c'
down_revision = '371b014854d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('slug')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('slug', sa.VARCHAR(length=255), nullable=True))

    # ### end Alembic commands ###
