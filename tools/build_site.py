#!/usr/bin/env python3
"""REPORT.md → docs/index.html;自包含单页,含两级目录、滚动高亮、证据分级图例、深浅色主题。
用法:python3 tools/build_site.py [--archive]

视觉设定(财政文书底子,非通用模板):
  · 纸=账页白,墨=偏绿的黑,唯一强调色=国库绿;红/琥珀/绿只给 🔴 ⚠ ✅ 三类标记用。
  · 🔴 源稿 37% 的字符是粗体(私有稿写作习惯)——本页不删粗体,改为【用墨色深浅表达强调而非字重】:
    正文墨色压低一档,strong 只加深不加粗(600),表格内更轻。
  · 整段皆粗体的"裁决句"识别出来另作判语块(正常字重 + 左规线),把噪声变成层级。
  · 段首的 🔴/⚠/📌/✅ 等标记移入悬挂标记栏,正文左缘对齐,标记自成一列可纵向扫读。
"""
import re, sys, html as H, datetime, json as _json
from pathlib import Path
import markdown

ROOT = Path(__file__).resolve().parent.parent
DATA_AS_OF = '2026-09-07'          # 时效性数字刷新至(源稿刷新后改这里)
BASE = 'https://ronfi.github.io/us-debt/'
REPO = 'https://github.com/ronfi/us-debt'
SITE = '美国国债研究 · US Debt'

LANG = {
 'zh': dict(
    src='REPORT.md', out='docs/index.html', html_lang='zh-CN', url=BASE, og_image=BASE + 'og.png',
    title='美国国债:40 万亿之后 —— 债务、美元与金融抑制 2.0 的机制核查',
    og_title='美国国债:40 万亿之后',
    og='不预测日期,只钉住机制与可判条件:$40T 之后的债务、美元与"金融抑制 2.0"。',
    desc='美国国债研究:债务口径与期限结构、净利息复利、持有人轮换、拍卖健康度、美元与储备份额、石油美元叙事的证伪、1946-1980 金融抑制剧本与它的当代复刻(GENIUS Act / eSLR / Fed 买 bills),以及六个钉死判定源的机械触发器。全部数字标注来源等级,一手为主。',
    keywords='美国国债, 美债, 40万亿, 净利息, 金融抑制, GENIUS Act, 稳定币, 短债, T-Bill, 美元储备份额, 石油美元, 债务上限, 期限溢价, Warsh, 贬值税',
    site='美国国债研究 · US Debt',
    asof='时效性数字刷新至', update='不定期更新(源稿刷新时同步)', source='源码与全文',
    toc='目录', built='页面生成', license='内容 CC BY-NC-ND 4.0 · 脚本 MIT',
    archive='历次版本存档', archive_href='archive/',
    switch='<span class="on" lang="zh-CN">中文</span><a href="en/" hreflang="en" lang="en">English</a>',
    pv='本页访问 <span id="busuanzi_value_page_pv"></span> 次(计数由第三方脚本 busuanzi 提供)',
    archnote='这是 {d} 的存档版本,数据与文字停留在当时;最新版见',
    support='打赏 / Support', support_qr='展开二维码', support_copy='点击复制',
    support_note='这个项目会长期免费、公开地维护下去。如果这份核查帮您在一堆互相矛盾的数字里分清了口径,那就是它存在的意义。'
                 '您的支持是它继续维护的动力,无论金额大小,都衷心感谢。'
                 f'地址以 <a href="{REPO}/blob/main/DONATE.md">DONATE.md(main 分支)</a>为唯一权威源;'
                 '在其他任何地方看到的地址,无论看起来多像,都不要使用。',
    donate_desc={'evm': 'ETH / L2s / BSC · ETH/USDC/USDT', 'tron': 'USDT-TRC20', 'sol': 'SOL / SPL',
                 'btc-segwit': 'Native SegWit(推荐)', 'btc-legacy': '兼容旧钱包'},
    legend=[('✅', '一手(官方接口 / 原始文档全文)'), ('🔶', '一手数据 + 本文自算,须连口径引用'),
            ('⚠', '单一来源或口径受限,只用于画窗口'), ('🔴', '最吃重、最易被误读之处'), ('❌', '经核查证伪')],
    stale='⚠ 英文版落后于中文版,以中文版为准。',
 ),
 'en': dict(
    src='REPORT.en.md', out='docs/en/index.html', html_lang='en', url=BASE + 'en/', og_image=BASE + 'og-en.png',
    title='US Debt After $40 Trillion — the debt, the dollar, and the machinery of Financial Repression 2.0',
    og_title='US Debt After $40 Trillion',
    og='No dates predicted — only mechanisms and falsifiable conditions: the debt, the dollar and "Financial Repression 2.0" after $40T.',
    desc='A mechanism-level audit of US federal debt: the four measures of the debt and its maturity structure, compounding net interest, the rotation in the marginal buyer, auction health, the dollar and reserve shares, the falsification of the petrodollar story, the 1946-1980 financial-repression playbook and its modern replica (GENIUS Act / eSLR / the Fed buying bills), plus six mechanical triggers with fixed adjudication sources. Every figure carries a source grade; primary sources throughout.',
    keywords='US debt, Treasury debt, 40 trillion, net interest, financial repression, GENIUS Act, stablecoins, T-bills, dollar reserve share, petrodollar, debt limit, term premium, Warsh, debasement tax',
    site='US Debt Research',
    asof='Time-sensitive figures current to', update='Updated when the source is refreshed', source='Source and full text',
    toc='Contents', built='Page built', license='Content CC BY-NC-ND 4.0 · scripts MIT',
    archive='Version archive', archive_href='../archive/',
    switch='<a href="../" hreflang="zh-CN" lang="zh-CN">中文</a><span class="on" lang="en">English</span>',
    pv='<span id="busuanzi_value_page_pv"></span> page views (counted by the third-party busuanzi script)',
    archnote='This is the archived {d} edition; data and text are as of then. Latest:',
    support='Support', support_qr='show QR code', support_copy='click to copy',
    support_note='This project will stay free and public for the long run. If this audit ever saved you from mixing up two different measures of the same number, that is what it is for. '
                 'Your support keeps it maintained; any amount is sincerely appreciated. '
                 f'The addresses in <a href="{REPO}/blob/main/DONATE.md">DONATE.md on the main branch</a> are the only authoritative source; '
                 'do not use any address you see anywhere else, however similar it looks.',
    donate_desc={'evm': 'ETH / L2s / BSC · ETH/USDC/USDT', 'tron': 'USDT-TRC20', 'sol': 'SOL / SPL',
                 'btc-segwit': 'Native SegWit (recommended)', 'btc-legacy': 'legacy wallets'},
    legend=[('✅', 'primary (official API / full original document)'), ('🔶', 'primary data + own calculation; cite the method with it'),
            ('⚠', 'single source or limited caliber; sizes a window, never settles one'), ('🔴', 'load-bearing, and easiest to misread'), ('❌', 'falsified on checking')],
    stale='⚠ The English edition lags the Chinese one; the Chinese edition governs.',
 ),
}

