# Liferay Learn


This is a proof of concept for the Liferay Learn project using [Sphinx](http://www.sphinx-doc.org/en/master/). 

Liferay Learn is an initiative to organize, create, and curate resources for learning about Liferay. An important part of these resources is documentation. The goal of this proof of concept is to see if the following requirements can be satisfied:
- generate a documentation site from the md files in separate repos
- provide different versions of a product's documentation
- provide internationalization support
- provide pdf and epub support
- consistent design language with the Liferay brand
- provide syntax highlighting support

## Set Up

### Prerequisites
Checkout Sphinx's documentation for the python [prerequisites](http://www.sphinx-doc.org/en/master/intro.html#prerequisites) and [installation](http://www.sphinx-doc.org/en/master/usage/installation.html) steps.

Please also install [node](https://nodejs.org/en/).

### Installation

Since the documentations here are written in `markdown`, you will also need to install _recommonmark_ via:
```
pip install --upgrade recommonmark
```
We are also using _sphinx-markdown-tables_ since markdown tables are not supported in Sphinx. To install, run:
```
pip install sphinx-markdown-tables
```

Finally, run:
```
npm install
```

## Generating Files

To generate `HTML` in the `build/html` directory, run

```
make html
```

To generate `pdf` in the `build/latex` directory, run
```
make latexpdf
```

To generate `epub` in the `build/epub` directory, run
```
make epub
```

## Live Reload 

First, install `sphinx-autobuild` with 
```
pip install sphinx-autobuild
```

<!-- TO DO: use Make to compile css -->
Run a watch task to compile css as you make changes:
```
npm run css:watch
```

In a separate terminal, run 
```
make livehtml
```
The site will be served at http://127.0.0.1:8000

## Internationalization

Read about Sphinx's internationalization [details here](http://www.sphinx-doc.org/en/master/usage/advanced/intl.html).

To generate the `pot` files in the `build/gettext` directory, run `make gettext`.

To generate the `po` files for translation in the `source/locale` directory, install `sphinx-intl` with:
```
pip sphinx-intl
```
Then generate the directory structure under the specified locale, for example `zh_CN`, by running:

```
make po locale='zh_CN'
```
The resulting `po` files can be translated. 
