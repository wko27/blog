---
layout: post
unique_id: es6_import_export
title: ES6 Import Export
categories: []
locations: 
---

A brief tutorial on import and export statements in ES6.

# Basic exports

In ES6, we can only import objects that other modules export.

The simplest way to export an object is simply to prefix it with **export** upon declaration.  For example, if we have a function:

```
function foo() {
  // code
}
```

To export it, we simply do:

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

If you prefer instead to list out all exported objects at the end, you can do it like this:

```
function foo() {
  // code here
}
const bar = "bar"
export { foo, bar }
```

You can use these syntaxes to export any **named** variable.

### Basic imports

So, if moduleA.js exports **foo**, how does moduleB.js import it?  The most basic way is:

```
import { foo } from moduleA
```

If moduleA.js exports multiple objects like:

```
function foo() {
  // code here
}
const bar = "bar"
export { foo, bar }
```

Then, moduleB.js can import all of them via:
```
import { foo, bar } from moduleA
```

### Renaming Imports and Exports

However, what if moduleA and moduleA2 both expose **foo** function and moduleB wants to import both?  The import syntax gives us a few options for handling this.  The simplest is providing a namespace prefix for all objects imported from each module:

```
import * as A from moduleA
import * as A2 from moduleA2
```

We can then reference **A.foo** and **A2.foo** in moduleB.

However, this means we have to import all exported functions from A and A2 which may be undesirable.  Another way to handle the naming conflict is to **rename** using the **as** keyword on import:

```
import { foo as Afoo } from moduleA
import { foo as A2foo } from moduleB
```

We can then reference **Afoo** and **A2foo** in moduleB.

One might wonder, if we can do renames on imports, can we do renames on exports?  Why yes we can!  ModuleA can rename its own exports:

```
export { foo as Afoo }
```

Then, moduleB would import as:

```
import { Afoo } from moduleA
```

### Default Imports and Exports

A common pattern is for a single file to only export a single object (usually a function or class).  For this case, ES6 added the **default** keyword.

For this example, we'll assume moduleA wants to export function **foo** and moduleB wants to import it.  In moduleA, we can use a default export:

```
export default function foo() {
  // code
};
```

In moduleB, we can now use a default import:

```
import newnameforfoo from moduleA
```

Note that this syntax allows the importer to choose any name for the default imported object!

### Star Imports

Lastly, another common use case is to export all imported objects from several modules (accumulator pattern).  We can use the **\*** keyword to do this:

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

But this would be annoying since adding a new constant means modifying many files.  The **\*** syntax lets us re-write moduleB as:

```
export * from moduleA
```

Much more clean :)

That's all there is to imports and exports in ES6!