CSS = """
:root{
  --paper:#FBFAF7;--paper2:#F1F0EA;--panel:#F6F5F0;--rule:#DEDCD3;
  --ink:#333834;--ink-em:#0D110F;--ink2:#737872;
  --accent:#1B4D3E;--accent-soft:#E4EDE8;
  --red:#9E2A20;--amber:#8A6410;--green:#1B6B4A;--gold:#8A6D1F;--mark:#F3E8C6;--code:#EAE8E0;
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
  --paper:#141714;--paper2:#1B1F1B;--panel:#191D19;--rule:#2E332E;
  --ink:#C7CCC6;--ink-em:#F3F6F1;--ink2:#8D948C;
  --accent:#7FBFA3;--accent-soft:#1D2A24;
  --red:#E88E82;--amber:#D6B15E;--green:#7BD3A3;--gold:#D3B577;--mark:#3E3720;--code:#22261F;
}}
:root[data-theme="dark"]{
  --paper:#141714;--paper2:#1B1F1B;--panel:#191D19;--rule:#2E332E;
  --ink:#C7CCC6;--ink-em:#F3F6F1;--ink2:#8D948C;
  --accent:#7FBFA3;--accent-soft:#1D2A24;
  --red:#E88E82;--amber:#D6B15E;--green:#7BD3A3;--gold:#D3B577;--mark:#3E3720;--code:#22261F;
}
*{box-sizing:border-box}html{scroll-behavior:smooth}@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--paper);color:var(--ink);
  font:16px/1.85 "Noto Sans SC","PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
  font-variant-numeric:tabular-nums;-webkit-font-smoothing:antialiased}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 30%,transparent)}
a:hover{border-bottom-color:var(--accent)}a:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* ── 报头:一条国库绿细线压顶,其余留白 ── */
.mast{border-bottom:1px solid var(--rule);background:var(--paper2);border-top:3px solid var(--accent)}
.mast-in{max-width:1240px;margin:0 auto;padding:24px 28px 20px;display:flex;flex-wrap:wrap;align-items:center;gap:8px 18px}
.mast h1{flex:1 1 auto;min-width:0;font:600 26px/1.34 "Noto Serif SC","Songti SC","SimSun",serif;margin:0;color:var(--ink-em);letter-spacing:.2px;text-wrap:balance}
html[lang=en] .mast h1{font-family:"Noto Serif",Georgia,"Times New Roman",serif;font-size:24px}
.mast .lang{margin-left:auto;flex:0 0 auto;display:inline-flex;border:1px solid var(--rule);border-radius:5px;overflow:hidden;background:var(--paper);font-size:12.5px;line-height:1;align-self:center}
.mast .lang a,.mast .lang span{padding:7px 13px;border:0;font-weight:600;color:var(--ink2)}
.mast .lang a:hover{color:var(--accent);background:var(--panel)}
.mast .lang .on{background:var(--accent);color:var(--paper)}
.mast .meta{flex:1 1 100%;color:var(--ink2);font-size:12.5px;display:flex;gap:10px 22px;flex-wrap:wrap;align-items:baseline;margin-top:2px}
.mast .meta b{font-weight:500;color:var(--ink);font-family:"JetBrains Mono",ui-monospace,monospace;font-size:12px}

.wrap{max-width:1240px;margin:0 auto;padding:30px 28px 60px;display:grid;grid-template-columns:246px minmax(0,1fr);gap:48px}

/* ── 两级目录 + 滚动高亮 ── */
nav.toc{position:sticky;top:16px;align-self:start;font-size:13px;line-height:1.55;max-height:calc(100vh - 32px);overflow-y:auto;scrollbar-width:thin}
nav.toc .lbl{font:500 10.5px/1 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.16em;text-transform:uppercase;color:var(--ink2);margin-bottom:10px}
nav.toc ol{list-style:none;margin:0;padding:0;border-left:1px solid var(--rule)}
nav.toc>ol>li>a{display:block;padding:5px 0 5px 13px;color:var(--ink2);border:0;margin-left:-1px;border-left:2px solid transparent;transition:color .12s}
nav.toc>ol>li>a:hover{color:var(--ink-em)}
nav.toc>ol>li.cur>a{color:var(--ink-em);font-weight:600;border-left-color:var(--accent)}
nav.toc ul.sub{list-style:none;margin:0 0 6px;padding:0 0 0 13px;display:none}
nav.toc>ol>li.cur ul.sub{display:block}
nav.toc ul.sub a{display:block;padding:2.5px 0;color:var(--ink2);border:0;font-size:12px;line-height:1.45}
nav.toc ul.sub a:hover{color:var(--accent)}
nav.toc ul.sub li.cur a{color:var(--accent)}
.legend{margin-top:24px;padding-top:15px;border-top:1px solid var(--rule);color:var(--ink2);font-size:12px;display:grid;gap:8px;line-height:1.5}
.legend .g{display:grid;grid-template-columns:1.5em 1fr;gap:2px}
.legend b{font-weight:400}

main{min-width:0}
main>blockquote:first-of-type{margin:0 0 30px;padding:18px 22px;border:0;border-left:3px solid var(--accent);
  background:var(--panel);color:var(--ink);font-size:14.5px;line-height:1.8;border-radius:0 3px 3px 0}
main>blockquote:first-of-type strong{color:var(--ink-em)}

/* ── 标题层级:序号用等宽字,与正文分离 ── */
h2{font:600 22px/1.4 "Noto Serif SC","Songti SC","SimSun",serif;color:var(--ink-em);
  margin:3em 0 .9em;padding-top:.85em;border-top:1px solid var(--rule);text-wrap:balance;scroll-margin-top:14px}
h2:first-of-type{border-top:0;padding-top:0;margin-top:.1em}
h3{font:600 16.5px/1.5 "Noto Sans SC",sans-serif;color:var(--ink-em);margin:2.1em 0 .6em;scroll-margin-top:14px}
h4{font:600 15px/1.5 "Noto Sans SC",sans-serif;color:var(--ink-em);margin:1.7em 0 .45em}
h5{font:500 13.5px/1.55 "Noto Sans SC",sans-serif;color:var(--ink2);margin:1.6em 0 .4em}

main p{margin:.75em 0}ol,ul{padding-left:1.5em}li{margin:.38em 0}li::marker{color:var(--ink2)}

/* 🔴 关键:强调靠墨色不靠字重 —— 正文墨色本就压低一档,strong 只加深 */
strong{font-weight:600;color:var(--ink-em)}
td strong,th strong{font-weight:600}
em{font-style:normal;color:var(--ink-em)}

/* 判语块:源稿里整段皆粗体的句子 —— 去掉粗体,改用规线与字号建立层级 */
p.verdict{font-weight:400;color:var(--ink-em);font-size:16.5px;line-height:1.8;
  margin:1.25em 0;padding:2px 0 2px 16px;border-left:2px solid var(--accent)}
blockquote p.verdict{border-left:0;padding-left:0;font-size:15.5px}

/* 悬挂标记栏:段首 🔴/⚠/📌/✅ 移出文本流,正文左缘对齐,标记自成一列 */
.flagged{padding-left:1.75em;text-indent:-1.75em}
li.flagged{text-indent:-1.75em;padding-left:0}
.flag{display:inline-block;width:1.75em;text-indent:0;font-size:13px;line-height:1;transform:translateY(-.5px)}
.f-red{color:var(--red)}.f-amber{color:var(--amber)}.f-green{color:var(--green)}
.f-gold{color:var(--gold)}.f-accent{color:var(--accent)}.f-ink2{color:var(--ink2)}

blockquote{margin:1.15em 0;padding:11px 18px;border-left:2px solid var(--rule);background:var(--panel);border-radius:0 3px 3px 0}
blockquote p{margin:.4em 0}
blockquote blockquote{background:transparent;margin:.5em 0}
blockquote.q-red{border-left-color:var(--red)}
blockquote.q-amber{border-left-color:var(--amber)}
blockquote.q-green{border-left-color:var(--green)}
blockquote.q-accent{border-left-color:var(--accent)}

.tbl{overflow-x:auto;margin:1.1em 0 1.7em;border:1px solid var(--rule);border-radius:3px;background:var(--paper2)}
table{border-collapse:collapse;width:100%;font-size:13.5px;line-height:1.6}
th{font:500 11.5px/1.4 "JetBrains Mono",ui-monospace,monospace;letter-spacing:.03em;color:var(--ink2);
  text-align:left;background:var(--paper2);border-bottom:1px solid var(--rule);padding:10px 12px;white-space:nowrap}
td{padding:9px 12px;border-top:1px solid var(--rule);vertical-align:top;background:var(--paper);color:var(--ink)}
td:first-child{white-space:nowrap;color:var(--ink-em)}
tr:hover td{background:var(--panel)}
mark{background:var(--mark);color:var(--ink-em);padding:0 3px;border-radius:2px}
code{font:12.5px/1.5 "JetBrains Mono",ui-monospace,Menlo,Consolas,monospace;background:var(--code);color:var(--ink-em);padding:1.5px 5px;border-radius:3px}
pre{background:var(--code);padding:13px 15px;border-radius:4px;overflow-x:auto;font-size:12.5px;line-height:1.65}pre code{background:none;padding:0}
hr{border:0;border-top:1px solid var(--rule);margin:2.8em 0}
figure.fig{margin:1.6em 0;overflow-x:auto}
figure.fig figcaption{color:var(--ink2);font-size:12px;margin-top:8px;line-height:1.6}

.stale{background:var(--mark);color:var(--ink-em);padding:11px 16px;border-radius:3px;font-size:13.5px;margin:0 0 22px}
.support{margin:52px 0 0;border:1px solid var(--rule);border-radius:3px;background:var(--panel)}
.support>summary{padding:14px 20px;cursor:pointer;color:var(--accent);font-weight:600;font-size:15px;list-style:none}
.support>summary::-webkit-details-marker{display:none}
.support>summary::before{content:"▸ ";color:var(--ink2);font-weight:400}
.support[open]>summary::before{content:"▾ "}
.support .sbody{padding:2px 20px 20px}
.support .note{color:var(--ink2);font-size:13px;line-height:1.8;margin:0 0 16px;max-width:62em}
.dgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(292px,1fr));gap:12px}
.dcard{background:var(--paper);border:1px solid var(--rule);border-radius:3px;padding:13px 14px;min-width:0}
.dcard b{font-size:13.5px;color:var(--ink-em)}
.dcard span{color:var(--ink2);font-size:11.5px;margin-left:8px}
.dcard code{display:block;margin-top:7px;font-size:11.5px;word-break:break-all;color:var(--accent);cursor:pointer;background:none;padding:0;line-height:1.65}
.dqr summary{color:var(--ink2);font-size:11.5px;cursor:pointer;margin-top:9px;list-style:none}
.dqr summary::before{content:"▸ "}.dqr[open] summary::before{content:"▾ "}
.dqr svg{display:block;margin-top:9px;width:150px;height:150px;background:#fff;padding:6px;border-radius:3px}
.site-foot{border-top:1px solid var(--rule);background:var(--paper2);position:relative;z-index:2}
.foot-in{max-width:1240px;margin:0 auto;padding:20px 28px;color:var(--ink2);font-size:12px;
  display:flex;flex-wrap:wrap;gap:8px 22px;line-height:1.7}
@media (max-width:940px){
  .wrap{grid-template-columns:1fr;gap:20px;padding:22px 20px 60px}
  nav.toc{position:static;max-height:none;border-bottom:1px solid var(--rule);padding-bottom:14px}
  nav.toc ol{display:flex;flex-wrap:wrap;gap:3px 14px;border:0}
  nav.toc>ol>li>a{padding:2px 0;border:0}nav.toc ul.sub{display:none!important}
  .legend{display:none}.mast-in{padding:18px 20px}.foot-in{padding:18px 20px}.mast h1{font-size:21px}
  body{font-size:15.5px}
}
"""

