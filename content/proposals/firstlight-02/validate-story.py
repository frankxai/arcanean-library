"""Validate proposal boundaries, consumer references and the frozen visual identity."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator

root = Path(__file__).parent
data = json.loads((root/'characters.json').read_text())
schema = json.loads((root/'characters.schema.json').read_text())
Draft202012Validator.check_schema(schema)
Draft202012Validator(schema).validate(data)
Draft202012Validator.check_schema(json.loads((root/'review-receipt.schema.json').read_text()))
source_schema_path=root/'independent-source-review.schema.json'
if source_schema_path.exists():
    source_schema=json.loads(source_schema_path.read_text())
    Draft202012Validator.check_schema(source_schema)
    receipt=root/'review/independent-source-v1.json'
    if receipt.exists():
        Draft202012Validator(source_schema).validate(json.loads(receipt.read_text()))
specs = {s['id']:s for s in json.loads((root/'visual-specs.json').read_text())['specs']}
prior = set(data['collision_check']['previous_character_names'])
names,ids,assets = set(),set(),set()
for c in data['characters']:
    slug=c['slug']
    assert c['name'] not in prior and c['name'] not in names, c['name']
    assert c['id'] == f'arcanea.fl02.{slug}' and c['character_id']==f'character:{slug}'
    assert c['id'] not in ids
    assert c['visual']['locked_identity']==specs[slug]['identity'], slug
    assert c['title']==specs[slug]['title'], slug
    assert set(c['asset_ids'])=={f'fl02-{slug}-sheet',f'fl02-{slug}-hero'}
    names.add(c['name']);ids.add(c['id']);assets.update(c['asset_ids'])
assert len(assets)==20
queue=json.loads((root/'review-queue.json').read_text())
assert {x['target_id'] for x in queue['items']}=={c['id'] for c in data['characters']}
assert {a for x in queue['items'] for a in x['asset_ids']}==assets
for item in queue['items']:
    assert item['state'] in ['pending','reviewed','needs_revision','rejected','deferred']
    if item['state']=='pending':
        assert item['decision'] is None and item['reviewer_id'] is None
    else:
        assert isinstance(item['reviewer_id'],str) and len(item['reviewer_id']) >= 3
        assert item['decision'] in queue['review_contract']['decision_values']
        assert item['evidence_refs'], 'A decision requires an independent review receipt.'
catalog_path=root/'assets-production.json'
if catalog_path.exists():
    catalog=json.loads(catalog_path.read_text())
    media=json.loads((root/'media-receipt.json').read_text())
    rows={r['id']:r for r in catalog['assets']}
    objects={(o['asset_id'],o['rendition']):o for o in media['files']}
    assert set(rows)==assets and len(objects)==40
    for alias,row in rows.items():
        assert row['canon_state']=='proposal'
        assert row['character_id'] in ids
        assert row['derived_from_sha256']==row['master_sha256']
        for variant,url,sha in [('master',row['original_url'],row['master_sha256']),('web',row['url'],row['sha256'])]:
            obj=objects[(alias,variant)]
            assert obj['url']==url and obj['sha256']==sha and obj['verified_sha256']==sha
            assert obj['verified_public_http_status']==200
        assert row['exhibition_release']['canon_acceptance'] is False
        assert row['exhibition_release']['state']=='approved'
print('Validated: 10 distinct character proposals, 20 consistent asset IDs, frozen identity alignment, 6/2/2 cast, review queue targets and evidence-bound review states.')
