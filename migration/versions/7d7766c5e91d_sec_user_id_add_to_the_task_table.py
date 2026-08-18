"""sec user_id add to the task table

Revision ID: 7d7766c5e91d
Revises: de6bc81fb320
Create Date: 2026-08-12 19:21:11.736586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7d7766c5e91d'
down_revision: Union[str, Sequence[str], None] = 'de6bc81fb320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()

    # 1) add column as nullable so old rows don't fail
    op.add_column('user_tasks', sa.Column('user_id', sa.Integer(), nullable=True))

    # 2) make sure there is at least one user in the users table
    user_count = bind.execute(sa.text("SELECT COUNT(*) FROM user_table")).scalar()
    if user_count == 0:
        raise RuntimeError(
            "Cannot migrate user_tasks: user_table is empty. Create at least one user first."
        )

    # 3) assign a valid user_id to existing tasks
    bind.execute(sa.text("""
        UPDATE user_tasks
        SET user_id = (
            SELECT id
            FROM user_table
            ORDER BY id
            LIMIT 1
        )
        WHERE user_id IS NULL
    """))

    # 4) enforce the foreign key and not-null rule
    op.alter_column('user_tasks', 'user_id', existing_type=sa.Integer(), nullable=False)
    op.create_foreign_key(
        'fk_user_tasks_user_id',
        'user_tasks',
        'user_table',
        ['user_id'],
        ['id'],
        ondelete='CASCADE'
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('fk_user_tasks_user_id', 'user_tasks', type_='foreignkey')
    op.drop_column('user_tasks', 'user_id')
