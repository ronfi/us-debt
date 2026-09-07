#!/usr/bin/env python3
"""生成 1200×630 的 OG 分享图(docs/og.png)。用法:python3 tools/make_og.py"""
from pathlib import Path
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

ROOT = Path(__file__).resolve().parent.parent
FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
fm.fontManager.addfont(FONT)
CJK = fm.FontProperties(fname=FONT)

PAPER, INK, INK2, RULE, GOLD, RED = '#F6F5F2', '#1A1A17', '#63625C', '#DCDAD3', '#8A6D1F', '#B42318'
# 净利息 / 联邦收入(FY16→FY26 前 10 个月),数据同正文 §2.1(MTS 一手)
RATIO = [7.4, 8.0, 9.3, 10.1, 9.4, 8.1, 9.1, 13.7, 16.6, 17.1, 20.8]
YEARS = list(range(2016, 2027))

fig = plt.figure(figsize=(12, 6.3), dpi=100)
fig.patch.set_facecolor(PAPER)

import sys
EN = '--en' in sys.argv
if EN:
    fig.text(.065, .80, 'US Debt After $40 Trillion', fontsize=50, color=INK, weight='bold', family='DejaVu Sans')
    fig.text(.065, .705, 'the debt, the dollar, and the machinery of Financial Repression 2.0', fontsize=21, color=INK2, family='DejaVu Sans')
    fig.text(.065, .175, 'Mechanisms, not dates. Criteria, not noise.', fontsize=21, color=GOLD, family='DejaVu Sans')
else:
    fig.text(.065, .80, '美国国债:40 万亿之后', fontproperties=CJK, fontsize=54, color=INK, weight='bold')
    fig.text(.065, .705, '债务、美元与「金融抑制 2.0」的机制核查', fontproperties=CJK, fontsize=25, color=INK2)
    fig.text(.065, .175, '机制,不是日期。判据,不是叫喊。', fontproperties=CJK, fontsize=22, color=GOLD)
fig.text(.065, .095, 'ronfi.github.io/us-debt', fontsize=19, color=INK2, family='DejaVu Sans')

ax = fig.add_axes([.065, .30, .87, .33])
ax.set_facecolor(PAPER)
ax.bar(YEARS, RATIO, color=[RED if y >= 2022 else RULE for y in YEARS], width=.62)
for s in ('top', 'right', 'left'):
    ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color(RULE)
ax.set_yticks([]); ax.set_xticks([])
ax.set_xlim(2015.3, 2026.9); ax.set_ylim(0, 26)
ax.text(2016, 9.6, '7.4%', ha='center', fontsize=15, color=INK2, family='DejaVu Sans')
ax.text(2026, 23.0, '20.8%', ha='center', fontsize=17, color=RED, weight='bold', family='DejaVu Sans')
if EN:
    ax.text(2015.4, 24.4, 'Net interest / federal net receipts · FY2016 → FY2026 (first 10 months) · primary MTS',
            fontsize=14, color=INK2, family='DejaVu Sans')
else:
    ax.text(2015.4, 24.4, '净利息 / 联邦净收入 · FY2016 → FY2026(前 10 个月)· 一手 MTS',
            fontproperties=CJK, fontsize=15, color=INK2)

out = ROOT / 'docs' / ('og-en.png' if EN else 'og.png')
fig.savefig(out, facecolor=PAPER)
print(out.name, 'written')
