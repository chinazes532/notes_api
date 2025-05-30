"""empty message

Revision ID: 37b9ed478489
Revises: c4b9d4eec3fc
Create Date: 2025-04-10 18:03:57.033953

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37b9ed478489'
down_revision: Union[str, None] = 'c4b9d4eec3fc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.add_column('notes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'notes', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'notes', type_='foreignkey')
    op.drop_column('notes', 'user_id')
    op.drop_table('users')
    # ### end Alembic commands ###
