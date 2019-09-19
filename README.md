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

To generate `HTML`, run

```
make html
```
The generated html files will be in the `build/html` directory. 

To generate `pdf`, run
```
make latexpdf
```
The generated pdf files will be in the `build/latex` directory. 

To generate `epub`, run
```
make epub
```
The generated epub files will be in the `build/epub` directory.