#!/usr/bin/env python3
"""ERCOT large-load exposure calculator.

Source: PUCT Project 58481, Proposal for Publication filed 2026-03-12,
proposed 16 TAC 25.194 subsections (d)(9), (d)(10), (g), (h).
observed_date: 2026-08-20

PROPOSED RULE, NOT FINAL. Confirm adoption before client use.
Stdlib only. No network. No fabricated inputs: costs_incurred has no default
because the rule does not supply one -- it is deal-specific and must be given.
"""
import argparse, sys

SECURITY_PER_MW = 50_000          # 25.194(d)(10)
STUDY_FEE_UNDER_250 = 100_000     # 25.194(d)(9)(A)
STUDY_FEE_250_PLUS = 300_000      # 25.194(d)(9)(B)
APPLICABILITY_MW = 75             # 25.194(b)
REFUND_SHARE = 0.20               # 25.194(g)(3)
RATEBASE_SHARE = 0.80             # 25.194(g)(4)


def study_fee(mw):
    return STUDY_FEE_250_PLUS if mw >= 250 else STUDY_FEE_UNDER_250


def exposure(mw, costs_incurred, ciac=0):
    """Return the exposure breakdown. costs_incurred is REQUIRED (deal-specific)."""
    if mw < APPLICABILITY_MW:
        return {"applicable": False,
                "note": f"{mw} MW is below the {APPLICABILITY_MW} MW threshold of 25.194(b)"}
    security = mw * SECURITY_PER_MW
    fee = study_fee(mw)
    balance = max(0.0, security - costs_incurred)
    refund = balance * REFUND_SHARE
    ratebase = balance * RATEBASE_SHARE
    drawn = min(security, costs_incurred)
    return {
        "applicable": True,
        "mw": mw,
        "security_posted": security,
        "study_fee_minimum": fee,
        "ciac_non_refundable": ciac,          # 25.194(g)(5)
        "costs_incurred_input": costs_incurred,
        "security_drawn_down": drawn,
        "balance_after_drawdown": balance,
        "refunded_to_customer": refund,
        "retained_to_tsp_ratebase": ratebase,
        "net_loss": security + fee + ciac - refund,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("mw", type=float, help="requested peak demand, MW")
    p.add_argument("--costs-incurred", type=float, required=True,
                   help="REQUIRED. DSP/TSP outstanding amounts owed at withdrawal, $. "
                        "Deal-specific; the rule supplies no default.")
    p.add_argument("--ciac", type=float, default=0.0,
                   help="contributions in aid of construction paid, $ (non-refundable)")
    a = p.parse_args()
    if a.costs_incurred < 0 or a.ciac < 0:
        sys.exit("costs and CIAC must be non-negative")
    r = exposure(a.mw, a.costs_incurred, a.ciac)
    if not r["applicable"]:
        print(r["note"]); return
    w = max(len(k) for k in r if k != "applicable")
    print(f"\n16 TAC 25.194 exposure -- {a.mw:,.0f} MW  (PROPOSED RULE)\n")
    for k, v in r.items():
        if k in ("applicable", "mw"):
            continue
        print(f"  {k.replace('_',' '):<{w}}  ${v:>14,.0f}")
    print("\n  25.194(h): missing a phased-energization milestone by 6 months triggers")
    print("  the same drawdown WITHOUT a withdrawal.\n")


if __name__ == "__main__":
    main()
