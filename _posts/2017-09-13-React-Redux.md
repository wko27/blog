---
layout: post
unique_id: react_redux
title: React-Redux
categories: []
locations: 
---

Notes from learning [React](https://facebook.github.io/react/tutorial/tutorial.html#getting-started) and [Redux example](http://redux.js.org/docs/basics/).

# react

**react** is a javascript framework that lets you create **interactive views** by **declaring** how a UI component should be rendered

### glossary

* **component**
  * takes in properties and state and renders views or other components
  * components can render other components
* **component hierarchy**
  * tree of components
* **element**
  * what a component's render returns
* **props**
  * properties of a component
  * typically fixed and passed from its parent component
  * changes to props triggers a render
  * callbacks are usually passed down via props
* **state**
  * state of a component
  * typically changed by this component
  * changes to state triggers a render
* **controlled component**
  * a component with no state, it relies on data sent by its parent
* **functional component**
  * a component with no state that only has a render function
* **presentational component**
  * a component that only knows how to display its properties
  * usually this doesn't have state
  * typically also a functional component
* **container component**
  * a component that handles state and behaviors

# redux

**redux** is a javascript framework that manages state in a complex app:
* the only way to change state is to **dispatch** an **action**
* the change itself is handled by a reducing function: (old state, action) => new state

a few other principles:
* state is stored in a global javascript object
* state is immutable (shallow copies everywhere)
* reducing functions are pure (side-effect free and deterministic)

### glossary

* **action**
  * javascript object that contains a 'type' and 'payload'
* **action creator**
  * function that produces actions
* **dispatch**
  * dispatches an action which will be picked up by a reducer
  * can be called by almost any part of the codebase
* **store**
  * javascript object containing the global data set
* **reducer**
  * function that performs (old state, action) => new state
  * the state parameter takes in a default value which initializes state
  * this function should be deterministic and have no side-effects
    * it can NOT call dispatch
  * reducers usually operate on state that is a sub-tree of the store
* **combineReducers**
  * redux helper function to create a 'root reducer' that combines functionality from individual reducers
  * specifically, it assumes that each reducer manages an independent part of the global store
* **connect**
  * redux helper function which creates components with an automatic 'shouldComponentUpdate' function
* **mapStateToProps**
  * function which takes in state and returns the properties for a presentational component
  * passed as an argument to 'connect'
* **mapDispatchToProps**
  * function which takes in dispatch and returns callback properties for a presentational component
  * passed as an argument to 'connect'

