# Story registration and review

This packet is fictional Arcanea material owned by the existing Arcanean Library authority. It is a public design exhibition proposal, with no accepted-canon state change. The product gallery renders a projection of the packet.

Canonical placement: `frankxai/arcanean-library/content/proposals/firstlight-02`.
Product consumer: `frankxai/arcanea-ai-app`, `/gallery/firstlight-02`.

The character source is `characters.json`; the exact frozen visual briefs and prompts are `visual-specs.json`. Every character has one identity sheet and one cinematic story frame. The asset manifest records actual generated files and their hashes; an intended asset ID alone is not evidence of generation or deployment.

The ten stable dossier IDs use `arcanea.fl02.<slug>`. Existing portable runtime-compatible character references use `character:<slug>`. Asset IDs use `fl02-<slug>-sheet` and `fl02-<slug>-hero`. A display approval does not bind an agent to a runtime, grant a capability or accept fictional canon.

Reviewers submit their own receipts by pull request. Pin the source commit and inspected image SHA256s; use `review-receipt.schema.json` for committed receipts. Local pre-commit reviews may use explicit file SHA256s and must say the target is uncommitted. Retain all blocking findings until the named revision is inspected. Do not infer a pass from an empty queue or an absent reviewer.

The independent aggregate source review uses `independent-source-review.schema.json`. It preserves exact source hashes and may cover several source-level lenses. Its image hashes remain null when the visual outputs are outside its inspected scope; that is not an image-review pass. The per-item review schema remains the contract for later image and encounter decisions.

The independent review queue is `review-queue.json`. New canon can be accepted only by a separate explicit owner/canon decision. Public display of a proposal, a successful build and a generated image do not constitute that decision.

Validation covers cast balance, source boundaries, identity locks, prior-name collisions within the named sources, all 20 asset references, and review target consistency. Install `jsonschema==4.26.0`, then run `python validate-story.py` beside the packet. This does not test rendered images, browser layout, Unreal assets or live-agent execution.

Current rights policy: Frank Riemer, all rights reserved under the repository LICENSE and LICENSING.md. The generation record is provenance, not proof of exclusivity or a registered right.
