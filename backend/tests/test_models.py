from sqlalchemy import inspect

from app.core.database import engine


def test_required_tables_exist():
    inspector = inspect(engine)

    tables = set(inspector.get_table_names())

    expected_tables = {
        "organizations",
        "members",
        "providers",
        "procedures",
        "claims",
        "claim_lines",
    }

    assert expected_tables.issubset(tables)