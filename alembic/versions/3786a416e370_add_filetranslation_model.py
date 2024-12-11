"""Add FileTranslation model

Revision ID: 3786a416e370
Revises: c8c52a8d6a0f
Create Date: 2024-12-11 12:46:43.033770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3786a416e370'
down_revision: Union[str, None] = 'c8c52a8d6a0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('file_translations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('input_file_id', sa.String(), nullable=True),
    sa.Column('output_file_id', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('INIT', 'FAILED', 'PROCESSED', name='filestatus'), nullable=True),
    sa.Column('total_lines', sa.Integer(), nullable=True),
    sa.Column('price_unit', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('file_translations')
    # ### end Alembic commands ###