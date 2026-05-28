"""add document permissions

Revision ID: 0002_document_permissions
Revises: 0001_baseline_schema
Create Date: 2026-05-28
"""

from alembic import op
import sqlalchemy as sa

revision = "0002_document_permissions"
down_revision = "0001_baseline_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "document_permissions",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("document_id", sa.Integer(), nullable=False),
        sa.Column("subject_type", sa.String(length=16), nullable=False),
        sa.Column("subject_id", sa.String(length=128), nullable=False),
        sa.Column("effect", sa.String(length=16), nullable=False, server_default="allow"),
        sa.Column("action", sa.String(length=16), nullable=False, server_default="read"),
        sa.ForeignKeyConstraint(["document_id"], ["documents.id"], ondelete="CASCADE"),
    )
    op.create_index(
        "ix_document_permissions_document_subject",
        "document_permissions",
        ["document_id", "subject_type", "subject_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_document_permissions_document_subject", table_name="document_permissions")
    op.drop_table("document_permissions")
