"""empty message

Revision ID: efd57aeb49ff
Revises: aa13b64ce22f
Create Date: 2024-05-03 17:32:29.084986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd57aeb49ff'
down_revision = 'aa13b64ce22f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.VARCHAR(length=80),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('characters', schema=None) as batch_op:
        batch_op.alter_column('age',
               existing_type=sa.VARCHAR(length=80),
               nullable=False)

    # ### end Alembic commands ###
