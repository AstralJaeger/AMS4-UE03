# latex-fhhagenberg

[![Build PDF](https://github.com/AstralJaeger/latex-fhhagenberg/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/AstralJaeger/latex-fhhagenberg/actions/workflows/build.yml)

 Latex template for assignments from FH Hagenberg.

 This is a basic template which includes a GitHub Action which builds the resulting pdf and adds it to a release.
 There is also the ``.bundleinclude`` file, all file globs in this file will be added to a zip archive and also added to the same release so you can immedialty hand it in. I would suggest adjusting the filename in the ``.github/workflows/build.yml`` file so you don`t have to rename it.

## Building Locally

In order to build LaTeX locally you need to install LaTeX, I suggest also installing the [LaTeX Workshop Extenson](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) for VSCode or the [TeXiFy Plugin](https://plugins.jetbrains.com/plugin/9473-texify-idea) for IDEA.
