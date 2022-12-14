"""todos table

Revision ID: 564603cbb439
Revises: 5ddf97a1df22
Create Date: 2022-11-17 22:50:15.771852

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '564603cbb439'
down_revision = '5ddf97a1df22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.String(length=10000), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_todo_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('todo', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_todo_timestamp'))

    op.drop_table('todo')
    # ### end Alembic commands ###
