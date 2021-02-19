"""create admin table """
from alembic import op
import sqlalchemy as sa


# revision identifiers
revision = '6058f666ef8a'
down_revision = 'f3b2df3c575b'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'admin',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('eid', sa.String, nullable=False),
        sa.Column('e-mail', sa.String(255), nullable=False, unique=True),
        sa.Column('phone', sa.String(30), nullable=False),
        sa.Column('gen', sa.String(30), nullable=False),
        sa.Column('cls', sa.String(30), nullable=False),
        sa.Column('Adr', sa.String(30), nullable=False),
        sa.Column('bgr', sa.String(30), nullable=False),
        sa.Column('fname', sa.String(30), nullable=False),
        sa.Column('mname', sa.String(30), nullable=False),
        sa.Column('dob', sa.String(30), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default='now()'),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default='now()')
    )


def downgrade():
    op.drop_table('admin')