SVG_THEME = [('#0d1117', 'var(--panel)'), ('rgba(255,255,255,.08)', 'var(--rule)'),
             ('rgba(255,255,255,.07)', 'var(--rule)'), ('rgba(255,255,255,.28)', 'var(--ink2)'),
             ('#edf1f6', 'var(--ink-em)'), ('#c6ceda', 'var(--ink)'), ('#8b95a5', 'var(--ink2)'), ('#6b7585', 'var(--ink2)'),
             ('rgba(211,181,119,.13)', 'rgba(176,137,44,.20)'), ('rgba(211,181,119,.55)', 'var(--ink2)'),
             ('rgba(211,181,119,.4)', 'var(--rule)'), ('rgba(211,181,119,.35)', 'rgba(176,137,44,.45)'),
             ('#d3b577', 'var(--gold)'), ('#5aa7d6', 'var(--accent)'), ('#e06c5a', 'var(--red)')]

DONATE = [  # 与 DONATE.md(main 分支,唯一权威源)逐字一致
    ('EVM', '0xcd98738afada22ace19830f2e7bcd1dee89f6869', 'evm', 'ETH / L2s / BSC · ETH/USDC/USDT'),
    ('TRON', 'TSjurosohn1psMKg5xV4L2ELCiLJTzcPMD', 'tron', 'USDT-TRC20'),
    ('Solana', '6LWiGPToGAjgYVwsYgqv5QAKfGm38jnhyDALbZYK3weC', 'sol', 'SOL / SPL'),
    ('Bitcoin', 'bc1qtpxutlz9ttve7z7mnvt87w95njeejmeallvwyg', 'btc-segwit', 'Native SegWit(推荐)'),
    ('Bitcoin · Legacy', '132v6ZpuZEFVCrkoRbUfKGCBayy31gWZnj', 'btc-legacy', '兼容旧钱包'),
]
_dm = (ROOT / 'DONATE.md').read_text(encoding='utf8')
for _n, _a, _q, _d in DONATE:
    assert _a in _dm, f'地址不在 DONATE.md:{_a}'

