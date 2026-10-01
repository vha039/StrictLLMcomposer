# Queue — run r20260923-152510-4571ea

Derived 2026-09-23T15:25:18Z. This view is disposable and regenerable; it is never authoritative.

## Counts

- approved opportunities: 2  (core 2, exception 0)
- semantic final available: 1
- triage: READY 0, CHECK 1, RERUN 0
- render: OK 0, DEGRADED 1, FAILED 0, not rendered 1
- blocked 0, failed 1, stale 0, not started 0

## Failed - mechanically invalid, recovery available

- **annen_etat_analytiker** — Annen Etat, Analytiker [NORMAL]
  - production: FAILED · stage: - · triage: - · render: NOT_RENDERED
  - action: Repair and revalidate: strategy.

## Check - bounded local confirmation or edit

- **testetaten_radgiver** — Testetaten HF, Rådgiver økonomi og analyse [HIGH · frist 2026-09-15]
  - production: VALID · stage: FINAL · triage: CHECK · render: DEGRADED
  - action: Utlysningen nevner prognosearbeid; pakken dekker det bare indirekte. Action: Bekreft om prognoseerfaringen er sterk nok til å nevnes. | Kontaktperson og frist er ikke omtalt i brevet. Action: Vurder én setning om frist dersom det er ønskelig. | Known limitation: Ingen dokumentert erfaring med prognosemodeller ut over budsjettarbeid.
  - render: Save/export the PDF manually for human submission use. Automated status remains DEGRADED unless the configured converter later produces a verified current PDF.
  - output: `CV_Testetaten_HF_Radgiver_okonomi_og_analyse.docx`
  - output: `Soknad_Testetaten_HF_Radgiver_okonomi_og_analyse.docx`
