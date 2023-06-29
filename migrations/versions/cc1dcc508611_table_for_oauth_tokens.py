"""Table for oauth tokens

Revision ID: cc1dcc508611
Revises: 7a3e336c0fba
Create Date: 2023-06-29 07:57:22.861763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc1dcc508611'
down_revision = '7a3e336c0fba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('oauth_tokens',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('toolkit_id', sa.Integer(), nullable=True),
    sa.Column('key', sa.String(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_index('ix_agent_execution_permissions_agent_execution_id', table_name='agent_execution_permissions')
    op.drop_index('ix_atc_agnt_template_id_key', table_name='agent_template_configs')
    op.drop_index('ix_agt_agnt_name', table_name='agent_templates')
    op.drop_index('ix_agt_agnt_organisation_id', table_name='agent_templates')
    op.drop_index('ix_agt_agnt_workflow_id', table_name='agent_templates')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_agt_agnt_workflow_id', 'agent_templates', ['agent_workflow_id'], unique=False)
    op.create_index('ix_agt_agnt_organisation_id', 'agent_templates', ['organisation_id'], unique=False)
    op.create_index('ix_agt_agnt_name', 'agent_templates', ['name'], unique=False)
    op.create_index('ix_atc_agnt_template_id_key', 'agent_template_configs', ['agent_template_id', 'key'], unique=False)
    op.create_index('ix_agent_execution_permissions_agent_execution_id', 'agent_execution_permissions', ['agent_execution_id'], unique=False)
    op.drop_table('oauth_tokens')
    # ### end Alembic commands ###