SUPPORT_NOTE = ('这个项目会长期免费、公开地维护下去。如果这份核查帮您在一堆互相矛盾的数字里分清了口径,那就是它存在的意义。'
                '您的支持是它继续维护的动力,无论金额大小,都衷心感谢。'
                f'地址以 <a href="{REPO}/blob/main/DONATE.md">DONATE.md(main 分支)</a>为唯一权威源;'
                '在其他任何地方看到的地址,无论看起来多像,都不要使用。')

FLAG = {'🔴': 'f-red', '❌': 'f-red', '⚠': 'f-amber', '🔶': 'f-gold',
        '✅': 'f-green', '📌': 'f-accent', '🔄': 'f-accent', '❔': 'f-ink2', '📖': 'f-ink2'}
FLAGCH = ''.join(FLAG)
_strip = lambda s: re.sub(r'<[^>]+>', '', s)


def verdictify(body):
    """整段皆粗体 → 判语块(去粗体,改用规线与字号)。源稿有 31 段这样的句子。"""
    def one(m):
        inner = m.group(1)
        if '<strong>' not in inner:
            return m.group(0)
        rest = _strip(re.sub(r'<strong>.*?</strong>', '', inner, flags=re.S)).strip()
        if len(rest) > 5:                       # 粗体之外还有实质内容 ⇒ 不是整段裁决句
            return m.group(0)
        return '<p class="verdict">' + inner.replace('<strong>', '').replace('</strong>', '') + '</p>'
    return re.sub(r'<p>(.*?)</p>', one, body, flags=re.S)


