---
layout: post
unique_id: es6_import_export
title: ES6 Import Export
categories: [javascript]
locations: 
---

A brief tutorial on import and export statements in ES6.

In ES6, a **module** is a piece of code isolated into a single file:
* All functions and state within a module are local to the module unless they are marked for **export**
* Modules can import objects from other modules via **import** statements
* Each module is itself a singleton, i.e. multiple imports of a module do **not** create multiple instances of that module

# Basic Exports

The simplest way to export an object from a module is simply to prefix it with **export** upon declaration.  For example, if we have a function **foo**:

```
function foo() {
  // code
}
```

We can export it with the **export** keyword:

```
export function foo() {
  // code
}
```

Similarly for constants and variables:

```
export const bar = "bar"
export let baz = "baz"
export var qux = "bah humbug"
```

If you prefer instead to list out all exported objects at the end of a module, we can use this syntax:

```
function foo() {
  // code here
}
const bar = "bar"

// more code here ...

export { foo, bar }
```

You can use these syntaxes to export any **named** variable.

### Basic Imports

So, if moduleA exports **foo**, how does moduleB import it?

Import statements must be declared at the top of a module.  The most basic way to import **foo** into moduleB is:

```
import { foo } from moduleA
```

Now, we can use function **foo** from within moduleB.

With this syntax, if moduleA exports multiple objects, moduleB can selectively choose which objects to import.  Suppose moduleA exposes **foo**, **bar**, and **baz**:

```
function foo() {
  // code here
}
const bar = "bar"
const baz = "baz"
export { foo, bar, baz }
```

If moduleB only wants **foo** and **bar** from moduleA, we can write:

```
import { foo, bar } from moduleA
```

Now, we can use both **foo** and **bar** within moduleB.

### Star Imports

What if we wanted to import all functions from moduleA into moduleB?  We can use the **\*** operator:

```
import * as A from moduleA
```

Now, **foo**, **bar**, and **baz** can be referenced within moduleB as **A.foo**, **A.bar**, and **A.baz**, respectively.  We've prefixed all exported objects from moduleA with a **namespace**.

The **namespace** concept is quite handy!

What if moduleA and moduleC both expose **foo** function and moduleB wants to import both?
```
import * as A from moduleA
import * as C from moduleC
```

We can then reference **A.foo** and **C.foo** in moduleB.

Similarly, if moduleB has its own **foo** function too, the namespace lets us distinguish between moduleB's **foo** and an imported **foo**.

### Renaming Imports

However, this **\*** syntax means we have to import all exported functions from A and C which may be undesirable.  Another way to handle the naming conflict is to **rename** using the **as** keyword on import:

```
import { foo as Afoo } from moduleA
import { foo as Cfoo } from moduleC
```

We can then reference **Afoo** and **Cfoo** within moduleB.

### Renaming Exports

One might wonder, if we can do renames on imports, can we do renames on exports?  Why yes we can!  ModuleA can rename its own exports:

```
export { foo as Afoo }
```

Then, moduleB would import as:

```
import { Afoo } from moduleA
```

This can be handy if you want to expose a formal name but keep a shorthand or concise name within the module.

### Default Imports and Exports

A common pattern is for a single file to only export a single object (usually a function or class).  For this case, ES6 added the **default** keyword.

For example, assume moduleA wants to export function **foo** and moduleB wants to import it.  In moduleA, we'll use a **default** export:

```
export default function foo() {
  // code
};
```

In moduleB, we can now use a **default** import:

```
import foo from moduleA
```

We can now reference **foo** within moduleB.

There are two differences from the basic import syntax.  First, we don't need the curly brace {} operators.  Second, we can actually name the imported object whatever we want in moduleB.

Another valid import statement could be:

```
import bar from moduleA
```

Now, the function defined as **foo** in moduleA is referenced a **bar** in moduleB!

There are a few special requirements to the **default** export syntax:

1. we can only have one default export in a module
2. **export default** syntax actually creates a variable named **default**
  * this prevents us from using **export default** syntax on types where more than one variable can be defined on a single line
3. you can mix default exports with normal exports
4. you can use the **as** operator to specify the default export

Item 1 should hopefully make sense.  We can't have two different default objects exported since it gets assigned to one reference when we import.

Item 2 may seem a bit confusing.  The issue is that in ES6, we can declare multiple constants in a single line of code:

```
const a, b, c
```

What would it mean if we added the **export default** keyword to that line?

```
export default const a, b, c
```

By Item 1, only one of them can be default, but it's unclear which one should be default.

For this reason, **named** constants and variables can not be declared via the **export default** syntax.  Instead, one could explicitly choose one via item 4:

```
export { a as default }
```

Note that functions and classes are exempt from this rule since you can not define multiple functions or classes in a single line.

For an example of item 3.  If we want the default export to be **foo** but also expose **bar**, we can have:

```
export default function foo() {
  // code
}

export const bar = "bar"
```

For an example of item 4::

```
export { foo as default, bar }
```

### Star Exports

Lastly, a common use case is to export all imported objects from several modules (accumulator pattern).  We can use the **\*** keyword to do this:

Let's assume moduleA wants to export several constants and moduleB wants to re-export them all.  Then moduleA would have:

```
export const foo = "foo"
export const bar = "bar"
export const baz = "baz"
```

ModuleB **could** re-export them one by one:

```
import { foo, bar, baz } from moduleA
export { foo, bar, baz }
```

But this would be verbose since exposing a new constant requires modifying potentially many files.  The **\*** syntax lets us re-write moduleB as:

```
export * from moduleA
```

Now if moduleD can import **foo** from moduleB using one of our import syntaxes:

```
import { foo } from moduleB
```

Much more clean :)

That's all there is to imports and exports in ES6!

For more reading on the history of modules, check out [this link](http://exploringjs.com/es6/ch_modules.html#sec_modules-in-javascript).
