"""rename_classes_to_courses"""

from alembic import op
import sqlalchemy as sa


# revision identifiers.
revision = 'f3b2df3c575b'
down_revision = '3109f5b15463'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('classes', 'courses')


def downgrade():
    op.rename_table('courses', 'classes')
