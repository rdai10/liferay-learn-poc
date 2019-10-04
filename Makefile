# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = build
locale        = 

# Default Target for now, should aim for a `make all`
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: livehtml

livehtml:
	sphinx-autobuild "$(SOURCEDIR)" "$(BUILDDIR)/html"

.PHONY: po $(locale)

po $(locale): 
	sphinx-intl update -p "$(BUILDDIR)/gettext" -l $(locale)

build/html_%:
	sphinx-build -b html -D language=$(filter-out 'build/html_', $@) "$(SOURCEDIR)/en" $@