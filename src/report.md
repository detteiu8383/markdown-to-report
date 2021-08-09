\begin{center}
{\LARGE 真ん中タイトル}
\end{center}

\begin{flushright}
{\large 右寄せ　名前}
\end{flushright}

# Markdown2PDF

1. `report.md`を編集して
2. `references.bib`を編集して
3. 使用画像を`./src/img`に入れて
4. `build.bat`を実行すると
5. PDF が出来る

## Requirement

- Pandoc <https://pandoc.org/installing.html>
- pandoc-crossref <https://github.com/lierdakil/pandoc-crossref>
- LaTeX
  - uplatex
  - dvipdfmx
  - biber
  - Latexmk

## Markdown 形式と LaTeX コマンドの対応

<https://pandoc.org/MANUAL.html#pandocs-markdown>を参考にすると理解が深まると思います。

普通の文章。**太字**。_斜体_。

明示したリンク <https://trap.jp/post/1123/>

[タイトル付きのリンク](https://trap.jp/post/1123/ "タイトル")

自動リンク https://trap.jp/post/1123/

ここは本文です。

> これは引用文です。

ここも本文です。

# h1 見出し 1

本文本文本文本文本文本文

## h2 見出し 1 {#sec:h2_1}

本文本文本文本文本文本文

## h2 見出し 2 {-}

番号がつかない見出し

### h3 見出し

[@sec:h2_1]見出しへのリンク

#### h4 見出し

本文本文本文本文本文本文

##### h5 見出し

本文本文本文本文本文本文

###### h6 見出し

本文本文本文本文本文本文

---

| 変身前     |      変身後      |       声優 |
| :--------- | :--------------: | ---------: |
| 星空みゆき |  キュアハッピー  |   福園美里 |
| 日野あかね |   キュアサニー   | 田野アサミ |
| 黄瀬やよい |   キュアピース   |   金元寿子 |
| 緑川なお   |   キュアマーチ   | 井上麻里奈 |
| 青木れいか | キュアビューティ | 西村ちなみ |

: スマイルプリキュア！に登場するキャラクター {#tbl:precure}

[@tbl:precure]に、スマイルプリキュア！に登場するキャラクターを示す。

![ここにキャプション](./img/sample_image.png)

<div id="fig:narabi">
![png画像の挿入](./img/sample_image.png){#fig:png width=60%}

![pdf画像の挿入](./img/sample_image.pdf){#fig:pdf width=40%}\hfill
![jpg画像の挿入](./img/sample_image.jpg){#fig:jpg width=40%}

![](./img/mitsu.png){width=15%}
![](./img/mitsu.png){width=20%}
![](./img/mitsu.png){width=15%}
![](./img/mitsu.png){width=10%}

![](./img/so.png){width=15%}\hfill
![](./img/so.png){width=20%}\hfill
![](./img/so.png){width=15%}\hfill
![](./img/so.png){width=10%}

画像の挿入テスト

</div>

[@fig:narabi]に、各画像の挿入結果を示す。[@fig:pdf]は pdf 形式、[@fig:png]は png 形式、[@fig:jpg]は jpg 形式の画像である。

$$
\begin{aligned}
\frac{\partial f}{\partial t} + \xi_i \frac{\partial f}{\partial X_i} &= J(f, f)\\
J(f, f) &= \frac{1}{m} \int_{\xi_1} \int_{\alpha} (f'f'_1 - ff_1)B(\lvert \alpha_j V_j \rvert, V))d\Omega(\bm{\alpha})d^3\xi_1
\end{aligned}
$${#eq:boltzmann}

[@eq:boltzmann]はボルツマン方程式である。

脚注も利用することができる[^1]。

[^1]: このように脚注が表示される。

参考文献の表示\cite{Laala}。

`\clearpage`、`\newpage`で改ページ。

\begin{lstlisting}[caption=キャプション,label=lst:python,language=python]
# 日本語のメモ
N = 20
for i in range(N):
  print(i % 3 // 2 * "Fizz" + i % 5 // 4 * "Buzz" or i + 1)
\end{lstlisting}

ソースコード[\ref{lst:python}]はPythonにおけるFizzBuzzの例
