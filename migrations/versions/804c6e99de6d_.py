"""empty message

Revision ID: 804c6e99de6d
Revises: 82c0490e95b5
Create Date: 2020-04-02 21:53:52.966426

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '804c6e99de6d'
down_revision = '82c0490e95b5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    op.execute('UPDATE todos SET completed = False WHERE completed IS NULL;')
    op.alter_column('todos', 'completed', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
