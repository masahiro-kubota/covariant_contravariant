## 型構築子　ジェネリクス/ジェネリッククラス
- 型引数を受け取ってカスタム型を定義する際に使われる。
- list[T]とかtuple[T]とかもジェネリクス
## 共変　反変
- A <: B ならば T`<A>` <: T`<B>` のとき、型構築子は共変
- A <: B ならば T`<B>` <: T`<A>` のとき、型構築子は反変

共変とか反変は型構築子が持つ性質であることに注意
## リスコフの置換原則 LSP
- スーパークラスのオブジェクトを使用している箇所で、そのサブクラスのオブジェクトで置き換えても、プログラムが正しく動作すべきであるという原則。
- サブクラスの方が機能が多い分、当然逆は成り立たない。
- スーパークラスの方が機能が少ないから、サブクラスの一部機能は全く使われなくなる

## 入力型を反変なジェネリクス、出力型を共変なジェネリクスにしておけばpythonの実行時エラーを防げる。（ある意味での型安全）
- スーパークラスを受け取るクラスよりも、サブクラスを受け取るクラスの方が低機能。なぜなら、スーパークラスを受け取るクラスはLSPより、そのサブクラスも受け取ってそれぞれの処理を記述しておくことことができるから。T`<B>` <: T`<A>`
- サブクラスを返すクラスよりも、スーパークラスを返すクラスの方が低機能。なぜなら、スーパークラスの方が要素が少なくクラス内の処理が少ないから。

```
mypy covariant_contravariant.py
```
