# Minecraft Lab — Cahier des charges canonique A+B+C

## A — Origine, promesse et produit attendu
A contient ce qui a été demandé avant toute recherche ou implémentation. Ce sont les invariants produit.

### A-P0-001 — Installation fluide
L'utilisateur doit installer le produit via un seul fichier `.mcaddon` ouvrable avec Minecraft. Aucun passage manuel dans une archive ZIP n'est accepté.

### A-P0-002 — Objet visible et identifiable
Le véhicule doit être trouvable dans l'inventaire créatif par son nom, avoir une icône réellement visible et reconnaissable, et pouvoir être placé sans commande de triche.

### A-P0-003 — Véhicule réellement utilisable
Le véhicule doit être montable, contrôlable sur mobile et se comporter comme un véhicule, pas comme un cheval/mob recyclé.

### A-P0-004 — Visibilité conducteur exploitable
Le joueur doit voir l'environnement en conduite sans que la carrosserie, le toit, le tableau de bord ou le siège masquent l'essentiel du champ de vision.

### A-P0-005 — Variante 4x4
La variante 4x4 doit franchir les reliefs ordinaires du terrain Minecraft, notamment les transitions d'un bloc et les monticules progressifs, sans devenir un grimpeur de murs verticaux.

### A-P0-006 — Réemploi avant invention
Avant de construire un sous-système, rechercher et qualifier les implémentations existantes utilisables légalement. Classer chaque piste REUSE / ADAPT / REFERENCE_ONLY / REJECT.

### A-P0-007 — Traçabilité
Toute ressource réutilisée doit conserver auteur, source, licence et portée d'intégration. Les inspirations non réutilisables restent REFERENCE_ONLY.

### A-P0-008 — Anticipations utiles
Une anticipation n'est comptée que si elle couvre une exigence précise, possède un scénario distinct, un oracle explicite et une preuve. Les répétitions combinatoires sans nouvelle propriété couverte ne comptent pas comme progrès.

### A-P0-009 — Release gate
Une candidate ne peut être appelée READY que lorsque tous les P0 ont une preuve adaptée. Une preuve statique ne peut pas être utilisée pour déclarer une exigence visuelle ou tactile comme validée.

## B — Recherche, sources et approfondissement technique
B contient les sources officielles et communautaires, les architectures existantes, les licences, les expériences antérieures et les décisions REUSE/ADAPT/REFERENCE_ONLY.

Chaque entrée B doit contenir :
- source et auteur ;
- licence ;
- version Bedrock ciblée ;
- fonction étudiée ;
- défauts connus ;
- décision d'adoption ;
- fichiers réellement importés, s'il y en a ;
- exigences A qu'elle aide à satisfaire.

## C — Retours terrain, corrections et exigences accumulées
C transforme chaque retour téléphone en exigence ou contre-exemple durable. Aucun écart observé ne doit être effacé par une nouvelle version.

### C-001 — V0.1 : UX de monture/cheval inacceptable
### C-002 — V0.1/V0.2 : véhicule trop routier pour le besoin 4x4
### C-003 — V0.3 : objet absent de la recherche créative
### C-004 — V0.3/V0.4 : icône invisible malgré présence de l'item
### C-005 — V0.3/V0.4 : visibilité conducteur insuffisante
### C-006 — V0.4 : packaging séparé .mcpack/.zip inacceptable
### C-007 — V0.4 : installation en un seul .mcaddon validée comme bon flux UX

## Règle de fusion A+B+C
Toute nouvelle version doit :
1. repartir du cahier courant ;
2. préserver les A encore actifs ;
3. intégrer les B retenus sans perdre la provenance ;
4. convertir les C en exigences/gates ;
5. marquer explicitement SUPERSEDED ce qui est remplacé ;
6. ne jamais reclasser une exigence en PASS sans nouvelle preuve.

## États autorisés
- UNTESTED
- STATIC_PASS
- RUNTIME_PASS
- VISUAL_PASS
- DEVICE_PASS
- PARTIAL
- FAIL
- BLOCKED_EXTERNAL
- SUPERSEDED

## Règle de vérité
Le niveau d'une preuve doit correspondre à l'exigence :
- structure/manifest/licence -> STATIC_PASS possible ;
- comportement moteur -> RUNTIME_PASS requis ;
- icône/rendu/caméra -> VISUAL_PASS requis ;
- toucher/sensation/FPS réel -> DEVICE_PASS requis.
