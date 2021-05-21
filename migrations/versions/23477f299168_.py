"""empty message

Revision ID: 23477f299168
Revises: 2ad7061ceb8a
Create Date: 2021-05-21 15:46:25.913432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23477f299168'
down_revision = '2ad7061ceb8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('video', sa.Column('available_inventory', sa.Integer(), nullable=True))
    op.alter_column('video', 'total_inventory',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('video', 'total_inventory',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('video', 'available_inventory')
    # ### end Alembic commands ###