"""add name column on datasets table

Revision ID: cbf947ca88d7
Revises: c0aea6931214
Create Date: 2019-10-17 00:15:11.304818

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbf947ca88d7'
down_revision = 'c0aea6931214'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('datasets', sa.Column('name', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('datasets', 'name')
    # ### end Alembic commands ###