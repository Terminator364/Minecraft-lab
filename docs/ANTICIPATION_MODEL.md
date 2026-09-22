# Anticipations — modèle canonique

## Ce qui change
Le compteur brut "64 803 anticipations" n'est plus un indicateur de maturité. Il décrivait surtout une matrice combinatoire de scénarios et pouvait rester vert alors qu'une exigence majeure comme l'icône était fausse sur téléphone.

Dorénavant, on publie **deux métriques séparées** :

1. **Coverage** = combien d'exigences du cahier ont un oracle et une preuve adaptés.
2. **Scenario executions** = combien de scénarios distincts ont été exécutés.

Seule la première autorise une promotion.

## Schéma obligatoire d'une anticipation
Chaque anticipation doit porter :
- anticipation_id
- requirement_id
- source_requirement: A / B / C
- precondition
- action
- expected_result
- oracle
- evidence_class
- negative_control
- status
- proof_pointer

Exemple correct :

```json
{
  "anticipation_id": "ICON-001",
  "requirement_id": "A-P0-002",
  "source_requirement": ["A-P0-002","C-004"],
  "precondition": "pack installed and Creative inventory opened",
  "action": "search '4x4 Minecraft Lab'",
  "expected_result": "one visible item tile with non-empty car icon",
  "oracle": "Minecraft client visual render",
  "evidence_class": "DEVICE_PASS",
  "negative_control": "remove item_texture mapping => icon must fail",
  "status": "UNTESTED",
  "proof_pointer": null
}
```

## Classes d'oracle
- STATIC: structure, JSON, path, hash, licence.
- PACKAGE: archive finale relue après build.
- RUNTIME: comportement chargé/exécuté par moteur Bedrock/BDS.
- VISUAL: rendu généré ou capture analysée.
- DEVICE: comportement réel du client Android.
- NEGATIVE_CONTROL: mutation volontaire qui doit être détectée.

## Règle anti-inflation
100 variantes qui changent uniquement météo × vitesse × angle, mais vérifient la même propriété, sont une **famille d'anticipation** avec 100 exécutions, pas 100 nouveaux points de couverture.

## Gate de release
La release ne dépend pas de N anticipations. Elle dépend de :
- 100% des P0 couverts ;
- oracle approprié pour chaque P0 ;
- aucune preuve périmée ;
- aucun C ouvert non relié à une exigence ;
- contrôles négatifs actifs sur les défauts déjà rencontrés.
