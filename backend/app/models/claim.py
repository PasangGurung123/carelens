from datetime import date, datetime
from decimal import Decimal

from sqlalchemy import (
    Date,
    DateTime,
    ForeignKey,
    Numeric,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base


class Claim(Base):
    __tablename__ = "claims"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    claim_number: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
        index=True,
    )

    member_id: Mapped[int] = mapped_column(
        ForeignKey("members.id"),
        nullable=False,
        index=True,
    )

    provider_id: Mapped[int] = mapped_column(
        ForeignKey("providers.id"),
        nullable=False,
        index=True,
    )

    service_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(12, 2),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        default="PAID",
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    member = relationship(
        "Member",
        back_populates="claims",
    )

    provider = relationship(
        "Provider",
        back_populates="claims",
    )

    claim_lines = relationship(
        "ClaimLine",
        back_populates="claim",
        cascade="all, delete-orphan",
    )