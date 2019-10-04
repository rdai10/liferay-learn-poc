For Commerce and DXP Cloud docs, the workflow could look something like:

### Initial:

-   Create a directory called `dump`
-   Add `dump` to `.gitignore`
-   Clone the Commerce docs in the dump directory
    -   `git clone git@github.com:liferay/liferay-help.git`
-   Clone the DXP Cloud docs in the dump directory
    -   `git clone git@github.com:liferay/liferay-learn-dxp-cloud.git`
-   _When we have multiple versions, we may want to clone and checkout the version branch for each product._

### Recurring:

-   Before generating any static web pages, we want to make sure we have the latest docs by running the following in each directory (ie: liferay-learn-dxp-cloud, commerce-2.x)
    -   `git pull rebase upstream master`
-   If any of the docs from the `liferay-learn-${product}` repos require a build step, build now.
-   Then we want to create a folder for each product following the `product-version-locale` naming convention in the `source` directory.
    -   For example, we would have a `source/commerce-en` folder for the English Commerce docs.
    -   If multiple versions are available, each version would have its own directory. For example, Japanese docs for Liferay DXP version 7.2.x would be in `source/dxp-7.2.x-ja`.
-   From the dump, docs would be copied to its corresponding `product` directory under `source/${product-version-locale}`. For instance, contents of `liferay-learn-dxp-cloud/docs/en` will be copied to `source/dxp-cloud-en/product`.
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