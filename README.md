# Liferay Learn

This is a proof of concept for the Liferay Learn project using [Sphinx](http://www.sphinx-doc.org/en/master/).

Liferay Learn is an initiative to organize, create, and curate resources for learning about Liferay. An important part of these resources is documentation. The goal of this proof of concept is to see if the following requirements can be satisfied:

-   generate a documentation site from the md files in separate repos
-   provide different versions of a product's documentation
-   provide internationalization support
-   provide pdf and epub support
-   consistent design language with the Liferay brand
-   provide syntax highlighting support

## Set Up

### Prerequisites

Checkout Sphinx's documentation for the python [prerequisites](http://www.sphinx-doc.org/en/master/intro.html#prerequisites) and [installation](http://www.sphinx-doc.org/en/master/usage/installation.html) steps.

Please also install [node](https://nodejs.org/en/).

### Installation

Since the documentations here are written in `markdown`, you will need to install `recommonmark` via:

```
pip install recommonmark
```

We are also using `sphinx-markdown-tables` since markdown tables are not supported in Sphinx. To install, run:

```
pip install sphinx-markdown-tables
```

To generate files for localization, we need `sphinx-intl` by running:

```
pip install sphinx-intl
```

If you would like to take advantage of the live update feature, install `sphinx-autobuild` with:

```
pip install sphinx-autobuild
```

Finally, run:

```
npm install
```

## Generating Files

To generate a file for a specific product and version, pass the name of the directory in the `FILE` parameter.

To generate `HTML` 

```
make build/html/commerce-en
```
To generate `pdf` in the `build/latexpdf` directory, run

```
make latexpdf FILE=commerce-en
```

To generate `epub` in the `build/epub` directory, run

```
make epub FILE=commerce-en
```

## Live Reload

Run a watch task to compile css as you make changes:

```
npm run css:watch
```

In a separate terminal, run

```
make livehtml FILE=commerce-en
```

The site will be served at http://127.0.0.1:8000

## Internationalization

Read about Sphinx's internationalization [details here](http://www.sphinx-doc.org/en/master/usage/advanced/intl.html).

To generate the `pot` files in the `build/gettext` directory, run:

```
make gettext
```

Then generate the directory structure under the specified locale inside the `source/locale` directory by running:

```
make po LOCALE='zh_CN'
```

The resulting `po` files can be translated.