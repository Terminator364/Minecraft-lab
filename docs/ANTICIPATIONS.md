# Minecraft Lab — ANTICIPATIONS

## Project definition
An **anticipation** is one concrete, traceable pre-delivery test or scenario intended to catch a real user-visible failure before the installable reaches the phone.

It is NOT:
- a loop count with no semantic variation;
- a repeated identical assertion;
- a marketing number.

## Vehicle v0.3.0 gates
The current car candidate must satisfy:
1. pack structure and JSON parse;
2. BP↔RP dependency/version consistency;
3. entity is summonable but has no generic spawn egg;
4. dedicated placer item exists;
5. ground control exists;
6. rideable driver seat exists;
7. horse/saddle/taming/breeding/inventory/climbing mechanics are absent;
8. automatic step height is at most 1 pixel (0.0625 block);
9. car geometry, texture, wheel/steering animations resolve;
10. localized drive prompt resolves in FR and EN;
11. packaging is reproducible and includes both packs;
12. road policy matrix passes for flat/low-profile surfaces and rejects step-like terrain.

## Runtime truth
Static/simulation gates do not claim to replace the Minecraft client. The final Android check remains limited to physical rendering, touch feel, camera/seat feel, and device performance.
