"""add email to student

Revision ID: 2f7a120c97a6
Revises: 
Create Date: 2026-04-08 18:38:39.568041
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2f7a120c97a6'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Upgrade schema."""
    # Add email column only (no unique constraint for SQLite)
    op.add_column('students', sa.Column('email', sa.String(), nullable=True))

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('students', 'email')