from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
publications = Table('publications', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('abstract', VARCHAR(length=128)),
    Column('teaser_image_path', VARCHAR(length=128)),
    Column('authors', VARCHAR(length=64)),
    Column('link_pdf1', VARCHAR(length=64)),
    Column('link_pdf2', VARCHAR(length=64)),
    Column('link_video', VARCHAR(length=64)),
    Column('link_source', VARCHAR(length=64)),
    Column('link_url', VARCHAR(length=64)),
    Column('link_etc', VARCHAR(length=64)),
    Column('conference', VARCHAR(length=128)),
    Column('date', VARCHAR(length=128)),
)

publications = Table('publications', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('description', String(length=128)),
    Column('abstract', String(length=128)),
    Column('year', Integer),
    Column('teaser_image_path', String(length=128)),
    Column('authors', String(length=64)),
    Column('link_pdf1', String(length=64)),
    Column('link_pdf2', String(length=64)),
    Column('link_video', String(length=64)),
    Column('link_source', String(length=64)),
    Column('link_url', String(length=64)),
    Column('link_etc', String(length=64)),
    Column('is_activated', Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['publications'].columns['conference'].drop()
    pre_meta.tables['publications'].columns['date'].drop()
    post_meta.tables['publications'].columns['description'].create()
    post_meta.tables['publications'].columns['is_activated'].create()
    post_meta.tables['publications'].columns['year'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['publications'].columns['conference'].create()
    pre_meta.tables['publications'].columns['date'].create()
    post_meta.tables['publications'].columns['description'].drop()
    post_meta.tables['publications'].columns['is_activated'].drop()
    post_meta.tables['publications'].columns['year'].drop()