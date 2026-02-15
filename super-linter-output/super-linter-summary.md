# Super-linter summary

| Language                   | Validation result |
| -------------------------- | ----------------- |
| BIOME_FORMAT               | Fail ❌           |
| BIOME_LINT                 | Fail ❌           |
| GITLEAKS                   | Pass ✅           |
| GIT_MERGE_CONFLICT_MARKERS | Pass ✅           |
| JSON                       | Pass ✅           |
| JSON_PRETTIER              | Pass ✅           |
| PRE_COMMIT                 | Pass ✅           |
| SPELL_CODESPELL            | Fail ❌           |
| TRIVY                      | Pass ✅           |

Super-linter detected linting errors

For more information, see the [GitHub Actions workflow run](https://github.com/grayjay-sources/grayjay-sources.github.io/actions/runs/22034901377)

Powered by [Super-linter](https://github.com/super-linter/super-linter)

<details>

<summary>BIOME_FORMAT</summary>

```text
Checked 10 files in 577ms. No fixes applied.
Found 10 errors..vscode/launch.json format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

     1  1 │   {
     2    │ - ··//·Use·IntelliSense·to·learn·about·possible·attributes.
     3    │ - ··//·Hover·to·view·descriptions·of·existing·attributes.
     4    │ - ··//·For·more·information,·visit:·https://go.microsoft.com/fwlink/?linkid=830387
     5    │ - ··"version":·"0.2.0",
     6    │ - ··"configurations":·[
     7    │ - ····{
     8    │ - ······"name":·"Python·Debugger:·Current·File",
     9    │ - ······"type":·"debugpy",
    10    │ - ······"request":·"launch",
    11    │ - ······"program":·"${file}",
    12    │ - ······"console":·"integratedTerminal"
    13    │ - ····}
    14    │ - ··]
        2 │ + → //·Use·IntelliSense·to·learn·about·possible·attributes.
        3 │ + → //·Hover·to·view·descriptions·of·existing·attributes.
        4 │ + → //·For·more·information,·visit:·https://go.microsoft.com/fwlink/?linkid=830387
        5 │ + → "version":·"0.2.0",
        6 │ + → "configurations":·[
        7 │ + → → {
        8 │ + → → → "name":·"Python·Debugger:·Current·File",
        9 │ + → → → "type":·"debugpy",
       10 │ + → → → "request":·"launch",
       11 │ + → → → "program":·"${file}",
       12 │ + → → → "console":·"integratedTerminal"
       13 │ + → → }
       14 │ + → ]
    15 15 │   }
    16 16 │


.vscode/settings.json format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

     1  1 │   {
     2    │ - ··"json.schemas":·[
     3    │ - ····{
     4    │ - ······"fileMatch":·["sources.json"],
     5    │ - ······"url":·"./sources.schema.json"
     6    │ - ····}
     7    │ - ··],
     8    │ - ··"json.schemas.remote":·[
     9    │ - ····{
    10    │ - ······"fileMatch":·["sources.json"],
    11    │ - ······"url":·"https://github.com/grayjay-sources/grayjay-sources.github.io/raw/main/sources.schema.json"
    12    │ - ····}
    13    │ - ··]
        2 │ + → "json.schemas":·[
        3 │ + → → {
        4 │ + → → → "fileMatch":·["sources.json"],
        5 │ + → → → "url":·"./sources.schema.json"
        6 │ + → → }
        7 │ + → ],
        8 │ + → "json.schemas.remote":·[
        9 │ + → → {
       10 │ + → → → "fileMatch":·["sources.json"],
       11 │ + → → → "url":·"https://github.com/grayjay-sources/grayjay-sources.github.io/raw/main/sources.schema.json"
       12 │ + → → }
       13 │ + → ]
    14 14 │   }
    15 15 │


assets/css/site.css format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

      1   1 │   .hidden {
      2     │ - ··display:·none;
          2 │ + → display:·none;
      3   3 │   }
      4   4 │
      5   5 │   .bd-placeholder-img {
      6     │ - ··font-size:·1.125rem;
      7     │ - ··text-anchor:·middle;
      8     │ - ··user-select:·none;
          6 │ + → font-size:·1.125rem;
          7 │ + → text-anchor:·middle;
          8 │ + → user-select:·none;
      9   9 │   }
     10  10 │
     11  11 │   @media (width >= 768px) {
     12     │ - ··.bd-placeholder-img-lg·{
     13     │ - ····font-size:·3.5rem;
     14     │ - ··}
         12 │ + → .bd-placeholder-img-lg·{
         13 │ + → → font-size:·3.5rem;
         14 │ + → }
     15  15 │   }
     16  16 │
     17  17 │   .b-example-divider {
     18     │ - ··width:·100%;
     19     │ - ··height:·3rem;
     20     │ - ··background-color:·rgb(0·0·0·/·10%);
     21     │ - ··border:·solid·rgb(0·0·0·/·15%);
     22     │ - ··border-width:·1px·0;
     23     │ - ··box-shadow:
     24     │ - ····inset·0·0.5em·1.5em·rgb(0·0·0·/·10%),
     25     │ - ····inset·0·0.125em·0.5em·rgb(0·0·0·/·15%);
         18 │ + → width:·100%;
         19 │ + → height:·3rem;
         20 │ + → background-color:·rgb(0·0·0·/·10%);
         21 │ + → border:·solid·rgb(0·0·0·/·15%);
         22 │ + → border-width:·1px·0;
         23 │ + → box-shadow:
         24 │ + → → inset·0·0.5em·1.5em·rgb(0·0·0·/·10%),
         25 │ + → → inset·0·0.125em·0.5em·rgb(0·0·0·/·15%);
     26  26 │   }
     27  27 │
     28  28 │   .b-example-vr {
     29     │ - ··flex-shrink:·0;
     30     │ - ··width:·1.5rem;
     31     │ - ··height:·100vh;
         29 │ + → flex-shrink:·0;
         30 │ + → width:·1.5rem;
         31 │ + → height:·100vh;
     32  32 │   }
     33  33 │
     34  34 │   .bi {
     35     │ - ··vertical-align:·-0.125em;
     36     │ - ··fill:·currentcolor;
         35 │ + → vertical-align:·-0.125em;
         36 │ + → fill:·currentcolor;
     37  37 │   }
     38  38 │
     39  39 │   .nav-scroller {
     40     │ - ··position:·relative;
     41     │ - ··z-index:·2;
     42     │ - ··height:·2.75rem;
     43     │ - ··overflow-y:·hidden;
         40 │ + → position:·relative;
         41 │ + → z-index:·2;
         42 │ + → height:·2.75rem;
         43 │ + → overflow-y:·hidden;
     44  44 │   }
     45  45 │
     46  46 │   .nav-scroller .nav {
     47     │ - ··display:·flex;
     48     │ - ··flex-wrap:·nowrap;
     49     │ - ··padding-bottom:·1rem;
     50     │ - ··margin-top:·-1px;
     51     │ - ··overflow-x:·auto;
     52     │ - ··text-align:·center;
     53     │ - ··white-space:·nowrap;
     54     │ - ··-webkit-overflow-scrolling:·touch;
         47 │ + → display:·flex;
         48 │ + → flex-wrap:·nowrap;
         49 │ + → padding-bottom:·1rem;
         50 │ + → margin-top:·-1px;
         51 │ + → overflow-x:·auto;
         52 │ + → text-align:·center;
         53 │ + → white-space:·nowrap;
         54 │ + → -webkit-overflow-scrolling:·touch;
     55  55 │   }
     56  56 │
     57  57 │   .btn-bd-primary {
     58     │ - ··--bd-violet-bg:·#712cf9;
     59     │ - ··--bd-violet-rgb:·112.520718,·44.062154,·249.437846;
     60     │ - ··--bs-btn-font-weight:·600;
     61     │ - ··--bs-btn-color:·var(--bs-white);
     62     │ - ··--bs-btn-bg:·var(--bd-violet-bg);
     63     │ - ··--bs-btn-border-color:·var(--bd-violet-bg);
     64     │ - ··--bs-btn-hover-color:·var(--bs-white);
     65     │ - ··--bs-btn-hover-bg:·#6528e0;
     66     │ - ··--bs-btn-hover-border-color:·#6528e0;
     67     │ - ··--bs-btn-focus-shadow-rgb:·var(--bd-violet-rgb);
     68     │ - ··--bs-btn-active-color:·var(--bs-btn-hover-color);
     69     │ - ··--bs-btn-active-bg:·#5a23c8;
     70     │ - ··--bs-btn-active-border-color:·#5a23c8;
         58 │ + → --bd-violet-bg:·#712cf9;
         59 │ + → --bd-violet-rgb:·112.520718,·44.062154,·249.437846;
         60 │ + → --bs-btn-font-weight:·600;
         61 │ + → --bs-btn-color:·var(--bs-white);
         62 │ + → --bs-btn-bg:·var(--bd-violet-bg);
         63 │ + → --bs-btn-border-color:·var(--bd-violet-bg);
         64 │ + → --bs-btn-hover-color:·var(--bs-white);
         65 │ + → --bs-btn-hover-bg:·#6528e0;
         66 │ + → --bs-btn-hover-border-color:·#6528e0;
         67 │ + → --bs-btn-focus-shadow-rgb:·var(--bd-violet-rgb);
         68 │ + → --bs-btn-active-color:·var(--bs-btn-hover-color);
         69 │ + → --bs-btn-active-bg:·#5a23c8;
         70 │ + → --bs-btn-active-border-color:·#5a23c8;
     71  71 │   }
     72  72 │
     73  73 │   .bd-mode-toggle {
     74     │ - ··z-index:·1500;
         74 │ + → z-index:·1500;
     75  75 │   }
     76  76 │
     77  77 │   .bd-mode-toggle .dropdown-menu .active .bi {
     78     │ - ··display:·block·!important;
         78 │ + → display:·block·!important;
     79  79 │   }
     80  80 │
     81  81 │   .btn-qr-primary {
     82     │ - ··border-radius:·50%;
     83     │ - ··border-color:·black;
     84     │ - ··font-weight:·600;
     85     │ - ··min-height:·2.5em;
         82 │ + → border-radius:·50%;
         83 │ + → border-color:·black;
         84 │ + → font-weight:·600;
         85 │ + → min-height:·2.5em;
     86  86 │   }
     87  87 │
     88  88 │   .btn-qr-primary:hover {
     89     │ - ··background-color:·black;
     90     │ - ··color:·white;
         89 │ + → background-color:·black;
         90 │ + → color:·white;
     91  91 │   }
     92  92 │
    ······· │
    174 174 │   img.source-icon,
    175 175 │   img.source-qrcode {
    176     │ - ··max-height:·15em;
    177     │ - ··min-height:·15em;
    178     │ - ··min-width:·15em;
  24 more lines truncated


assets/dist/css/bootstrap.min.css format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

        6     6 │   :root,
        7     7 │   [data-bs-theme="light"] {
        8       │ - ··--bs-blue:·#0d6efd;
        9       │ - ··--bs-indigo:·#6610f2;
       10       │ - ··--bs-purple:·#6f42c1;
       11       │ - ··--bs-pink:·#d63384;
       12       │ - ··--bs-red:·#dc3545;
       13       │ - ··--bs-orange:·#fd7e14;
       14       │ - ··--bs-yellow:·#ffc107;
       15       │ - ··--bs-green:·#198754;
       16       │ - ··--bs-teal:·#20c997;
       17       │ - ··--bs-cyan:·#0dcaf0;
       18       │ - ··--bs-black:·#000;
       19       │ - ··--bs-white:·#fff;
       20       │ - ··--bs-gray:·#6c757d;
       21       │ - ··--bs-gray-dark:·#343a40;
       22       │ - ··--bs-gray-100:·#f8f9fa;
       23       │ - ··--bs-gray-200:·#e9ecef;
       24       │ - ··--bs-gray-300:·#dee2e6;
       25       │ - ··--bs-gray-400:·#ced4da;
       26       │ - ··--bs-gray-500:·#adb5bd;
       27       │ - ··--bs-gray-600:·#6c757d;
       28       │ - ··--bs-gray-700:·#495057;
       29       │ - ··--bs-gray-800:·#343a40;
       30       │ - ··--bs-gray-900:·#212529;
       31       │ - ··--bs-primary:·#0d6efd;
       32       │ - ··--bs-secondary:·#6c757d;
       33       │ - ··--bs-success:·#198754;
       34       │ - ··--bs-info:·#0dcaf0;
       35       │ - ··--bs-warning:·#ffc107;
       36       │ - ··--bs-danger:·#dc3545;
       37       │ - ··--bs-light:·#f8f9fa;
       38       │ - ··--bs-dark:·#212529;
       39       │ - ··--bs-primary-rgb:·13,·110,·253;
       40       │ - ··--bs-secondary-rgb:·108,·117,·125;
       41       │ - ··--bs-success-rgb:·25,·135,·84;
       42       │ - ··--bs-info-rgb:·13,·202,·240;
       43       │ - ··--bs-warning-rgb:·255,·193,·7;
       44       │ - ··--bs-danger-rgb:·220,·53,·69;
       45       │ - ··--bs-light-rgb:·248,·249,·250;
       46       │ - ··--bs-dark-rgb:·33,·37,·41;
       47       │ - ··--bs-primary-text-emphasis:·#052c65;
       48       │ - ··--bs-secondary-text-emphasis:·#2b2f32;
       49       │ - ··--bs-success-text-emphasis:·#0a3622;
       50       │ - ··--bs-info-text-emphasis:·#055160;
       51       │ - ··--bs-warning-text-emphasis:·#664d03;
       52       │ - ··--bs-danger-text-emphasis:·#58151c;
       53       │ - ··--bs-light-text-emphasis:·#495057;
       54       │ - ··--bs-dark-text-emphasis:·#495057;
       55       │ - ··--bs-primary-bg-subtle:·#cfe2ff;
       56       │ - ··--bs-secondary-bg-subtle:·#e2e3e5;
       57       │ - ··--bs-success-bg-subtle:·#d1e7dd;
       58       │ - ··--bs-info-bg-subtle:·#cff4fc;
       59       │ - ··--bs-warning-bg-subtle:·#fff3cd;
       60       │ - ··--bs-danger-bg-subtle:·#f8d7da;
       61       │ - ··--bs-light-bg-subtle:·#fcfcfd;
       62       │ - ··--bs-dark-bg-subtle:·#ced4da;
       63       │ - ··--bs-primary-border-subtle:·#9ec5fe;
       64       │ - ··--bs-secondary-border-subtle:·#c4c8cb;
       65       │ - ··--bs-success-border-subtle:·#a3cfbb;
       66       │ - ··--bs-info-border-subtle:·#9eeaf9;
       67       │ - ··--bs-warning-border-subtle:·#ffe69c;
       68       │ - ··--bs-danger-border-subtle:·#f1aeb5;
       69       │ - ··--bs-light-border-subtle:·#e9ecef;
       70       │ - ··--bs-dark-border-subtle:·#adb5bd;
       71       │ - ··--bs-white-rgb:·255,·255,·255;
       72       │ - ··--bs-black-rgb:·0,·0,·0;
       73       │ - ··--bs-font-sans-serif:·system-ui,·-apple-system,·"Segoe·UI",·roboto,
       74       │ - ····"Helvetica·Neue",·"Noto·Sans",·"Liberation·Sans",·arial,·sans-serif,
       75       │ - ····"Apple·Color·Emoji",·"Segoe·UI·Emoji",·"Segoe·UI·Symbol",·"Noto·Color·Emoji";
       76       │ - ··--bs-font-monospace:·sfmono-regular,·menlo,·monaco,·consolas,
       77       │ - ····"Liberation·Mono",·"Courier·New",·monospace;
       78       │ - ··--bs-gradient:·linear-gradient(
       79       │ - ····180deg,
       80       │ - ····rgb(255·255·255·/·15%),
       81       │ - ····rgb(255·255·255·/·0%)
       82       │ - ··);
       83       │ - ··--bs-body-font-family:·var(--bs-font-sans-serif);
       84       │ - ··--bs-body-font-size:·1rem;
       85       │ - ··--bs-body-font-weight:·400;
       86       │ - ··--bs-body-line-height:·1.5;
       87       │ - ··--bs-body-color:·#212529;
       88       │ - ··--bs-body-color-rgb:·33,·37,·41;
       89       │ - ··--bs-body-bg:·#fff;
       90       │ - ··--bs-body-bg-rgb:·255,·255,·255;
       91       │ - ··--bs-emphasis-color:·#000;
       92       │ - ··--bs-emphasis-color-rgb:·0,·0,·0;
       93       │ - ··--bs-secondary-color:·rgb(33·37·41·/·75%);
       94       │ - ··--bs-secondary-color-rgb:·33,·37,·41;
       95       │ - ··--bs-secondary-bg:·#e9ecef;
       96       │ - ··--bs-secondary-bg-rgb:·233,·236,·239;
       97       │ - ··--bs-tertiary-color:·rgb(33·37·41·/·50%);
       98       │ - ··--bs-tertiary-color-rgb:·33,·37,·41;
       99       │ - ··--bs-tertiary-bg:·#f8f9fa;
      100       │ - ··--bs-tertiary-bg-rgb:·248,·249,·250;
      101       │ - ··--bs-heading-color:·inherit;
      102       │ - ··--bs-link-color:·#0d6efd;
      103       │ - ··--bs-link-color-rgb:·13,·110,·253;
      104       │ - ··--bs-link-decoration:·underline;
      105       │ - ··--bs-link-hover-color:·#0a58ca;
      106       │ - ··--bs-link-hover-color-rgb:·10,·88,·202;
      107       │ - ··--bs-code-color:·#d63384;
      108       │ - ··--bs-highlight-color:·#212529;
      109       │ - ··--bs-highlight-bg:·#fff3cd;
      110       │ - ··--bs-border-width:·1px;
      111       │ - ··--bs-border-style:·solid;
      112       │ - ··--bs-border-color:·#dee2e6;
      113       │ - ··--bs-border-color-translucent:·rgb(0·0·0·/·17.5%);
      114       │ - ··--bs-border-radius:·0.375rem;
      115       │ - ··--bs-border-radius-sm:·0.25rem;
      116       │ - ··--bs-border-radius-lg:·0.5rem;
      117       │ - ··--bs-border-radius-xl:·1rem;
      118       │ - ··--bs-border-radius-xxl:·2rem;
      119       │ - ··--bs-border-radius-2xl:·var(--bs-border-radius-xxl);
      120       │ - ··--bs-border-radius-pill:·50rem;
      121       │ - ··--bs-box-shadow:·0·0.5rem·1rem·rgb(0·0·0·/·15%);
      122       │ - ··--bs-box-shadow-sm:·0·0.125rem·0.25rem·rgb(0·0·0·/·7.5%);
      123       │ - ··--bs-box-shadow-lg:·0·1rem·3rem·rgb(0·0·0·/·17.5%);
      124       │ - ··--bs-box-shadow-inset:·inset·0·1px·2px·rgb(0·0·0·/·7.5%);
      125       │ - ··--bs-focus-ring-width:·0.25rem;
      126       │ - ··--bs-focus-ring-opacity:·0.25;
      127       │ - ··--bs-focus-ring-color:·rgb(13·110·253·/·25%);
      128       │ - ··--bs-form-valid-color:·#198754;
      129       │ - ··--bs-form-valid-border-color:·#198754;
      130       │ - ··--bs-form-invalid-color:·#dc3545;
      131       │ - ··--bs-form-invalid-border-color:·#dc3545;
              8 │ + → --bs-blue:·#0d6efd;
              9 │ + → --bs-indigo:·#6610f2;
             10 │ + → --bs-purple:·#6f42c1;
             11 │ + → --bs-pink:·#d63384;
             12 │ + → --bs-red:·#dc3545;
             13 │ + → --bs-orange:·#fd7e14;
             14 │ + → --bs-yellow:·#ffc107;
             15 │ + → --bs-green:·#198754;
             16 │ + → --bs-teal:·#20c997;
             17 │ + → --bs-cyan:·#0dcaf0;
             18 │ + → --bs-black:·#000;
             19 │ + → --bs-white:·#fff;
             20 │ + → --bs-gray:·#6c757d;
             21 │ + → --bs-gray-dark:·#343a40;
             22 │ + → --bs-gray-100:·#f8f9fa;
             23 │ + → --bs-gray-200:·#e9ecef;
             24 │ + → --bs-gray-300:·#dee2e6;
             25 │ + → --bs-gray-400:·#ced4da;
             26 │ + → --bs-gray-500:·#adb5bd;
             27 │ + → --bs-gray-600:·#6c757d;
             28 │ + → --bs-gray-700:·#495057;
             29 │ + → --bs-gray-800:·#343a40;
             30 │ + → --bs-gray-900:·#212529;
             31 │ + → --bs-primary:·#0d6efd;
  20352 more lines truncated


assets/dist/css/bootstrap.rtl.min.css format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

        6     6 │   :root,
        7     7 │   [data-bs-theme="light"] {
        8       │ - ··--bs-blue:·#0d6efd;
        9       │ - ··--bs-indigo:·#6610f2;
       10       │ - ··--bs-purple:·#6f42c1;
       11       │ - ··--bs-pink:·#d63384;
       12       │ - ··--bs-red:·#dc3545;
       13       │ - ··--bs-orange:·#fd7e14;
       14       │ - ··--bs-yellow:·#ffc107;
       15       │ - ··--bs-green:·#198754;
       16       │ - ··--bs-teal:·#20c997;
       17       │ - ··--bs-cyan:·#0dcaf0;
       18       │ - ··--bs-black:·#000;
       19       │ - ··--bs-white:·#fff;
       20       │ - ··--bs-gray:·#6c757d;
       21       │ - ··--bs-gray-dark:·#343a40;
       22       │ - ··--bs-gray-100:·#f8f9fa;
       23       │ - ··--bs-gray-200:·#e9ecef;
       24       │ - ··--bs-gray-300:·#dee2e6;
       25       │ - ··--bs-gray-400:·#ced4da;
       26       │ - ··--bs-gray-500:·#adb5bd;
       27       │ - ··--bs-gray-600:·#6c757d;
       28       │ - ··--bs-gray-700:·#495057;
       29       │ - ··--bs-gray-800:·#343a40;
       30       │ - ··--bs-gray-900:·#212529;
       31       │ - ··--bs-primary:·#0d6efd;
       32       │ - ··--bs-secondary:·#6c757d;
       33       │ - ··--bs-success:·#198754;
       34       │ - ··--bs-info:·#0dcaf0;
       35       │ - ··--bs-warning:·#ffc107;
       36       │ - ··--bs-danger:·#dc3545;
       37       │ - ··--bs-light:·#f8f9fa;
       38       │ - ··--bs-dark:·#212529;
       39       │ - ··--bs-primary-rgb:·13,·110,·253;
       40       │ - ··--bs-secondary-rgb:·108,·117,·125;
       41       │ - ··--bs-success-rgb:·25,·135,·84;
       42       │ - ··--bs-info-rgb:·13,·202,·240;
       43       │ - ··--bs-warning-rgb:·255,·193,·7;
       44       │ - ··--bs-danger-rgb:·220,·53,·69;
       45       │ - ··--bs-light-rgb:·248,·249,·250;
       46       │ - ··--bs-dark-rgb:·33,·37,·41;
       47       │ - ··--bs-primary-text-emphasis:·#052c65;
       48       │ - ··--bs-secondary-text-emphasis:·#2b2f32;
       49       │ - ··--bs-success-text-emphasis:·#0a3622;
       50       │ - ··--bs-info-text-emphasis:·#055160;
       51       │ - ··--bs-warning-text-emphasis:·#664d03;
       52       │ - ··--bs-danger-text-emphasis:·#58151c;
       53       │ - ··--bs-light-text-emphasis:·#495057;
       54       │ - ··--bs-dark-text-emphasis:·#495057;
       55       │ - ··--bs-primary-bg-subtle:·#cfe2ff;
       56       │ - ··--bs-secondary-bg-subtle:·#e2e3e5;
       57       │ - ··--bs-success-bg-subtle:·#d1e7dd;
       58       │ - ··--bs-info-bg-subtle:·#cff4fc;
       59       │ - ··--bs-warning-bg-subtle:·#fff3cd;
       60       │ - ··--bs-danger-bg-subtle:·#f8d7da;
       61       │ - ··--bs-light-bg-subtle:·#fcfcfd;
       62       │ - ··--bs-dark-bg-subtle:·#ced4da;
       63       │ - ··--bs-primary-border-subtle:·#9ec5fe;
       64       │ - ··--bs-secondary-border-subtle:·#c4c8cb;
       65       │ - ··--bs-success-border-subtle:·#a3cfbb;
       66       │ - ··--bs-info-border-subtle:·#9eeaf9;
       67       │ - ··--bs-warning-border-subtle:·#ffe69c;
       68       │ - ··--bs-danger-border-subtle:·#f1aeb5;
       69       │ - ··--bs-light-border-subtle:·#e9ecef;
       70       │ - ··--bs-dark-border-subtle:·#adb5bd;
       71       │ - ··--bs-white-rgb:·255,·255,·255;
       72       │ - ··--bs-black-rgb:·0,·0,·0;
       73       │ - ··--bs-font-sans-serif:·system-ui,·-apple-system,·"Segoe·UI",·roboto,
       74       │ - ····"Helvetica·Neue",·"Noto·Sans",·"Liberation·Sans",·arial,·sans-serif,
       75       │ - ····"Apple·Color·Emoji",·"Segoe·UI·Emoji",·"Segoe·UI·Symbol",·"Noto·Color·Emoji";
       76       │ - ··--bs-font-monospace:·sfmono-regular,·menlo,·monaco,·consolas,
       77       │ - ····"Liberation·Mono",·"Courier·New",·monospace;
       78       │ - ··--bs-gradient:·linear-gradient(
       79       │ - ····180deg,
       80       │ - ····rgb(255·255·255·/·15%),
       81       │ - ····rgb(255·255·255·/·0%)
       82       │ - ··);
       83       │ - ··--bs-body-font-family:·var(--bs-font-sans-serif);
       84       │ - ··--bs-body-font-size:·1rem;
       85       │ - ··--bs-body-font-weight:·400;
       86       │ - ··--bs-body-line-height:·1.5;
       87       │ - ··--bs-body-color:·#212529;
       88       │ - ··--bs-body-color-rgb:·33,·37,·41;
       89       │ - ··--bs-body-bg:·#fff;
       90       │ - ··--bs-body-bg-rgb:·255,·255,·255;
       91       │ - ··--bs-emphasis-color:·#000;
       92       │ - ··--bs-emphasis-color-rgb:·0,·0,·0;
       93       │ - ··--bs-secondary-color:·rgb(33·37·41·/·75%);
       94       │ - ··--bs-secondary-color-rgb:·33,·37,·41;
       95       │ - ··--bs-secondary-bg:·#e9ecef;
       96       │ - ··--bs-secondary-bg-rgb:·233,·236,·239;
       97       │ - ··--bs-tertiary-color:·rgb(33·37·41·/·50%);
       98       │ - ··--bs-tertiary-color-rgb:·33,·37,·41;
       99       │ - ··--bs-tertiary-bg:·#f8f9fa;
      100       │ - ··--bs-tertiary-bg-rgb:·248,·249,·250;
      101       │ - ··--bs-heading-color:·inherit;
      102       │ - ··--bs-link-color:·#0d6efd;
      103       │ - ··--bs-link-color-rgb:·13,·110,·253;
      104       │ - ··--bs-link-decoration:·underline;
      105       │ - ··--bs-link-hover-color:·#0a58ca;
      106       │ - ··--bs-link-hover-color-rgb:·10,·88,·202;
      107       │ - ··--bs-code-color:·#d63384;
      108       │ - ··--bs-highlight-color:·#212529;
      109       │ - ··--bs-highlight-bg:·#fff3cd;
      110       │ - ··--bs-border-width:·1px;
      111       │ - ··--bs-border-style:·solid;
      112       │ - ··--bs-border-color:·#dee2e6;
      113       │ - ··--bs-border-color-translucent:·rgb(0·0·0·/·17.5%);
      114       │ - ··--bs-border-radius:·0.375rem;
      115       │ - ··--bs-border-radius-sm:·0.25rem;
      116       │ - ··--bs-border-radius-lg:·0.5rem;
      117       │ - ··--bs-border-radius-xl:·1rem;
      118       │ - ··--bs-border-radius-xxl:·2rem;
      119       │ - ··--bs-border-radius-2xl:·var(--bs-border-radius-xxl);
      120       │ - ··--bs-border-radius-pill:·50rem;
      121       │ - ··--bs-box-shadow:·0·0.5rem·1rem·rgb(0·0·0·/·15%);
      122       │ - ··--bs-box-shadow-sm:·0·0.125rem·0.25rem·rgb(0·0·0·/·7.5%);
      123       │ - ··--bs-box-shadow-lg:·0·1rem·3rem·rgb(0·0·0·/·17.5%);
      124       │ - ··--bs-box-shadow-inset:·inset·0·1px·2px·rgb(0·0·0·/·7.5%);
      125       │ - ··--bs-focus-ring-width:·0.25rem;
      126       │ - ··--bs-focus-ring-opacity:·0.25;
      127       │ - ··--bs-focus-ring-color:·rgb(13·110·253·/·25%);
      128       │ - ··--bs-form-valid-color:·#198754;
      129       │ - ··--bs-form-valid-border-color:·#198754;
      130       │ - ··--bs-form-invalid-color:·#dc3545;
      131       │ - ··--bs-form-invalid-border-color:·#dc3545;
              8 │ + → --bs-blue:·#0d6efd;
              9 │ + → --bs-indigo:·#6610f2;
             10 │ + → --bs-purple:·#6f42c1;
             11 │ + → --bs-pink:·#d63384;
             12 │ + → --bs-red:·#dc3545;
             13 │ + → --bs-orange:·#fd7e14;
             14 │ + → --bs-yellow:·#ffc107;
             15 │ + → --bs-green:·#198754;
             16 │ + → --bs-teal:·#20c997;
             17 │ + → --bs-cyan:·#0dcaf0;
             18 │ + → --bs-black:·#000;
             19 │ + → --bs-white:·#fff;
             20 │ + → --bs-gray:·#6c757d;
             21 │ + → --bs-gray-dark:·#343a40;
             22 │ + → --bs-gray-100:·#f8f9fa;
             23 │ + → --bs-gray-200:·#e9ecef;
             24 │ + → --bs-gray-300:·#dee2e6;
             25 │ + → --bs-gray-400:·#ced4da;
             26 │ + → --bs-gray-500:·#adb5bd;
             27 │ + → --bs-gray-600:·#6c757d;
             28 │ + → --bs-gray-700:·#495057;
             29 │ + → --bs-gray-800:·#343a40;
             30 │ + → --bs-gray-900:·#212529;
             31 │ + → --bs-primary:·#0d6efd;
  20352 more lines truncated


assets/dist/js/bootstrap.bundle.min.js format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

       5    5 │    */
       6    6 │   !(function (t, e) {
       7      │ - ··"object"·==·typeof·exports·&&·"undefined"·!=·typeof·module
       8      │ - ····?·(module.exports·=·e())
       9      │ - ····:·"function"·==·typeof·define·&&·define.amd
      10      │ - ······?·define(e)
      11      │ - ······:·((t·=
      12      │ - ··········"undefined"·!=·typeof·globalThis·?·globalThis·:·t·||·self).bootstrap·=
      13      │ - ··········e());
            7 │ + → "object"·==·typeof·exports·&&·"undefined"·!=·typeof·module
            8 │ + → → ?·(module.exports·=·e())
            9 │ + → → :·"function"·==·typeof·define·&&·define.amd
           10 │ + → → → ?·define(e)
           11 │ + → → → :·((t·=
           12 │ + → → → → → "undefined"·!=·typeof·globalThis·?·globalThis·:·t·||·self).bootstrap·=
           13 │ + → → → → → e());
      14   14 │   })(this, function () {
      15      │ - ··"use·strict";
      16      │ - ··const·t·=·new·Map(),
      17      │ - ····e·=·{
      18      │ - ······set(e,·i,·n)·{
      19      │ - ········t.has(e)·||·t.set(e,·new·Map());
      20      │ - ········const·s·=·t.get(e);
      21      │ - ········s.has(i)·||·0·===·s.size
      22      │ - ··········?·s.set(i,·n)
      23      │ - ··········:·console.error(
      24      │ - ··············`Bootstrap·doesn't·allow·more·than·one·instance·per·element.·Bound·instance:·${Array.from(s.keys())[0]}.`,
      25      │ - ············);
      26      │ - ······},
      27      │ - ······get:·(e,·i)·=>·(t.has(e)·&&·t.get(e).get(i))·||·null,
      28      │ - ······remove(e,·i)·{
      29      │ - ········if·(!t.has(e))·return;
      30      │ - ········const·n·=·t.get(e);
      31      │ - ········n.delete(i),·0·===·n.size·&&·t.delete(e);
      32      │ - ······},
      33      │ - ····},
      34      │ - ····i·=·"transitionend",
      35      │ - ····n·=·(t)·=>·(
      36      │ - ······t·&&
      37      │ - ········window.CSS·&&
      38      │ - ········window.CSS.escape·&&
      39      │ - ········(t·=·t.replace(/#([^\s"#']+)/g,·(t,·e)·=>·`#${CSS.escape(e)}`)),
      40      │ - ······t
      41      │ - ····),
      42      │ - ····s·=·(t)·=>·{
      43      │ - ······t.dispatchEvent(new·Event(i));
      44      │ - ····},
      45      │ - ····o·=·(t)·=>
      46      │ - ······!(!t·||·"object"·!=·typeof·t)·&&
      47      │ - ······(void·0·!==·t.jquery·&&·(t·=·t[0]),·void·0·!==·t.nodeType),
      48      │ - ····r·=·(t)·=>
      49      │ - ······o(t)
      50      │ - ········?·t.jquery
      51      │ - ··········?·t[0]
      52      │ - ··········:·t
      53      │ - ········:·"string"·==·typeof·t·&&·t.length·>·0
      54      │ - ··········?·document.querySelector(n(t))
      55      │ - ··········:·null,
      56      │ - ····a·=·(t)·=>·{
      57      │ - ······if·(!o(t)·||·0·===·t.getClientRects().length)·return·!1;
      58      │ - ······const·e·=
      59      │ - ··········"visible"·===·getComputedStyle(t).getPropertyValue("visibility"),
      60      │ - ········i·=·t.closest("details:not([open])");
      61      │ - ······if·(!i)·return·e;
      62      │ - ······if·(i·!==·t)·{
      63      │ - ········const·e·=·t.closest("summary");
      64      │ - ········if·(e·&&·e.parentNode·!==·i)·return·!1;
      65      │ - ········if·(null·===·e)·return·!1;
      66      │ - ······}
      67      │ - ······return·e;
      68      │ - ····},
      69      │ - ····l·=·(t)·=>
      70      │ - ······!t·||
      71      │ - ······t.nodeType·!==·Node.ELEMENT_NODE·||
      72      │ - ······!!t.classList.contains("disabled")·||
      73      │ - ······(void·0·!==·t.disabled
      74      │ - ········?·t.disabled
      75      │ - ········:·t.hasAttribute("disabled")·&&·"false"·!==·t.getAttribute("disabled")),
      76      │ - ····c·=·(t)·=>·{
      77      │ - ······if·(!document.documentElement.attachShadow)·return·null;
      78      │ - ······if·("function"·==·typeof·t.getRootNode)·{
      79      │ - ········const·e·=·t.getRootNode();
      80      │ - ········return·e·instanceof·ShadowRoot·?·e·:·null;
      81      │ - ······}
      82      │ - ······return·t·instanceof·ShadowRoot
      83      │ - ········?·t
      84      │ - ········:·t.parentNode
      85      │ - ··········?·c(t.parentNode)
      86      │ - ··········:·null;
      87      │ - ····},
      88      │ - ····h·=·()·=>·{},
      89      │ - ····d·=·(t)·=>·{
      90      │ - ······t.offsetHeight;
      91      │ - ····},
      92      │ - ····u·=·()·=>
      93      │ - ······window.jQuery·&&·!document.body.hasAttribute("data-bs-no-jquery")
      94      │ - ········?·window.jQuery
      95      │ - ········:·null,
      96      │ - ····f·=·[],
      97      │ - ····p·=·()·=>·"rtl"·===·document.documentElement.dir,
      98      │ - ····m·=·(t)·=>·{
      99      │ - ······var·e;
     100      │ - ······(e·=·()·=>·{
     101      │ - ········const·e·=·u();
     102      │ - ········if·(e)·{
     103      │ - ··········const·i·=·t.NAME,
     104      │ - ············n·=·e.fn[i];
     105      │ - ··········(e.fn[i]·=·t.jQueryInterface),
     106      │ - ············(e.fn[i].Constructor·=·t),
     107      │ - ············(e.fn[i].noConflict·=·()·=>·((e.fn[i]·=·n),·t.jQueryInterface));
     108      │ - ········}
     109      │ - ······}),
     110      │ - ········"loading"·===·document.readyState
     111      │ - ··········?·(f.length·||
     112      │ - ··············document.addEventListener("DOMContentLoaded",·()·=>·{
     113      │ - ················for·(const·t·of·f)·t();
     114      │ - ··············}),
     115      │ - ············f.push(e))
     116      │ - ··········:·e();
     117      │ - ····},
     118      │ - ····g·=·(t,·e·=·[],·i·=·t)·=>·("function"·==·typeof·t·?·t(...e)·:·i),
     119      │ - ····_·=·(t,·e,·n·=·!0)·=>·{
     120      │ - ······if·(!n)·return·void·g(t);
     121      │ - ······const·o·=
     122      │ - ········((t)·=>·{
     123      │ - ··········if·(!t)·return·0;
     124      │ - ··········let·{·transitionDuration:·e,·transitionDelay:·i·}·=
     125      │ - ············window.getComputedStyle(t);
     126      │ - ··········const·n·=·Number.parseFloat(e),
     127      │ - ············s·=·Number.parseFloat(i);
     128      │ - ··········return·n·||·s
     129      │ - ············?·((e·=·e.split(",")[0]),
     130      │ - ··············(i·=·i.split(",")[0]),
     131      │ - ··············1e3·*·(Number.parseFloat(e)·+·Number.parseFloat(i)))
     132      │ - ············:·0;
     133      │ - ········})(e)·+·5;
     134      │ - ······let·r·=·!1;
     135      │ - ······const·a·=·({·target:·n·})·=>·{
     136      │ - ········n·===·e·&&·((r·=·!0),·e.removeEventListener(i,·a),·g(t));
     137      │ - ······};
     138      │ - ······e.addEventListener(i,·a),
     139      │ - ········setTimeout(()·=>·{
     140      │ - ··········r·||·s(e);
     141      │ - ········},·o);
     142      │ - ····},
     143      │ - ····b·=·(t,·e,·i,·n)·=>·{
     144      │ - ······const·s·=·t.length;
     145      │ - ······let·o·=·t.indexOf(e);
     146      │ - ······return·-1·===·o
     147      │ - ········?·!i·&&·n
  8288 more lines truncated


assets/js/color-modes.js format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

     6  6 │
     7  7 │   (() => {
     8    │ - ··'use·strict'
        8 │ + → "use·strict";
     9  9 │
    10    │ - ··const·getStoredTheme·=·()·=>·localStorage.getItem('theme')
    11    │ - ··const·setStoredTheme·=·(theme)·=>·localStorage.setItem('theme',·theme)
       10 │ + → const·getStoredTheme·=·()·=>·localStorage.getItem("theme");
       11 │ + → const·setStoredTheme·=·(theme)·=>·localStorage.setItem("theme",·theme);
    12 12 │
    13    │ - ··const·getPreferredTheme·=·()·=>·{
    14    │ - ····const·storedTheme·=·getStoredTheme()
    15    │ - ····if·(storedTheme)·{
    16    │ - ······return·storedTheme
    17    │ - ····}
       13 │ + → const·getPreferredTheme·=·()·=>·{
       14 │ + → → const·storedTheme·=·getStoredTheme();
       15 │ + → → if·(storedTheme)·{
       16 │ + → → → return·storedTheme;
       17 │ + → → }
    18 18 │
    19    │ - ····return·window.matchMedia('(prefers-color-scheme:·dark)').matches
    20    │ - ······?·'dark'
    21    │ - ······:·'light'
    22    │ - ··}
       19 │ + → → return·window.matchMedia("(prefers-color-scheme:·dark)").matches
       20 │ + → → → ?·"dark"
       21 │ + → → → :·"light";
       22 │ + → };
    23 23 │
    24    │ - ··const·setTheme·=·(theme)·=>·{
    25    │ - ····if·(theme·===·'auto')·{
    26    │ - ······document.documentElement.setAttribute(
    27    │ - ········'data-bs-theme',
    28    │ - ········window.matchMedia('(prefers-color-scheme:·dark)').matches
    29    │ - ··········?·'dark'
    30    │ - ··········:·'light'
    31    │ - ······)
    32    │ - ····}·else·{
    33    │ - ······document.documentElement.setAttribute('data-bs-theme',·theme)
    34    │ - ····}
    35    │ - ··}
       24 │ + → const·setTheme·=·(theme)·=>·{
       25 │ + → → if·(theme·===·"auto")·{
       26 │ + → → → document.documentElement.setAttribute(
       27 │ + → → → → "data-bs-theme",
       28 │ + → → → → window.matchMedia("(prefers-color-scheme:·dark)").matches
       29 │ + → → → → → ?·"dark"
       30 │ + → → → → → :·"light",
       31 │ + → → → );
       32 │ + → → }·else·{
       33 │ + → → → document.documentElement.setAttribute("data-bs-theme",·theme);
       34 │ + → → }
       35 │ + → };
    36 36 │
    37    │ - ··setTheme(getPreferredTheme())
       37 │ + → setTheme(getPreferredTheme());
    38 38 │
    39    │ - ··const·showActiveTheme·=·(theme,·focus·=·false)·=>·{
    40    │ - ····const·themeSwitcher·=·document.querySelector('#bd-theme')
       39 │ + → const·showActiveTheme·=·(theme,·focus·=·false)·=>·{
       40 │ + → → const·themeSwitcher·=·document.querySelector("#bd-theme");
    41 41 │
    42    │ - ····if·(!themeSwitcher)·{
    43    │ - ······return
    44    │ - ····}
       42 │ + → → if·(!themeSwitcher)·{
       43 │ + → → → return;
       44 │ + → → }
    45 45 │
    46    │ - ····const·themeSwitcherText·=·document.querySelector('#bd-theme-text')
    47    │ - ····const·activeThemeIcon·=·document.querySelector('.theme-icon-active·use')
    48    │ - ····const·btnToActive·=·document.querySelector(
    49    │ - ······`[data-bs-theme-value="${theme}"]`
    50    │ - ····)
    51    │ - ····const·svgOfActiveBtn·=·btnToActive
    52    │ - ······.querySelector('svg·use')
    53    │ - ······.getAttribute('href')
       46 │ + → → const·themeSwitcherText·=·document.querySelector("#bd-theme-text");
       47 │ + → → const·activeThemeIcon·=·document.querySelector(".theme-icon-active·use");
       48 │ + → → const·btnToActive·=·document.querySelector(
       49 │ + → → → `[data-bs-theme-value="${theme}"]`,
       50 │ + → → );
       51 │ + → → const·svgOfActiveBtn·=·btnToActive
       52 │ + → → → .querySelector("svg·use")
       53 │ + → → → .getAttribute("href");
    54 54 │
    55    │ - ····document.querySelectorAll('[data-bs-theme-value]').forEach((element)·=>·{
    56    │ - ······element.classList.remove('active')
    57    │ - ······element.setAttribute('aria-pressed',·'false')
    58    │ - ····})
       55 │ + → → document.querySelectorAll("[data-bs-theme-value]").forEach((element)·=>·{
       56 │ + → → → element.classList.remove("active");
       57 │ + → → → element.setAttribute("aria-pressed",·"false");
       58 │ + → → });
    59 59 │
    60    │ - ····btnToActive.classList.add('active')
    61    │ - ····btnToActive.setAttribute('aria-pressed',·'true')
    62    │ - ····activeThemeIcon.setAttribute('href',·svgOfActiveBtn)
    63    │ - ····const·themeSwitcherLabel·=·`${themeSwitcherText.textContent}·(${btnToActive.dataset.bsThemeValue})`
    64    │ - ····themeSwitcher.setAttribute('aria-label',·themeSwitcherLabel)
       60 │ + → → btnToActive.classList.add("active");
       61 │ + → → btnToActive.setAttribute("aria-pressed",·"true");
       62 │ + → → activeThemeIcon.setAttribute("href",·svgOfActiveBtn);
       63 │ + → → const·themeSwitcherLabel·=·`${themeSwitcherText.textContent}·(${btnToActive.dataset.bsThemeValue})`;
       64 │ + → → themeSwitcher.setAttribute("aria-label",·themeSwitcherLabel);
    65 65 │
    66    │ - ····if·(focus)·{
    67    │ - ······themeSwitcher.focus()
    68    │ - ····}
    69    │ - ··}
       66 │ + → → if·(focus)·{
       67 │ + → → → themeSwitcher.focus();
       68 │ + → → }
       69 │ + → };
    70 70 │
    71    │ - ··window
    72    │ - ····.matchMedia('(prefers-color-scheme:·dark)')
    73    │ - ····.addEventListener('change',·()·=>·{
    74    │ - ······const·storedTheme·=·getStoredTheme()
    75    │ - ······if·(storedTheme·!==·'light'·&&·storedTheme·!==·'dark')·{
    76    │ - ········setTheme(getPreferredTheme())
    77    │ - ······}
    78    │ - ····})
       71 │ + → window
       72 │ + → → .matchMedia("(prefers-color-scheme:·dark)")
       73 │ + → → .addEventListener("change",·()·=>·{
       74 │ + → → → const·storedTheme·=·getStoredTheme();
       75 │ + → → → if·(storedTheme·!==·"light"·&&·storedTheme·!==·"dark")·{
       76 │ + → → → → setTheme(getPreferredTheme());
       77 │ + → → → }
       78 │ + → → });
    79 79 │
    80    │ - ··window.addEventListener('DOMContentLoaded',·()·=>·{
    81    │ - ····showActiveTheme(getPreferredTheme())
       80 │ + → window.addEventListener("DOMContentLoaded",·()·=>·{
       81 │ + → → showActiveTheme(getPreferredTheme());
    82 82 │
    83    │ - ····document.querySelectorAll('[data-bs-theme-value]').forEach((toggle)·=>·{
    84    │ - ······toggle.addEventListener('click',·()·=>·{
    85    │ - ········const·theme·=·toggle.getAttribute('data-bs-theme-value')
    86    │ - ········setStoredTheme(theme)
    87    │ - ········setTheme(theme)
    88    │ - ········showActiveTheme(theme,·true)
    89    │ - ······})
    90    │ - ····})
    91    │ - ··})
    92    │ - })()
       83 │ + → → document.querySelectorAll("[data-bs-theme-value]").forEach((toggle)·=>·{
       84 │ + → → → toggle.addEventListener("click",·()·=>·{
  9 more lines truncated


assets/js/site.js format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

      1   1 │   filters = {
      2     │ - ··nsfw:·"NSFW",
      3     │ - ··archived:·"Archived",
          2 │ + → nsfw:·"NSFW",
          3 │ + → archived:·"Archived",
      4   4 │   };
      5   5 │
      6   6 │   function varExists(value) {
      7     │ - ··return·value·!==·undefined·&&·value·!==·null·&&·value·!==·""·&&·value·!==·0;
          7 │ + → return·value·!==·undefined·&&·value·!==·null·&&·value·!==·""·&&·value·!==·0;
      8   8 │   }
      9   9 │   function removeLast(inputString, separator) {
     10     │ - ··if·(inputString·===·undefined·||·inputString·===·null)·return·"";
     11     │ - ··if·(separator·===·undefined·||·separator·===·null)·return·"";
     12     │ - ··const·lastIndex·=·inputString.lastIndexOf(separator);
     13     │ - ··if·(lastIndex·>·0)·return·inputString.substring(0,·lastIndex);
     14     │ - ··else·return·"";
         10 │ + → if·(inputString·===·undefined·||·inputString·===·null)·return·"";
         11 │ + → if·(separator·===·undefined·||·separator·===·null)·return·"";
         12 │ + → const·lastIndex·=·inputString.lastIndexOf(separator);
         13 │ + → if·(lastIndex·>·0)·return·inputString.substring(0,·lastIndex);
         14 │ + → else·return·"";
     15  15 │   }
     16  16 │   function isQueryParamSet(paramName) {
     17     │ - ··const·searchParams·=·new·URLSearchParams(window.location.search);
     18     │ - ··return·searchParams.has(paramName);
         17 │ + → const·searchParams·=·new·URLSearchParams(window.location.search);
         18 │ + → return·searchParams.has(paramName);
     19  19 │   }
     20  20 │   function isRelativeUrl(url) {
     21     │ - ··return·url.startsWith("./");
         21 │ + → return·url.startsWith("./");
     22  22 │   }
     23  23 │   function getAbsoluteUrl(url, baseUrl) {
     24     │ - ··if·(isRelativeUrl(url))·{
     25     │ - ····return·url.replace("./",·baseUrl);
     26     │ - ··}
     27     │ - ··return·url;
         24 │ + → if·(isRelativeUrl(url))·{
         25 │ + → → return·url.replace("./",·baseUrl);
         26 │ + → }
         27 │ + → return·url;
     28  28 │   }
     29  29 │   function setParams(params, navigate = true) {
     30     │ - ··const·url·=·new·URL(window.location.href);
     31     │ - ··const·setParam·=·(key,·value)·=>·{
     32     │ - ····if·(value·!==·undefined·&&·value·!==·null)·{
     33     │ - ······url.searchParams.set(key,·value.toString());
     34     │ - ····}·/*·if·(!url.searchParams.has(key))·*/·else·{
     35     │ - ······url.searchParams.set(key,·1);
     36     │ - ····}
     37     │ - ··};
     38     │ - ··if·(Array.isArray(params))·{
     39     │ - ····params.forEach(setParam);
     40     │ - ··}·else·if·(typeof·params·===·"object"·&&·params·!==·null)·{
     41     │ - ····Object.entries(params).forEach(setParam);
     42     │ - ··}·else·if·(typeof·params·===·"string")·{
     43     │ - ····const·[key,·value]·=·params.split("=");
     44     │ - ····setParam(key,·value);
     45     │ - ··}
     46     │ - ··console.log(`New·URL:·${url}`);
     47     │ - ··if·(navigate)·{
     48     │ - ····window.location.href·=·url;
     49     │ - ····window.location.replace(url);
     50     │ - ··}
     51     │ - ··return·url;
         30 │ + → const·url·=·new·URL(window.location.href);
         31 │ + → const·setParam·=·(key,·value)·=>·{
         32 │ + → → if·(value·!==·undefined·&&·value·!==·null)·{
         33 │ + → → → url.searchParams.set(key,·value.toString());
         34 │ + → → }·/*·if·(!url.searchParams.has(key))·*/·else·{
         35 │ + → → → url.searchParams.set(key,·1);
         36 │ + → → }
         37 │ + → };
         38 │ + → if·(Array.isArray(params))·{
         39 │ + → → params.forEach(setParam);
         40 │ + → }·else·if·(typeof·params·===·"object"·&&·params·!==·null)·{
         41 │ + → → Object.entries(params).forEach(setParam);
         42 │ + → }·else·if·(typeof·params·===·"string")·{
         43 │ + → → const·[key,·value]·=·params.split("=");
         44 │ + → → setParam(key,·value);
         45 │ + → }
         46 │ + → console.log(`New·URL:·${url}`);
         47 │ + → if·(navigate)·{
         48 │ + → → window.location.href·=·url;
         49 │ + → → window.location.replace(url);
         50 │ + → }
         51 │ + → return·url;
     52  52 │   }
     53  53 │
     54  54 │   function getSourceFeeds(data, key) {
     55     │ - ··const·urls·=·[];
     56     │ - ··data.forEach((item)·=>·{
     57     │ - ····if·(!item.hasOwnProperty("_feeds"))·return;
     58     │ - ····if·(item._feeds.hasOwnProperty(key))·{
     59     │ - ······urls.push(encodeURI(item._feeds[key]));
     60     │ - ····}
     61     │ - ····//·else·console.warn(`Source·${item.name}·has·no·${key}`);
     62     │ - ··});
     63     │ - ··console.log("URLs:",·urls);·//·Log·encoded·URLs
     64     │ - ··const·urlCount·=·urls.length;
     65     │ - ··const·baseUrl·=·"https://rssmerge.onrender.com";·//·Use·the·current·page's·origin·as·the·base·URL
     66     │ - ··console.log("Base·URL:",·baseUrl);·//·Log·base·URL
     67     │ - ··const·params·=·new·URLSearchParams({
     68     │ - ····title:·`${urlCount}·${key}`,
     69     │ - ····urls:·urls.join(","),
     70     │ - ··}).toString();
     71     │ - ··const·finalUrl·=·`${baseUrl}/?${params}`;
     72     │ - ··console.log("Final·URL:",·finalUrl);·//·Log·final·URL
     73     │ - ··return·finalUrl;
         55 │ + → const·urls·=·[];
         56 │ + → data.forEach((item)·=>·{
         57 │ + → → if·(!item.hasOwnProperty("_feeds"))·return;
         58 │ + → → if·(item._feeds.hasOwnProperty(key))·{
         59 │ + → → → urls.push(encodeURI(item._feeds[key]));
         60 │ + → → }
         61 │ + → → //·else·console.warn(`Source·${item.name}·has·no·${key}`);
         62 │ + → });
         63 │ + → console.log("URLs:",·urls);·//·Log·encoded·URLs
         64 │ + → const·urlCount·=·urls.length;
         65 │ + → const·baseUrl·=·"https://rssmerge.onrender.com";·//·Use·the·current·page's·origin·as·the·base·URL
         66 │ + → console.log("Base·URL:",·baseUrl);·//·Log·base·URL
         67 │ + → const·params·=·new·URLSearchParams({
         68 │ + → → title:·`${urlCount}·${key}`,
         69 │ + → → urls:·urls.join(","),
         70 │ + → }).toString();
         71 │ + → const·finalUrl·=·`${baseUrl}/?${params}`;
         72 │ + → console.log("Final·URL:",·finalUrl);·//·Log·final·URL
         73 │ + → return·finalUrl;
     74  74 │   }
     75  75 │   function fixData(data) {
     76     │ - ··if·(varExists(data.scriptUrl))·{
     77     │ - ····data.baseUrl·=·removeLast(data.sourceUrl,·"/")·+·"/";
     78     │ - ··}
     79     │ - ··if·(!data.hasOwnProperty("_feeds"))·data._feeds·=·{};
     80     │ - ··if·(!data.hasOwnProperty("_tags"))·data._tags·=·[];
     81     │ - ··for·(const·[key,·value]·of·Object.entries(data))·{
     82     │ - ····if·(key.toLowerCase().includes("url"))·{
     83     │ - ······if·(Array.isArray(value))·continue;
     84     │ - ······if·(isRelativeUrl(value))·{
     85     │ - ········data[key·+·"_"]·=·value;
     86     │ - ········data[key]·=·getAbsoluteUrl(value,·data.baseUrl);
     87     │ - ······}
     88     │ - ····}
     89     │ - ··}
     90     │ - ··console.log(data);
     91     │ - ··return·data;
         76 │ + → if·(varExists(data.scriptUrl))·{
         77 │ + → → data.baseUrl·=·removeLast(data.sourceUrl,·"/")·+·"/";
         78 │ + → }
  344 more lines truncated


sources.json format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

       1    1 │   [
       2      │ - ····{
       3      │ - ········"_tags":·[
       4      │ - ············"unofficial",
       5      │ - ············"untested"
       6      │ - ········],
       7      │ - ········"name":·"Adventures·in·Odyssey·Club",
       8      │ - ········"description":·"Subscription·service·for·the·award-winning,·original·audio·drama·series·enjoyed·by·the·whole·family.",
       9      │ - ········"author":·"CATEIN",
      10      │ - ········"authorUrl":·"https://catein.xyz",
      11      │ - ········"sourceUrl":·"https://raw.githubusercontent.com/CATEIN/adventures-in-odyssey-club-plugin/refs/heads/main/AdventuresInOdysseyClubConfig.json",
      12      │ - ········"repositoryUrl":·"https://github.com/CATEIN/adventures-in-odyssey-club-plugin",
      13      │ - ········"scriptUrl":·"./AIOScript.js",
      14      │ - ········"version":·14,
      15      │ - ········"iconUrl":·"./AIOC.png",
      16      │ - ········"id":·"62e186ef-160d-46d7-9953-74fe84d11b40",
      17      │ - ········"scriptSignature":·"",
      18      │ - ········"scriptPublicKey":·"",
      19      │ - ········"packages":·[
      20      │ - ············"Http"
      21      │ - ········],
      22      │ - ········"allowEval":·false,
      23      │ - ········"allowUrls":·[
      24      │ - ············"fotf.my.site.com"
      25      │ - ········],
      26      │ - ········"authentication":·{
      27      │ - ············"loginUrl":·"https://app.adventuresinodyssey.com/signin",
      28      │ - ············"domainHeadersToFind":·{
      29      │ - ················"fotf.my.site.com":·[
      30      │ - ····················"Authorization",
      31      │ - ····················"x-viewer-id",
      32      │ - ····················"x-pin"
      33      │ - ················]
      34      │ - ············},
      35      │ - ············"cookiesToFind":·[
      36      │ - ················"idccsrf"
      37      │ - ············],
      38      │ - ············"loginWarning":·"You·must·select·a·profile·with·a·PIN·for·authentication·to·complete."
      39      │ - ········},
      40      │ - ········"settings":·[
      41      │ - ············{
      42      │ - ················"variable":·"podcasts",
      43      │ - ················"name":·"Podcasts",
      44      │ - ················"description":·"Show·new·podcasts·in·subscription·feed",
      45      │ - ················"type":·"Boolean",
      46      │ - ················"default":·"false"
      47      │ - ············},
      48      │ - ············{
      49      │ - ················"variable":·"fetchRandomEpisode",
      50      │ - ················"name":·"Randomizer·via·Recommended",
      51      │ - ················"description":·"Puts·a·random·episode·at·the·top·of·recommendations·(Recommendations·may·take·longer·to·load)",
      52      │ - ················"type":·"Boolean",
      53      │ - ················"default":·"false"
      54      │ - ············},
      55      │ - ············{
      56      │ - ················"variable":·"fasterRandom",
      57      │ - ················"name":·"Faster·Randomizer",
      58      │ - ················"description":·"Cache·episodes·instead·of·using·the·random·API.·Might·not·include·the·newest·episodes.·Default·when·not·logged·in.",
      59      │ - ················"type":·"Boolean",
      60      │ - ················"default":·"false",
      61      │ - ················"dependency":·"fetchRandomEpisode"
      62      │ - ············},
      63      │ - ············{
      64      │ - ················"variable":·"groupings",
      65      │ - ················"name":·"Content·Groupings",
      66      │ - ················"description":·"Choose·which·content·groups·appear·on·the·playlists·tab",
      67      │ - ················"type":·"Dropdown",
      68      │ - ················"default":·"0",
      69      │ - ················"options":·[
      70      │ - ····················"Albums",
      71      │ - ····················"Playlists·(Club)",
      72      │ - ····················"Series",
      73      │ - ····················"Collections",
      74      │ - ····················"Bonus·Videos",
      75      │ - ····················"Life·Lessons"
      76      │ - ················]
      77      │ - ············},
      78      │ - ············{
      79      │ - ················"variable":·"advancedHeader",
      80      │ - ················"name":·"Advanced·settings",
      81      │ - ················"description":·"Advanced/Experimental·settings",
      82      │ - ················"type":·"Header"
      83      │ - ············},
      84      │ - ············{
      85      │ - ················"variable":·"commentPageSize",
      86      │ - ················"name":·"Comment·page·size",
      87      │ - ················"description":·"Set·how·many·comments·to·load·on·each·request.·Higher·might·be·slower",
      88      │ - ················"type":·"Dropdown",
      89      │ - ················"default":·"1",
      90      │ - ················"options":·[
      91      │ - ····················"10·(the·club·uses·this)",
      92      │ - ····················"20",
      93      │ - ····················"30",
      94      │ - ····················"40",
      95      │ - ····················"50"
      96      │ - ················]
      97      │ - ············},
      98      │ - ············{
      99      │ - ················"variable":·"debug",
     100      │ - ················"name":·"Show·additional·info",
     101      │ - ················"description":·"Show·additional·info·in·description",
     102      │ - ················"type":·"Boolean",
     103      │ - ················"default":·"false"
     104      │ - ············},
     105      │ - ············{
     106      │ - ················"variable":·"secretVariable",
     107      │ - ················"name":·"Enable·Experimental·Ambient·Playback·Rerouting",
     108      │ - ················"description":·"Only·enable·if·you·are·not·logged·in",
     109      │ - ················"type":·"Boolean",
     110      │ - ················"default":·"false"
     111      │ - ············}
     112      │ - ········],
     113      │ - ········"changelog":·{
     114      │ - ············"5":·[
     115      │ - ················"Comment·Update!",
     116      │ - ················"Finding·comments·should·now·use·less·requests",
     117      │ - ················"Replies·now·show·up",
     118      │ - ················"Added·setting·for·comment·page·size",
     119      │ - ················"Increased·EpisodeHomePage·size·to·30·instead·of·25"
     120      │ - ············],
     121      │ - ············"6":·[
     122      │ - ················"Small·lil·update",
     123      │ - ················"Changed·EpisodeHomePage·API·url·to·one·the·club·might·like·better",
     124      │ - ················"Loading·comments·might·show·toast·messages·when·searching·for·a·page·maybe?",
     125      │ - ················"Added·themes·support·-·issue·#2·on·github",
     126      │ - ················"Added·weird·video·URL·support·-·issue·#3·on·github"
     127      │ - ············],
     128      │ - ············"7":·[
     129      │ - ················"Another·small·lil·update",
     130      │ - ················"Changed·EpisodeHomePage·endpoint·again·to·one·that·gives·both·video·and·audio·content",
     131      │ - ················"Support·for·badge·content·(loads·the·first·content·id·in·the·badge)"
     132      │ - ············],
     133      │ - ············"8":·[
     134      │ - ················"Very·lil·update",
     135      │ - ················"Fixed·older·club·videos·not·loading",
     136      │ - ················"Support·for·playlist·URLs·(currently·no·way·to·get·to·them·on·grayjay)",
     137      │ - ················"Slightly·better·search"
     138      │ - ············],
     139      │ - ············"9":·[
     140      │ - ················"u·p·d·a·t·e",
     141      │ - ················"content·with·null·download_url·throws·UnavailableException",
     142      │ - ················"Randomizer·now·works·for·logged·out·users·via·episode·cache·system",
     143      │ - ················"Minor·changes·to·recommendations"
     144      │ - ············],
     145      │ - ············"10":·[
     146      │ - ················"Support·for·content·urls·with·contentGroup·in·them",
     147      │ - ················"Simplifyed·isFreeEpisode·logic",
     148      │ - ················"Support·for·getHome",
     149      │ - ················"Added·Faster·Randomizer·setting·for·logged·in·users",
     150      │ - ················"Added·Content·Groupings·setting",
  9855 more lines truncated


sources.schema.json format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Formatter would have printed the following content:

      1   1 │   {
      2     │ - ··"$schema":·"http://json-schema.org/draft-07/schema#",
      3     │ - ··"type":·"array",
      4     │ - ··"items":·{
      5     │ - ····"$ref":·"#/definitions/Source"
      6     │ - ··},
      7     │ - ··"definitions":·{
      8     │ - ····"Source":·{
      9     │ - ······"type":·"object",
     10     │ - ······"additionalProperties":·true,
     11     │ - ······"properties":·{
     12     │ - ········"name":·{
     13     │ - ··········"type":·"string"
     14     │ - ········},
     15     │ - ········"description":·{
     16     │ - ··········"type":·"string"
     17     │ - ········},
     18     │ - ········"author":·{
     19     │ - ··········"type":·"string"
     20     │ - ········},
     21     │ - ········"authorUrl":·{
     22     │ - ··········"type":·"string"
     23     │ - ········},
     24     │ - ········"maxDownloadParallelism":·{
     25     │ - ··········"type":·"integer"
     26     │ - ········},
     27     │ - ········"changelogUrl":·{
     28     │ - ··········"type":·"string"
     29     │ - ········},
     30     │ - ········"sourceUrl":·{
     31     │ - ··········"type":·"string",
     32     │ - ··········"pattern":·"^(\\./|\\.\\./|https?://|/|[a-zA-Z]:\\\\).*\\.(json)$|^$|^(https?://[^/]+/.+)$",
     33     │ - ··········"description":·"URL·to·the·source·configuration·file.·Must·be·a·relative·path·(./config.json),·absolute·path·(/config.json),·full·URL·(https://example.com/config.json),·or·base·URL·(https://example.com/),·or·empty"
     34     │ - ········},
     35     │ - ········"repositoryUrl":·{
     36     │ - ··········"type":·"string"
     37     │ - ········},
     38     │ - ········"scriptUrl":·{
     39     │ - ··········"type":·"string",
     40     │ - ··········"pattern":·"^(\\./|\\.\\./|https?://|/|[a-zA-Z]:\\\\).*\\.(js|ts|mjs)$|^$",
     41     │ - ··········"description":·"Path·to·the·script·file.·Must·be·a·relative·path·(./script.js),·absolute·path·(/script.js),·or·full·URL·(https://example.com/script.js),·or·empty"
     42     │ - ········},
     43     │ - ········"version":·{
     44     │ - ··········"type":·"integer"
     45     │ - ········},
     46     │ - ········"iconUrl":·{
     47     │ - ··········"type":·"string",
     48     │ - ··········"pattern":·"^(\\./|\\.\\./|https?://|/|[a-zA-Z]:\\\\).*\\.(png|jpg|jpeg|gif|svg|ico|webp)(\\?.*)?$|^$|^(https?://[^/]+/.+)$",
     49     │ - ··········"description":·"Path·to·the·icon·file.·Must·be·a·relative·path·(./icon.png),·absolute·path·(/icon.png),·full·URL·(https://example.com/icon.png),·URL·with·query·params,·any·valid·URL,·or·empty"
     50     │ - ········},
     51     │ - ········"id":·{
     52     │ - ··········"type":·"string",
     53     │ - ··········"format":·"uuid"
     54     │ - ········},
     55     │ - ········"packages":·{
     56     │ - ··········"type":·"array",
     57     │ - ··········"items":·{
     58     │ - ············"$ref":·"#/definitions/Package"
     59     │ - ··········}
     60     │ - ········},
     61     │ - ········"allowEval":·{
     62     │ - ··········"type":·"boolean"
     63     │ - ········},
     64     │ - ········"allowUrls":·{
     65     │ - ··········"type":·"array",
     66     │ - ··········"items":·{
     67     │ - ············"type":·"string"
     68     │ - ··········}
     69     │ - ········},
     70     │ - ········"scriptSignature":·{
     71     │ - ··········"type":·"string"
     72     │ - ········},
     73     │ - ········"scriptPublicKey":·{
     74     │ - ··········"type":·"string"
     75     │ - ········},
     76     │ - ········"platformUrl":·{
     77     │ - ··········"type":·"string"
     78     │ - ········},
     79     │ - ········"authentication":·{
     80     │ - ··········"$ref":·"#/definitions/Authentication"
     81     │ - ········},
     82     │ - ········"settings":·{
     83     │ - ··········"type":·"array",
     84     │ - ··········"items":·{
     85     │ - ············"$ref":·"#/definitions/Setting"
     86     │ - ··········}
     87     │ - ········},
     88     │ - ········"supportedClaimTypes":·{
     89     │ - ··········"type":·"array",
     90     │ - ··········"items":·{
     91     │ - ············"type":·"integer"
     92     │ - ··········}
     93     │ - ········},
     94     │ - ········"constants":·{
     95     │ - ··········"$ref":·"#/definitions/Constants"
     96     │ - ········},
     97     │ - ········"allowAllHttpHeaderAccess":·{
     98     │ - ··········"type":·"boolean"
     99     │ - ········},
    100     │ - ········"websiteUrl":·{
    101     │ - ··········"type":·"string"
    102     │ - ········},
    103     │ - ········"changelog":·{
    104     │ - ··········"type":·"object",
    105     │ - ··········"patternProperties":·{
    106     │ - ············"^[0-9]+$":·{
    107     │ - ··············"type":·"array",
    108     │ - ··············"items":·{
    109     │ - ················"type":·"string"
    110     │ - ··············}
    111     │ - ············}
    112     │ - ··········},
    113     │ - ··········"additionalProperties":·false
    114     │ - ········},
    115     │ - ········"subscriptionRateLimit":·{
    116     │ - ··········"type":·"integer"
    117     │ - ········},
    118     │ - ········"captcha":·{
    119     │ - ··········"$ref":·"#/definitions/CAPTCHA"
    120     │ - ········},
    121     │ - ········"primaryClaimFieldType":·{
    122     │ - ··········"type":·"integer"
    123     │ - ········},
    124     │ - ········"_customButtons":·{
    125     │ - ··········"type":·"array",
    126     │ - ··········"description":·"Custom·action·buttons·shown·on·the·source·card",
    127     │ - ··········"items":·{
    128     │ - ············"$ref":·"#/definitions/CustomButton"
    129     │ - ··········}
    130     │ - ········},
    131     │ - ········"_generatorUrl":·{
    132     │ - ··········"type":·"string",
    133     │ - ··········"description":·"URL·to·a·web-based·generator·for·creating·custom·plugin·instances.·If·present,·shows·a·'Generate'·button·instead·of·'Install'"
    134     │ - ········},
    135     │ - ········"_nsfw":·{
    136     │ - ··········"type":·"boolean",
    137     │ - ··········"description":·"Mark·source·as·NSFW·content.·Will·be·filtered·by·default·unless·user·opts·in"
    138     │ - ········},
    139     │ - ········"_tags":·{
    140     │ - ··········"type":·"array",
    141     │ - ··········"items":·{
    142     │ - ············"type":·"string"
    143     │ - ··········}
    144     │ - ········},
    145     │ - ········"_feeds":·{
    146     │ - ··········"$ref":·"#/definitions/Feeds"
    147     │ - ········},
    148     │ - ········"_installUrl":·{
    149     │ - ··········"type":·"string"
    150     │ - ········}
  523 more lines truncated


format ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Some errors were emitted while running checks.

```

</details>

<details>

<summary>BIOME_LINT</summary>

```text
The number of diagnostics exceeds the limit allowed. Use --max-diagnostics to increase it.
Diagnostics not shown: 4082.
Checked 13 files in 81s. No fixes applied.
Found 277 errors.
Found 3814 warnings.
Found 11 infos.assets/js/site.js:77:20 lint/style/useTemplate  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  i Template literals are preferred over string concatenation.

    75 │ function fixData(data) {
    76 │   if (varExists(data.scriptUrl)) {
  > 77 │     data.baseUrl = removeLast(data.sourceUrl, "/") + "/";
       │                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    78 │   }
    79 │   if (!data.hasOwnProperty("_feeds")) data._feeds = {};

  i Unsafe fix: Use a template literal.

     75  75 │   function fixData(data) {
     76  76 │     if (varExists(data.scriptUrl)) {
     77     │ - ····data.baseUrl·=·removeLast(data.sourceUrl,·"/")·+·"/";
         77 │ + ····data.baseUrl·=·`${removeLast(data.sourceUrl,·"/")}/`;
     78  78 │     }
     79  79 │     if (!data.hasOwnProperty("_feeds")) data._feeds = {};


assets/js/site.js:85:14 lint/style/useTemplate  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  i Template literals are preferred over string concatenation.

    83 │       if (Array.isArray(value)) continue;
    84 │       if (isRelativeUrl(value)) {
  > 85 │         data[key + "_"] = value;
       │              ^^^^^^^^^
    86 │         data[key] = getAbsoluteUrl(value, data.baseUrl);
    87 │       }

  i Unsafe fix: Use a template literal.

     83  83 │         if (Array.isArray(value)) continue;
     84  84 │         if (isRelativeUrl(value)) {
     85     │ - ········data[key·+·"_"]·=·value;
         85 │ + ········data[`${key}_`]·=·value;
     86  86 │           data[key] = getAbsoluteUrl(value, data.baseUrl);
     87  87 │         }


assets/css/site.css:78:18 lint/complexity/noImportantStyles  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! Avoid the use of the !important style.

    77 │ .bd-mode-toggle .dropdown-menu .active .bi {
  > 78 │   display: block !important;
       │                  ^^^^^^^^^^
    79 │ }
    80 │

  i This style reverses the cascade logic, and precedence is reversed. This could lead to having styles with higher specificity being overridden by styles with lower specificity.

  i Unsafe fix: Remove the style.

    78 │ ··display:·block·!important;
       │                 -----------

assets/js/site.js:57:15 lint/suspicious/noPrototypeBuiltins  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! Do not access Object.prototype method 'hasOwnProperty' from target object.

    55 │   const urls = [];
    56 │   data.forEach((item) => {
  > 57 │     if (!item.hasOwnProperty("_feeds")) return;
       │               ^^^^^^^^^^^^^^
    58 │     if (item._feeds.hasOwnProperty(key)) {
    59 │       urls.push(encodeURI(item._feeds[key]));

  i It's recommended using Object.hasOwn() instead of using Object.hasOwnProperty().

  i See MDN web docs for more details.

  i Safe fix: Use 'Object.hasOwn()' instead.

     55  55 │     const urls = [];
     56  56 │     data.forEach((item) => {
     57     │ - ····if·(!item.hasOwnProperty("_feeds"))·return;
         57 │ + ····if·(!Object.hasOwn(item,·"_feeds"))·return;
     58  58 │       if (item._feeds.hasOwnProperty(key)) {
     59  59 │         urls.push(encodeURI(item._feeds[key]));


assets/js/site.js:58:21 lint/suspicious/noPrototypeBuiltins  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! Do not access Object.prototype method 'hasOwnProperty' from target object.

    56 │   data.forEach((item) => {
    57 │     if (!item.hasOwnProperty("_feeds")) return;
  > 58 │     if (item._feeds.hasOwnProperty(key)) {
       │                     ^^^^^^^^^^^^^^
    59 │       urls.push(encodeURI(item._feeds[key]));
    60 │     }

  i It's recommended using Object.hasOwn() instead of using Object.hasOwnProperty().

  i See MDN web docs for more details.

  i Safe fix: Use 'Object.hasOwn()' instead.

     56  56 │     data.forEach((item) => {
     57  57 │       if (!item.hasOwnProperty("_feeds")) return;
     58     │ - ····if·(item._feeds.hasOwnProperty(key))·{
         58 │ + ····if·(Object.hasOwn(item._feeds,·key))·{
     59  59 │         urls.push(encodeURI(item._feeds[key]));
     60  60 │       }


assets/js/site.js:79:13 lint/suspicious/noPrototypeBuiltins  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! Do not access Object.prototype method 'hasOwnProperty' from target object.

    77 │     data.baseUrl = removeLast(data.sourceUrl, "/") + "/";
    78 │   }
  > 79 │   if (!data.hasOwnProperty("_feeds")) data._feeds = {};
       │             ^^^^^^^^^^^^^^
    80 │   if (!data.hasOwnProperty("_tags")) data._tags = [];
    81 │   for (const [key, value] of Object.entries(data)) {

  i It's recommended using Object.hasOwn() instead of using Object.hasOwnProperty().

  i See MDN web docs for more details.

  i Safe fix: Use 'Object.hasOwn()' instead.

     77  77 │       data.baseUrl = removeLast(data.sourceUrl, "/") + "/";
     78  78 │     }
     79     │ - ··if·(!data.hasOwnProperty("_feeds"))·data._feeds·=·{};
         79 │ + ··if·(!Object.hasOwn(data,·"_feeds"))·data._feeds·=·{};
     80  80 │     if (!data.hasOwnProperty("_tags")) data._tags = [];
     81  81 │     for (const [key, value] of Object.entries(data)) {


assets/js/site.js:80:13 lint/suspicious/noPrototypeBuiltins  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! Do not access Object.prototype method 'hasOwnProperty' from target object.

    78 │   }
    79 │   if (!data.hasOwnProperty("_feeds")) data._feeds = {};
  > 80 │   if (!data.hasOwnProperty("_tags")) data._tags = [];
       │             ^^^^^^^^^^^^^^
    81 │   for (const [key, value] of Object.entries(data)) {
    82 │     if (key.toLowerCase().includes("url")) {

  i It's recommended using Object.hasOwn() instead of using Object.hasOwnProperty().

  i See MDN web docs for more details.

  i Safe fix: Use 'Object.hasOwn()' instead.

     78  78 │     }
     79  79 │     if (!data.hasOwnProperty("_feeds")) data._feeds = {};
     80     │ - ··if·(!data.hasOwnProperty("_tags"))·data._tags·=·[];
         80 │ + ··if·(!Object.hasOwn(data,·"_tags"))·data._tags·=·[];
     81  81 │     for (const [key, value] of Object.entries(data)) {
     82  82 │       if (key.toLowerCase().includes("url")) {


assets/js/site.js:206:10 lint/correctness/noUnusedVariables  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! This function filterItems is unused.

    204 │   navbarMenu.appendChild(listItemElement);
    205 │ }
  > 206 │ function filterItems(items) {
        │          ^^^^^^^^^^^
    207 │   // Function to filter items based on hidden tags
    208 │   return items.filter((item) => {

  i Unused variables are often the result of typos, incomplete refactors, or other sources of bugs.

  i Unsafe fix: If this is intentional, prepend filterItems with an underscore.

    204 204 │     navbarMenu.appendChild(listItemElement);
    205 205 │   }
    206     │ - function·filterItems(items)·{
        206 │ + function·_filterItems(items)·{
    207 207 │     // Function to filter items based on hidden tags
    208 208 │     return items.filter((item) => {


assets/js/site.js:221:5 lint/style/useConst  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ! This let declares a variable that is only assigned once.

    219 │   try {
    220 │     const response = await fetch(url);
  > 221 │     let data = await response.json();
        │     ^^^
    222 │     const cardsContainer = document.getElementById("cards-container");
    223 │     cardsContainer.innerHTML = "";

  i 'data' is never reassigned.

    219 │   try {
    220 │     const response = await fetch(url);
  > 221 │     let data = await response.json();
        │         ^^^^
    222 │     const cardsContainer = document.getElementById("cards-container");
    223 │     cardsContainer.innerHTML = "";

  i Safe fix: Use const instead.

    219 219 │     try {
    220 220 │       const response = await fetch(url);
    221     │ - ····let·data·=·await·response.json();
        221 │ + ····const·data·=·await·response.json();
    222 222 │       const cardsContainer = document.getElementById("cards-container");
    223 223 │       cardsContainer.innerHTML = "";


assets/js/site.js:247:23 lint/suspicious/noDoubleEquals  FIXABLE  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Using == may be unsafe if you are relying on type coercion.

    245 │   const firstSourceIcon = document.getElementsByClassName("source-icon")[0];
    246 │   const sourceIconStyle = firstSourceIcon.getAttribute("style");
  > 247 │   if (sourceIconStyle == "display:block") {
        │                       ^^
    248 │     document.querySelectorAll(".source-icon").forEach((element) => {
    249 │       element.setAttribute("style", "display:none");

  i == is only allowed when comparing against null.

  i Unsafe fix: Use === instead.

    247 │ ··if·(sourceIconStyle·===·"display:block")·{
        │                         +

index.html:117:108 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Void elements should not have a closing tag.

    115 │           <div class="col-sm-8 col-md-7 py-2">
    116 │             <h4>About</h4>
  > 117 │             <p class="text-body-secondary">The sources offered on this site were not scanned or verified.</br>Always make sure to check any code that you're running.</p>
        │                                                                                                            ^^
    118 │           </div>
    119 │           <div class="col-sm-4 offset-md-1 py-2">


index.html:117:106 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected a matching closing tag but instead found '</br>'.

    115 │           <div class="col-sm-8 col-md-7 py-2">
    116 │             <h4>About</h4>
  > 117 │             <p class="text-body-secondary">The sources offered on this site were not scanned or verified.</br>Always make sure to check any code that you're running.</p>
        │                                                                                                          ^^^^^
    118 │           </div>
    119 │           <div class="col-sm-4 offset-md-1 py-2">

  i Expected a matching closing tag here.

    115 │           <div class="col-sm-8 col-md-7 py-2">
    116 │             <h4>About</h4>
  > 117 │             <p class="text-body-secondary">The sources offered on this site were not scanned or verified.</br>Always make sure to check any code that you're running.</p>
        │                                                                                                          ^^^^^
    118 │           </div>
    119 │           <div class="col-sm-4 offset-md-1 py-2">


index.html:177:38 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Void elements should not have a closing tag.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                      ^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>


index.html:177:36 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected a matching closing tag but instead found '</br>'.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                    ^^^^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>

  i Expected a matching closing tag here.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                    ^^^^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>


index.html:177:43 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Void elements should not have a closing tag.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                           ^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>


index.html:177:41 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected a matching closing tag but instead found '</br>'.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                         ^^^^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>

  i Expected a matching closing tag here.

    175 │     <div class="container">
    176 │       <p class="float-end mb-1" id="footerLinks">
  > 177 │         <a href="#">Back to top</a></br></br>
        │                                         ^^^^^
    178 │       </p>
    179 │       <p class="mb-1">This page is not affiliated with <a href="https://grayjay.app/">GrayJay</a> or <a href="https://futo.org/">FUTO</a>!</p>


repo/index.html:1:1 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Unescaped `<` bracket character. Expected a tag or escaped character.

  > 1 │ <?php header('Location: https://grayjay-sources.github.io'); ?>
      │ ^
    2 │ <!doctype html>
    3 │ <html>

  i Replace this character with `&lt;` to escape it.


repo/index.html:2:2 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected an element name but instead found '!'.

    1 │ <?php header('Location: https://grayjay-sources.github.io'); ?>
  > 2 │ <!doctype html>
      │  ^
    3 │ <html>
    4 │   <head>

  i Expected an element name here.

    1 │ <?php header('Location: https://grayjay-sources.github.io'); ?>
  > 2 │ <!doctype html>
      │  ^
    3 │ <html>
    4 │   <head>


repo/index.html:3:1 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected an attribute but instead found '<'.

    1 │ <?php header('Location: https://grayjay-sources.github.io'); ?>
    2 │ <!doctype html>
  > 3 │ <html>
      │ ^
    4 │   <head>
    5 │     <meta

  i Expected an attribute here.

    1 │ <?php header('Location: https://grayjay-sources.github.io'); ?>
    2 │ <!doctype html>
  > 3 │ <html>
      │ ^
    4 │   <head>
    5 │     <meta


repo/index.html:22:1 parse ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Expected a closing tag but instead found the end of the file.

    20 │   </body>
    21 │ </html>
  > 22 │
       │

  i Expected a closing tag here.

    20 │   </body>
    21 │ </html>
  > 22 │
       │


lint ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  × Some warnings were emitted while running checks.

```

</details>

<details>

<summary>SPELL_CODESPELL</summary>

```text
/github/workspace/sources.json:1377: Nam ==> Name
/github/workspace/sources.json:1670: Nam ==> Name
/github/workspace/sources.json:1807: ommitted ==> omitted
/github/workspace/sources.json:1808: ommitted ==> omitted
/github/workspace/sources.json:3473: comming ==> coming
/github/workspace/sources.json:3681: necesities ==> necessities
/github/workspace/sources.json:3693: necesities ==> necessities
/github/workspace/sources.json:3705: necesities ==> necessities
/github/workspace/sources.json:4021: didnt ==> didn't
/github/workspace/sources.json:4428: ommitted ==> omitted
/github/workspace/sources.json:4429: ommitted ==> omitted
```

</details>
