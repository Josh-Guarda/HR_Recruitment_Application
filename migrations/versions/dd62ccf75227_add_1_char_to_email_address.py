"""add 1 char to email_address

Revision ID: dd62ccf75227
Revises: 509b39185a41
Create Date: 2025-07-19 01:57:40.213754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd62ccf75227'
down_revision = '509b39185a41'
branch_labels = None
depends_on = None



def upgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_constraint('email_address', type_='unique')
        # You can recreate the column without unique if needed
        # batch_op.alter_column('email_address', existing_type=sa.String(length=50), unique=False)

def downgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.create_unique_constraint('email_address', ['email_address'])

    # ### end Alembic commands ###