def flagify(body):
    """段首标记移入悬挂标记栏(标记不参与加粗,正文左缘对齐)。"""
    def one(m):
        tag, cls, inner = m.group(1), m.group(2) or '', m.group(3)
        mm = re.match(rf'((?:<strong>)?)\s*([{FLAGCH}])\s*', inner)
        if not mm:
            return m.group(0)
        ch = mm.group(2)
        rest = mm.group(1) + inner[mm.end():]
        cls = (cls + ' flagged').strip()
        return f'<{tag} class="{cls}"><span class="flag {FLAG[ch]}">{ch}</span>{rest}</{tag}>'
    return re.sub(r'<(p|li)(?: class="([^"]*)")?>(.*?)</\1>', one, body, flags=re.S)


def quoteclass(body):
    """引用块按其首个标记着色左规线,让"裁决/警示/确证"三类一眼可分。"""
    def one(m):
        head = _strip(m.group(1))[:8]
        for ch, cl in FLAG.items():
            if ch in head:
                return f'<blockquote class="q-{cl[2:]}">' + m.group(1) + '</blockquote>'
        return m.group(0)
    return re.sub(r'<blockquote>(.*?)</blockquote>', one, body, flags=re.S)


def _en_stale():
    """英文版是否落后于中文版(按章哈希;详见 tools/en_sync.py)。漂移时英文页自动挂提示,
    不依赖任何人记得 —— 静默过期的译文比没有译文更糟。"""
    st = ROOT / 'data' / 'en_sync.json'
    if not st.exists(): return True
    import hashlib
    md = (ROOT / 'REPORT.md').read_text(encoding='utf8').split('\n')
    idx = [i for i, l in enumerate(md) if l.startswith('## ')] + [len(md)]
    now = [hashlib.sha256('\n'.join(md[idx[k]:idx[k+1]]).encode()).hexdigest()[:16] for k in range(len(idx)-1)]
    return now != _json.loads(st.read_text(encoding='utf8')).get('synced')

