"""baseline schema

Revision ID: 0001_baseline_schema
Revises:
Create Date: 2026-05-28
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "0001_baseline_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("role", sa.String(length=32), nullable=False, server_default="viewer"),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "collections",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
    )
    op.create_index("ix_collections_name", "collections", ["name"], unique=True)

    op.create_table(
        "documents",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("collection_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("content_type", sa.String(length=64), nullable=False, server_default="text/plain"),
        sa.Column("storage_path", sa.String(length=500), nullable=False),
        sa.ForeignKeyConstraint(["collection_id"], ["collections.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_documents_title", "documents", ["title"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_documents_title", table_name="documents")
    op.drop_table("documents")
    op.drop_index("ix_collections_name", table_name="collections")
    op.drop_table("collections")
    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")
