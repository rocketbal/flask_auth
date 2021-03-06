"""empty message

Revision ID: d593bc7ca3e1
Revises: e61b89d8f811
Create Date: 2021-09-18 15:55:56.162044

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd593bc7ca3e1'
down_revision = 'e61b89d8f811'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###
