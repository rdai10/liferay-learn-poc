For Commerce and DXP Cloud docs, the workflow could look something like:

### Initial:

- Create a directory called `dump`
- Add `dump` to `.gitignore`
- Clone the Commerce docs in the dump directory
  - `git clone git@github.com:liferay/liferay-help.git`
- Clone the DXP Cloud docs in the dump directory
  - `git clone git@github.com:liferay/liferay-learn-dxp-cloud.git`

### Recurring:

- Before generating any static web pages, we want to make sure we have the latest docs by running the following in each directory (ie: liferay-learn-dxp-cloud)
  - `git pull rebase upstream master`
  - _In the future, when we have multiple versions, we may want to generate a directory in the `dump` for each version of a given product._

- If any of the docs from the `liferay-learn-${product}` repos require a build step, build now.
- Then we want to move the doc dumps to the corresponding locale folder in the `source` directory. For example, contents of `liferay-learn-dxp-cloud/docs/en` should be copied to `source/en/dxp-cloud`.
- We also want to **copy** both the `conf.py` file and `contents.rst` file to the root of each locale folder under `source` because Sphinx doesn't allow multiple source folders.
  
  After moving all the files, the source directory should look like:
```
├───source
│   ├───en
│   | |───conf.py
│   | |───contents.rst
│   | |───Commerce
│   | └───DXP Cloud
│   └───ja
│   | |───conf.py
│   | |───contents.rst
│   | |───Commerce
│   | └───DXP Cloud
```

### Final Output:

- Once we know all the languages we are going to support, we can leverage the existing `make build/html_%` target to produce html in the desired language. We would still leverage Sphinx's built in language support to translate the site. 
- The final output should look like: 

```
├───build
│   ├───html_en
│   | |───...
│   | |───Commerce
│   | └───DXP Cloud
│   └───html_ja
│   | |───...
│   | |───Commerce
│   | └───DXP Cloud
```