def build(lang):
    T = LANG[lang]; other = LANG['en' if lang == 'zh' else 'zh']
    src = ROOT / T['src']
    if not src.exists():
        print(f'· 跳过 {lang}:{T["src"]} 不存在'); return
    md = src.read_text(encoding='utf8')
    lines = md.split('\n'); title = lines[0].lstrip('# ').strip()
    body = markdown.markdown('\n'.join(lines[1:]), extensions=['tables', 'fenced_code', 'toc'],
                             extension_configs={'toc': {'toc_depth': '3', 'slugify': lambda v, s: re.sub(r'[^\w一-鿿]+', '-', v).strip('-').lower()}})
    # 两级目录:每个 h2 下挂它的 h3(章内导航,60k 字的文章没有它只能靠滚)
    heads = [(int(m.group(1)), m.group(2), _strip(m.group(3))) for m in re.finditer(r'<h([23]) id="([^"]+)">(.*?)</h\1>', body)]
    toc, cur = [], None
    for lv, hid, txt_ in heads:
        if lv == 2:
            if cur: toc.append(cur + '</ul></li>')
            cur = f'<li><a href="#{hid}">{txt_}</a><ul class="sub">'
        elif cur:
            short = re.sub(r'[((].*$', '', txt_).strip()[:24]
            cur += f'<li><a href="#{hid}">{H.escape(short)}</a></li>'
    if cur: toc.append(cur + '</ul></li>')

    body = verdictify(body)
    body = flagify(body)
    body = quoteclass(body)
    body = body.replace('<table>', '<div class="tbl"><table>').replace('</table>', '</table></div>')
    for a, b in SVG_THEME:
        body = body.replace(a, b)
    body = body.replace('<div style="overflow-x:auto;margin:1.1em 0;">', '<figure class="fig">').replace('</svg></div>', '</svg></figure>')

    qr = lambda n: (p.read_text(encoding='utf8') if (p := ROOT / 'assets' / 'qr' / f'{n}.svg').exists() else '')
    support = (f'<details class="support" id="support"><summary>{T["support"]}</summary><div class="sbody"><p class="note">' + T['support_note'] + '</p><div class="dgrid">'
               + ''.join(f'<div class="dcard"><b>{net}</b><span>{T["donate_desc"][q]}</span>'
                         f'<code onclick="navigator.clipboard&amp;&amp;navigator.clipboard.writeText(this.textContent)" title="{T["support_copy"]}">{addr}</code>'
                         f'<details class="dqr"><summary>{T["support_qr"]}</summary>{qr(q)}</details></div>'
                         for net, addr, q, _d in DONATE)
               + '</div></div></details>')

    legend = ''.join(f'<div class="g"><span class="flag {FLAG[k]}">{k}</span><b>{v}</b></div>' for k, v in T['legend'])
    built = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    stale_note = (f'<p class="stale">{T["stale"]} <a href="{other["url"]}">{other["title"]}</a></p>'
                  if lang == 'en' and _en_stale() else '')
    jsonld = _json.dumps({'@context': 'https://schema.org', '@type': 'Report', 'name': T['og_title'], 'headline': title,
                          'description': T['desc'], 'url': T['url'], 'inLanguage': T['html_lang'], 'dateModified': DATA_AS_OF,
                          'license': 'https://creativecommons.org/licenses/by-nc-nd/4.0/', 'isAccessibleForFree': True,
                          'keywords': [k.strip() for k in T['keywords'].split(',')],
                          'author': {'@type': 'Organization', 'name': SITE, 'url': REPO}, 'sameAs': REPO}, ensure_ascii=False)
    spy = """
document.addEventListener('DOMContentLoaded',function(){
 var sup=document.getElementById('support');
 if(sup){
  [].forEach.call(document.querySelectorAll('a[href="#support"]'),function(a){
   a.addEventListener('click',function(){sup.open=true});
  });
  if(location.hash==='#support')sup.open=true;
 }
 var links=[].slice.call(document.querySelectorAll('nav.toc a')),
     secs=links.map(function(a){return document.getElementById(a.getAttribute('href').slice(1))}),
     tick=false;
 function mark(){
  var y=window.scrollY+120,i,best=0;
  for(i=0;i<secs.length;i++){if(secs[i]&&secs[i].offsetTop<=y)best=i}
  links.forEach(function(a){var li=a.parentNode;li.classList.remove('cur')});
  var a=links[best];if(!a)return;
  a.parentNode.classList.add('cur');
  var top=a.closest('nav.toc>ol>li');if(top)top.classList.add('cur');
  tick=false;
 }
 window.addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(mark)}},{passive:true});
 mark();
});"""
    html = f"""<!DOCTYPE html><html lang="{T['html_lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{H.escape(T['title'])}</title>
<meta name="description" content="{H.escape(T['desc'])}">
<meta name="robots" content="index,follow,max-image-preview:large"><meta name="keywords" content="{H.escape(T['keywords'])}">
<link rel="canonical" href="{T['url']}"><link rel="alternate" hreflang="{T['html_lang']}" href="{T['url']}"><link rel="alternate" hreflang="{other['html_lang']}" href="{other['url']}"><link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="article"><meta property="og:site_name" content="{T['site']}"><meta property="og:locale" content="{'zh_CN' if lang == 'zh' else 'en_US'}"><meta property="og:title" content="{H.escape(T['og_title'])}"><meta property="og:description" content="{H.escape(T['og'])}"><meta property="og:url" content="{T['url']}"><meta property="og:image" content="{T['og_image']}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="article:modified_time" content="{DATA_AS_OF}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{H.escape(T['og_title'])}"><meta name="twitter:description" content="{H.escape(T['og'])}"><meta name="twitter:image" content="{T['og_image']}">
<script type="application/ld+json">{jsonld}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600&family=Noto+Sans+SC:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}</style></head><body>
<header class="mast"><div class="mast-in"><h1>{H.escape(title)}</h1><nav class="lang" aria-label="language">{T['switch']}</nav>
<div class="meta"><span>{T['asof']} <b>{DATA_AS_OF}</b></span><span>{T['update']}</span><span><a href="{REPO}">{T['source']}</a></span></div></div></header>
<div class="wrap">
<nav class="toc" aria-label="{T['toc']}"><div class="lbl">{T['toc']}</div><ol>{''.join(toc)}</ol><div class="legend">{legend}</div></nav>
<main>
{stale_note}{body}
{support}
</main>
</div>
<footer class="site-foot"><div class="foot-in"><span>{T['source']}: <a href="{REPO}">github.com/ronfi/us-debt</a></span><span><a href="{T['archive_href']}">{T['archive']}</a></span><span>{T['built']} {built}</span><span>{T['license']}</span><span><a href="#support">{T['support']}</a></span><span id="busuanzi_container_page_pv" style="display:none">{T['pv']}</span></div></footer>
<script>{spy}</script><script async src="//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js"></script></body></html>"""
    out = ROOT / T['out']; out.parent.mkdir(parents=True, exist_ok=True); out.write_text(html, encoding='utf8')
    if '--archive' in sys.argv:
        arch = ROOT / 'docs' / 'archive'; arch.mkdir(exist_ok=True)
        note = f'<div class="archnote">{T["archnote"].format(d=DATA_AS_OF)} <a href="{T['url']}">{T['url']}</a> · <a href="./">{T["archive"]}</a></div>'
        a = (html.replace(f'href="{T["archive_href"]}"', 'href="./"')
                 .replace('<meta name="robots" content="index,follow,max-image-preview:large">', '<meta name="robots" content="noindex,follow">', 1)
                 .replace('<body>', '<body>' + note, 1)
                 .replace('</style>', '.archnote{background:var(--mark);color:var(--ink-em);padding:11px 28px;font-size:12.5px}</style>', 1))
        (arch / (f'{DATA_AS_OF}.html' if lang == 'zh' else f'{DATA_AS_OF}.en.html')).write_text(a, encoding='utf8')
        dates = sorted({f.name[:10] for f in arch.glob('????-??-??*.html')}, reverse=True)
        items = ''.join(f'<li><span class="d">{d}</span> <a href="{d}.html">中文</a>'
                        + (f' · <a href="{d}.en.html">English</a>' if (arch / f'{d}.en.html').exists() else '') + '</li>' for d in dates)
        (arch / 'index.html').write_text(f"""<!DOCTYPE html><html lang="{T['html_lang']}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{SITE} · 历次版本存档</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@600&family=Noto+Sans+SC:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<style>{CSS}.arch{{max-width:760px;margin:0 auto;padding:36px 28px}}.arch li{{margin:.55em 0}}.arch .d{{font-family:"JetBrains Mono",ui-monospace,monospace;margin-right:10px;color:var(--ink2)}}</style></head><body>
<div class="arch"><h2>历次版本存档 / Version archive</h2><p>不回改的可信度 = 旧版本的可访问性。每次刷新存一份当时的页面,数据与文字停留在当时。<br>Credibility without retroactive edits = old versions stay reachable. A copy of the page is archived at each refresh, with data and text as of then.</p><ul>{items}</ul><p><a href="{BASE}">← 最新版</a></p></div></body></html>""", encoding='utf8')
        print('archive', dates)
    (ROOT / 'docs' / 'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
    (ROOT / 'docs' / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">'
        + ''.join(f'<url><loc>{LANG[l]["url"]}</loc><lastmod>{DATA_AS_OF}</lastmod><changefreq>monthly</changefreq><priority>{"1.0" if l == "zh" else "0.9"}</priority>'
                  + ''.join(f'<xhtml:link rel="alternate" hreflang="{LANG[m]["html_lang"]}" href="{LANG[m]["url"]}"/>' for m in LANG) + '</url>'
                  for l in LANG if (ROOT / LANG[l]['src']).exists())
        + f'<url><loc>{BASE}archive/</loc><changefreq>monthly</changefreq><priority>0.3</priority></url></urlset>')
    print(f"built {len(html):,} 字符;目录 {len(toc)} 章;判语块 {html.count('p class=\"verdict\"')};"
          f"悬挂标记 {html.count('class=\"flag ')};着色引用 {html.count('blockquote class=\"q-')};表 {html.count('<table')};图 {html.count('<svg')}")

for _lang in LANG:
    build(_lang)
