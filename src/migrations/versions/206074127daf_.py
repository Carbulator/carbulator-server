"""empty message

Revision ID: 206074127daf
Revises: 84e4b31bc2db
Create Date: 2018-12-15 14:29:56.129617

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '206074127daf'
down_revision = '84e4b31bc2db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_instances', sa.Column('community_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'task_instances', 'communities', ['community_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task_instances', type_='foreignkey')
    op.drop_column('task_instances', 'community_id')
    # ### end Alembic commands ###
