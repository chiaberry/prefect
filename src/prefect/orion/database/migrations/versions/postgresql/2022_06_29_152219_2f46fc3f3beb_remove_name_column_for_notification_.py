"""Remove name column for notification policies

Revision ID: 2f46fc3f3beb
Revises: 7296741dff68
Create Date: 2022-06-29 15:22:19.213787

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "2f46fc3f3beb"
down_revision = "7296741dff68"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("flow_run_notification_policy", schema=None) as batch_op:
        batch_op.drop_index("ix_flow_run_notification_policy__name")
        batch_op.drop_column("name")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("flow_run_notification_policy", schema=None) as batch_op:
        batch_op.add_column(sa.Column("name", sa.VARCHAR(), nullable=False))
        batch_op.create_index(
            "ix_flow_run_notification_policy__name", ["name"], unique=False
        )

    # ### end Alembic commands ###
