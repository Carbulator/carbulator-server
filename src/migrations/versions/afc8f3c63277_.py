"""empty message

Revision ID: afc8f3c63277
Revises: 206074127daf
Create Date: 2018-12-25 08:30:13.803079

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'afc8f3c63277'
down_revision = '206074127daf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task_instances', sa.Column('time_finished', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('task_instances', 'time_finished')
    # ### end Alembic commands ###