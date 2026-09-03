from datetime import date
from decimal import Decimal
from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[1]
BACKEND_PATH = PROJECT_ROOT / "backend"

sys.path.insert(0, str(BACKEND_PATH))


from app.core.database import SessionLocal
from app.models import (
    Claim,
    ClaimLine,
    Member,
    Organization,
    Procedure,
    Provider,
)


def seed_database() -> None:
    db = SessionLocal()

    try:
        organization = Organization(
            name="CareLens Demo Health Plan",
        )

        db.add(organization)
        db.flush()

        members = [
            Member(
                member_number="M10001",
                first_name="John",
                last_name="Smith",
                date_of_birth=date(1985, 5, 20),
                organization_id=organization.id,
            ),
            Member(
                member_number="M10002",
                first_name="Sarah",
                last_name="Wilson",
                date_of_birth=date(1990, 8, 12),
                organization_id=organization.id,
            ),
        ]

        db.add_all(members)

        providers = [
            Provider(
                provider_number="P20001",
                name="City Medical Center",
                specialty="Primary Care",
                organization_id=organization.id,
            ),
            Provider(
                provider_number="P20002",
                name="Mountain Cardiology",
                specialty="Cardiology",
                organization_id=organization.id,
            ),
        ]

        db.add_all(providers)

        procedures = [
            Procedure(
                code="99213",
                description="Established patient office visit",
            ),
            Procedure(
                code="99214",
                description="Established patient office visit - moderate complexity",
            ),
            Procedure(
                code="80053",
                description="Comprehensive metabolic panel",
            ),
        ]

        db.add_all(procedures)

        db.flush()

        claim = Claim(
            claim_number="C30001",
            member_id=members[0].id,
            provider_id=providers[0].id,
            service_date=date(2026, 1, 15),
            total_amount=Decimal("275.00"),
            status="PAID",
        )

        db.add(claim)
        db.flush()

        claim_line_1 = ClaimLine(
            claim_id=claim.id,
            procedure_id=procedures[0].id,
            quantity=1,
            amount=Decimal("150.00"),
        )

        claim_line_2 = ClaimLine(
            claim_id=claim.id,
            procedure_id=procedures[2].id,
            quantity=1,
            amount=Decimal("125.00"),
        )

        db.add_all(
            [
                claim_line_1,
                claim_line_2,
            ]
        )

        db.commit()

        print("Database seeded successfully.")

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()