"""baseline

Revision ID: 88311937f7b6
Revises: 
Create Date: 2019-10-16 18:03:41.212329

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '88311937f7b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('user_id', UUID(as_uuid=True), primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('chosen_decimal', sa.Numeric(16,8), nullable=False),
        sa.Column('dob', sa.DateTime, nullable=False),
    )


def downgrade():
    op.drop_table('users')
