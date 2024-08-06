"""temat

Revision ID: a518fd56c2a4
Revises: 4f81e6a5d83b
Create Date: 2024-08-06 21:44:49.196391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a518fd56c2a4'
down_revision = '4f81e6a5d83b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sprawa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('temat', sa.String(), nullable=True))
        batch_op.drop_column('kategoria')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sprawa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('kategoria', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('temat')

    # ### end Alembic commands ###
