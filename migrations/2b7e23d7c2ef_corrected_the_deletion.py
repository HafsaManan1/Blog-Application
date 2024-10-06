"""corrected the deletion

Revision ID: 2b7e23d7c2ef
Revises: fc74da294b81
Create Date: 2024-09-27 12:33:42.267723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b7e23d7c2ef'
down_revision = 'fc74da294b81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
