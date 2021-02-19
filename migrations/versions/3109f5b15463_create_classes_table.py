"""create classes table"""

from alembic import op
import sqlalchemy as sa


# revision identifiers.
revision = '3109f5b15463'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default='now()'),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default='now()')
    )


def downgrade():
    op.drop_table('classes')
