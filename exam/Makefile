PDFLATEX = pdflatex -interaction nonstopmode -shell-escape -file-line-error
TOOLS = Makefile
TEX := $(shell ls *.tex)
PDF := $(TEX:%.tex=%.pdf)

all: $(PDF)

%.pdf: %.tex $(TOOLS)
	$(PDFLATEX) $*.tex
	rm -f $*.aux *.log
	chmod 644 $*.pdf

clean:
	rm -f *.nav *.out *.snm *.toc *.vrb *.aux *.log
	rm -rf _minted*

clobber: clean
	rm -f $(PDF)
