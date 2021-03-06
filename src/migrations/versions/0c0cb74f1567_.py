"""empty message

Revision ID: 0c0cb74f1567
Revises: f630edffbf2b
Create Date: 2018-11-30 13:42:04.619879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c0cb74f1567'
down_revision = 'f630edffbf2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('reset_password_hash_created', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'reset_password_hash_created')
    # ### end Alembic commands ###
