# The Kindred Realms

Ten new Arcanea character proposals, each commissioned as an identity sheet and a cinematic story frame. The cast balances six welcoming companions, two protective guardians and two contained opponents. The exhibition is authorized for public review; every new story record remains a proposal.

- [Story and cast](STORY-BIBLE.md)
- [Character metadata](characters.json)
- [Exact visual identities and 20 prompts](visual-specs.json)
- [Agent review queue](review-queue.json)
- [Source, rights and registration contract](STORY-REGISTRATION.md)
- [Independent source review](review/independent-source-v1.json)
- [Independent image review](review/independent-visual-v1.json)
- [Verified twenty-asset production catalog](assets-production.json)
- [Forty stored original and web objects](media-receipt.json)
- [SHA-bound exhibition approvals](media-exhibition-approval.json)

Fictional source authority: `artifact_arcanean_library_fiction`, `frankxai/arcanean-library/content/proposals/firstlight-02`. Product consumer: `frankxai/arcanea-ai-app`, intended route `/gallery/firstlight-02`. Actual generation, media storage and deployment state must be read from their receipts; a commissioned image or route name is not a delivery receipt.

Review one named revision at a time. Preserve source commit, inspected file/image hashes, scope, findings and reviewer identity. Submit a new receipt through a pull request and reference it from the queue. Use the per-item `review-receipt.schema.json` for display/encounter review, or the aggregate `independent-source-review.schema.json` for source-level inspection. Pending entries do not imply a pass.

Display approval, lore acceptance and real tool authority are separate decisions. A successful fictional expedition is not evidence of a completed business campaign. Unreal rigs, animation and live-agent adapters remain production work until observed receipts demonstrate them.

The source catalog uses canonical `asset_id` values such as `arcanea.fl02.seli.hero.v1`, with a shorter `id` such as `fl02-seli-hero` as the presentation alias used by character `asset_ids` and image-review receipts. Character review targets use the registered `arcanea.fl02.<slug>` ID. The explicit `portable_character_ref` preserves compatibility with earlier `character:<slug>` proposal records.

All twenty original images passed independent exhibition review, and the media receipt records individual public HTTP and full SHA256 checks for twenty originals plus twenty WebP derivatives. Three continuity explorations remain visible in the catalog: Seli's cinematic scale, Kethr's pointed cinematic prop and Vessakar's occluded legs. These are approved exhibition notes, not accepted model/rig specifications. Aven also shares a name component with separate public proposal entries, which the character metadata records by source revision.
