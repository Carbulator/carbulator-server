"""empty message

Revision ID: f0f8fe380410
Revises: 6ed4317c5750
Create Date: 2019-02-02 19:09:20.839947

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'f0f8fe380410'
down_revision = '6ed4317c5750'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('community_user_link', sa.Column('is_favourite', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('community_user_link', 'is_favourite')
    # ### end Alembic commands ###
