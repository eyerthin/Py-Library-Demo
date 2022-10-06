argparse主要被用来实现命令行选项和参数解析，在构建命令行程序时，是一个很好用的标准库。当然还存在一些其他强大的功能，可以将命令行输入的参数转化为列表等格式。

----

*声明：本文档基于python3.10。如有复杂需求推荐查看官方文档，本文档不保证时效性和完整性，仅保留我认为或许比较有用的一部分。*

[01]: https://docs.python.org/zh-cn/3.10/howto/argparse.html	"argparse教程"
[02]: https://docs.python.org/zh-cn/3.10/library/argparse.html	"argparse文档"

```python
import argparse

# 创建解析器
parser = argparse.ArgumentParser()
# 添加参数
parser.add_argument()
# 解析参数（将参数字符串转化为对象并将其设为命名空间的属性）
parser.parse_args()
```

#### ArgumentParser对象

`class argparse.ArgumentParser(prog=None, usage=None, description=None, epilog=None, parents=[], formatter_class=argparse.HelpFormatter, prefix_chars='-', fromfile_prefix_chars=None, argument_default=None, conflict_handler='error', add_help=True, allow_abbrev=True, exit_on_error=True)[¶](https://docs.python.org/zh-cn/3.10/library/argparse.html#argparse.ArgumentParser)`（太长可以不看）

常用参数：

* prog：程序的名称（默认值：`os.path.basename(sys.argv[0])`）
* usage：描述程序用途的字符串（可以添加 `%(prog)s`参数，默认值由添加的参数自动生成）
* description：在参数帮助文档之前显示的文本（无默认值）
* epilog：在参数帮助文档之后显示的文本（无默认值）
* formatter_class：自定义description和epilog的输出格式。
  * RawDescriptionHelpFormatter表示description和epilog已经被正确格式化了，不能再命令行中被换行。
  * RawTextHelpFormatter表示保留所有种类文字的空格，包括参数的描述。多余的新行会被替换成一行。如果想保留多重的空白行，可以在新行之间加空格。
  * ArgumentDefaultsHelpFormatter自动添加默认的值的信息到每一个帮助信息的参数中。
  * MetavarTypeHelpFormatter在每一个参数中使用type的参数名当做它的显示名（默认是dest）

#### add_argument()方法

`ArgumentParser.add_argument(name or flags...[, action][, nargs][, const][, default][, type][, choices][, required][, help][, metavar][, dest])`

* name or flags：一个命名或者一个选项字符串的列表。（例如："bar", "-f", "--foo"）
* action：参数在命令行中出现的动作基本类型。
  * store 存储参数的值，默认动作。
  * append 存储一个列表，并且将每个参数追加到列表中。
  * count 计算一个关键字参数出现的次数，默认为None而不是0。
  * help 打印帮助信息，一般用-h --help就可以了。
  * version 版本信息（例如：version='%(prog)s 1.48'）。
* nargs：
  | 值   | 含义           |
  | ---- | -------------- |
  | N    | 参数确切个数   |
  | ‘?’  | 0或1个参数     |
  | ‘*’  | 0或更多参数    |
  | ‘+’  | 至少有一个参数 |
* default：当参数未在命令行中出现并且也不存在于命名空间对象时所产生的值。
* type：命令行参数应当被转换成的类型。
* choices：可用参数的容器。
* required：此参数是否可省略。
* help：一个此选项作用的简单描述。
* metavar：改变dest显示的名称，实际属性名称依然是dest决定。
* dest：parse_args()所返回对象的属性名称。有默认的生成规则。

#### parse_args()方法

`ArgumentParser.parse_args(args=None, namespace=None)`

* args：要解析的字符串列表，默认是从sys.argv获取。
* namespace：用于获取属性的对象，默认是一个新的空Namespace对象。

其实就是获取命令行参数的方法











