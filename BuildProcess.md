For Commerce and DXP Cloud docs, the workflow could look something like:

### Initial:

-   Create a directory called `sphinx`, generate with `sphinx-quickstart`
    -  move `_static`, `_templates` to the root, move `conf.py` and `contents.rst` in `_configuration`

### Recurring:

-   Then we want to create a folder for each product following the `product-version-locale` naming convention in the `source` directory.
    -   For example, we would have a `source/commerce-en` folder for the English Commerce docs.
    -   If multiple versions are available, each version would have its own directory. For example, Japanese docs for Liferay DXP version 7.2.x would be in `source/dxp-7.2.x-ja`.
-   We want to create sym links for the English docs
-   For other locale, we want to copy the English contents and over ride the docs with content from the correspondign locale folder in the `docs/` directory.
-   We also want to copy both the `conf.py` file and `contents.rst` file from `_configuration` folder to the root of each product folder.

    After moving all the files, the source directory should look like:

```
├───source
│   ├───commerce-en
│   | |───conf.py
│   | |───contents.rst
│   | └───product
│   └───commerce-ja
│   | |───conf.py
│   | |───contents.rst
│   | └───product
│   └───dxp-7.2.x-en
│   | |───conf.py
│   | |───contents.rst
│   | └───product
```

### Final Output:

-   Once we know all the languages we are going to support, we can leverage the existing `make build/html/%` target to produce html in the desired language. We would still leverage Sphinx's built in language support to translate the site.
-   The final output should look like:

```
├───build
|   |───html
│   | ├───commerce-en
│   | | |───_images
│   | | |───_sources
│   | | |───_static
│   | | |───product
│   | | |───...
│   | | └───index.html
│   | ├───commerce-ja
│   | | |───_images
│   | | |───_sources
│   | | |───_static
│   | | |───product
│   | | |───...
│   | | └───index.html
│   | ├───dxp-7.2.x-en
│   | | |───_images
│   | | |───_sources
│   | | |───_static
│   | | |───product
│   | | |───...
│   | | └───index.html
```
