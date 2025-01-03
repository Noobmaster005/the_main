"""Add hotel_id to rooms

Revision ID: 098dacad9cd3
Revises: 6c94046e9f0b
Create Date: 2025-01-02 15:28:28.140277

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "098dacad9cd3"
down_revision: Union[str, None] = "6c94046e9f0b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("rooms_hotels_id_fkey", "rooms", type_="foreignkey")
    op.drop_column("rooms", "hotels_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "rooms",
        sa.Column("hotels_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.create_foreign_key(
        "rooms_hotels_id_fkey", "rooms", "hotels", ["hotels_id"], ["id"]
    )
    # ### end Alembic commands ###