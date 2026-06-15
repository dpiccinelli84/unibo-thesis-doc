#!/usr/bin/env python3
"""Trova ripetizioni (frasi quasi identiche e paragrafi ad alta sovrapposizione lessicale)
fra punti distinti della tesi. Output: coppie candidate con posizione (file:riga) e testo."""
import re, glob, itertools
from collections import defaultdict

FILES = sorted(glob.glob("chapters/0[0-6]*.tex"))

STOP = set("""
a ad al allo ai agli alla alle agli con col coi da dal dallo dai dagli dalla dalle di del
dello dei degli della delle in nel nello nei negli nella nelle su sul sullo sui sugli sulla
sulle per tra fra il lo la i gli le un uno una e ed o oppure ma se che chi cui non come piu
più meno molto poco anche pure ancora gia già sempre mai questo questa questi queste quello
quella quelli quelle suo sua suoi sue loro nostro nostra si ne ci vi lo la li le ce sono
essere stato stata stati state ha hanno avere viene vengono venga puo può possono deve devono
quando dove mentre quindi inoltre infine ovvero cioe cioè esempio es ad esso essa essi esse
fin dalla delle alle nelle sulle dei degli ogni tutto tutti tutte tutta solo sola anche
al fine modo punto caso casi sia siano due tre primo prima secondo terzo stesso stessa stesse
stessi base parte parti tramite attraverso rispetto presso senza presso entro circa
""".split())

def strip_latex(t):
    t = re.sub(r'(?<!\\)%.*', '', t)                 # commenti
    t = re.sub(r'\\(label|ref|autoref|cref|Cref|cite|includegraphics|input|footnotetext|footnote)\*?(\[[^\]]*\])?\{[^}]*\}', ' ', t)
    t = re.sub(r'\$[^$]*\$', ' ', t)                 # math
    t = re.sub(r'\\(begin|end)\{[^}]*\}', ' ', t)    # ambienti
    t = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', ' ', t)  # comandi
    t = re.sub(r'[{}\\~^&]', ' ', t)
    t = t.replace("``", '"').replace("''", '"')
    return t

# paragrafi con riga di partenza
paras = []  # (file, line, raw_para)
for f in FILES:
    lines = open(f, encoding="utf-8").read().split("\n")
    buf, start = [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip() == "":
            if buf:
                paras.append((f, start, " ".join(buf))); buf, start = [], None
        else:
            if start is None: start = i
            buf.append(ln)
    if buf: paras.append((f, start, " ".join(buf)))

# frasi
SENT = []  # (file, line, norm_words(tuple), display)
for f, line, raw in paras:
    txt = strip_latex(raw)
    for s in re.split(r'(?<=[.!?:;])\s+', txt):
        s = s.strip()
        words = re.findall(r"[a-zA-ZàèéìíòóùúÀÈÉÌÒÙ']+", s.lower())
        content = [w for w in words if w not in STOP and len(w) > 2]
        if len(content) >= 6:
            SENT.append((f, line, tuple(words), tuple(content), s.strip()))

def ngrams(seq, n):
    return set(tuple(seq[i:i+n]) for i in range(len(seq)-n+1)) if len(seq) >= n else set()

def jacc(a, b):
    a, b = set(a), set(b)
    return len(a & b) / len(a | b) if a | b else 0

near_literal, paraphrase = [], []
for (i, A), (j, B) in itertools.combinations(enumerate(SENT), 2):
    fa, la, wa, ca, da = A
    fb, lb, wb, cb, db = B
    # salta frasi vicine nello stesso file (stesso punto, non "punti distinti")
    if fa == fb and abs(la - lb) < 8:
        continue
    # near-literal: condividono una sequenza di >=6 parole
    g = ngrams(wa, 6) & ngrams(wb, 6)
    if g:
        near_literal.append((len(g), fa, la, da, fb, lb, db))
        continue
    # paraphrase: alta sovrapposizione di parole-contenuto
    jc = jacc(ca, cb)
    shared = len(set(ca) & set(cb))
    if jc >= 0.55 and shared >= 6:
        paraphrase.append((round(jc, 2), shared, fa, la, da, fb, lb, db))

def short(f): return f.split("/")[-1].replace(".tex", "")

print("="*70)
print(f"NEAR-LITERAL (condividono >=6 parole consecutive) — {len(near_literal)} coppie")
print("="*70)
for n, fa, la, da, fb, lb, db in sorted(near_literal, reverse=True):
    print(f"\n[{n} match] {short(fa)}:{la}  <->  {short(fb)}:{lb}")
    print(f"   A: {da[:160]}")
    print(f"   B: {db[:160]}")

print("\n" + "="*70)
print(f"PARAFRASI / STESSO CONCETTO (Jaccard>=0.55) — {len(paraphrase)} coppie")
print("="*70)
for jc, sh, fa, la, da, fb, lb, db in sorted(paraphrase, reverse=True):
    print(f"\n[J={jc} sh={sh}] {short(fa)}:{la}  <->  {short(fb)}:{lb}")
    print(f"   A: {da[:160]}")
    print(f"   B: {db[:160]}")
