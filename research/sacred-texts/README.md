# Sacred Texts Research Corpus

Sacred Texts is the provenance layer beneath the Arcanean Library. It preserves
primary witnesses, original-language texts, edition facts, rights decisions,
and precise passage locators. It is not itself Arcanea scripture.

## The contract

Every item must remain visibly one of four things:

1. **Source** — a primary text or documentary witness.
2. **Translation** — a named translator's accountable rendering.
3. **Interpretation** — attributed scholarship or editorial argument.
4. **Synthesis** — new Starlight or Arcanea writing, never presented as ancient,
   revealed, or spoken by a historical figure.

No file may silently cross those boundaries.

## Repository topology

```text
research/sacred-texts/
├── CANON.md                         # epistemic and editorial boundaries
├── RIGHTS.md                        # ingestion and quotation gate
├── ledgers/source-ledger.jsonl      # one provenance decision per source
├── originals/                       # verified original-language witnesses
├── registry/                        # thinkers, works, themes, priorities
└── schemas/source-record.schema.json

collections/sacred-visions/          # curated experience built from the corpus
content/                             # original Arcanea codices and scripture
```

## Ingestion gate

A text enters `originals/` only when all of the following are recorded:

- author and stable work identifier;
- original language;
- exact source URL and edition or manuscript basis;
- whether the transcription is diplomatic, normalized, critical, or liturgical;
- rights status for the underlying work, edition, transcription, annotations,
  and any translation;
- capture scope (`full`, `excerpt`, or `locator-only`);
- verification status and reviewer.

An attractive quotation without a traceable edition remains a lead, not a
source.

## Christian foundation wave

The first registry covers Augustine, Thomas Aquinas, Meister Eckhart, Teresa of
Ávila, John of the Cross, Blaise Pascal, Søren Kierkegaard, Simone Weil, and
Thomas Merton. It begins with four original-language specimens whose textual
status is stated in the file rather than concealed:

- Augustine, *Confessiones* I.1 (Latin excerpt)
- Thomas Aquinas, *Pange lingua gloriosi Corporis mysterium* (Latin hymn)
- Teresa of Ávila, *Ya toda me entregué y di* (Spanish poem)
- John of the Cross, *Noche oscura* (Spanish poem)

The registry is deliberately broader than the first ingest. Full-text capture
is earned work: edition by edition, rights decision by rights decision.

## Next expansion sequence

1. Complete the public-domain original-language poetry of Teresa and John.
2. Add passage witnesses for Augustine, Aquinas, Eckhart, Pascal, and
   Kierkegaard.
3. Keep Simone Weil edition-aware and Thomas Merton locator-only until the
   relevant rights are resolved.
4. Add biblical Hebrew, Greek, Syriac, and Latin poetic witnesses before using
   modern translations.
5. Expand tradition by tradition—Jewish, Islamic and Sufi, Hindu, Buddhist,
   Sikh, Jain, Daoist, and responsibly governed oral traditions—without
   collapsing their incompatible claims into generic mysticism.

## Quality rule

Beauty is a selection criterion. Fidelity is the admission criterion.

