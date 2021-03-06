"""Added propper login model, fixed legacy column

Revision ID: 0650b30b287f
Revises: 646bb7420889
Create Date: 2019-12-19 13:44:19.831621

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0650b30b287f'
down_revision = '646bb7420889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item', 'person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item', sa.Column('person', mysql.TEXT(collation='utf8mb4_unicode_ci'), nullable=False))
    # ### end Alembic commands ###
