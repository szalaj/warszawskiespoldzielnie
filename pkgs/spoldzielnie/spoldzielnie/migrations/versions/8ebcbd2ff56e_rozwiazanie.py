"""rozwiazanie

Revision ID: 8ebcbd2ff56e
Revises: e852efa2a2d8
Create Date: 2024-03-17 10:48:19.101095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ebcbd2ff56e'
down_revision = 'e852efa2a2d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sprawa', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rozwiazanie', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sprawa', schema=None) as batch_op:
        batch_op.drop_column('rozwiazanie')

    # ### end Alembic commands ###