"""Fake checkout configuration for the demo shop."""
from __future__ import annotations

import os


def load_payment_config() -> dict[str, str]:
    key = os.getenv("SHOP_PAYMENT_KEY")
    if key is None:
        raise RuntimeError("Missing payment key")
    return {"payment_key": key}
