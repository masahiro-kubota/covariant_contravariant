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

## 入力を反変、出力を共変にしておけばpythonの実行時エラーを防げる。（ある意味での型安全）

