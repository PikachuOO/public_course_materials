PDFLATEX = pdflatex -interaction nonstopmode -shell-escape -file-line-error
TOOLS = include.tex Makefile
LECTURE_TEX := $(shell ls *.tex|egrep -v '(include|_notes|.*_slides).tex$$')
SLIDES_PDF := $(LECTURE_TEX:%.tex=%.pdf)
NOTES_PDF := $(LECTURE_TEX:%.tex=%_notes.pdf)
FIGURES := $(shell ls Pic/*.fig)
FIGURES_PS := $(FIGURES:%.fig=%.ps)
IMAGES := $(shell ls Pic/*.gif)
IMAGES_PS := $(IMAGES:%.gif=%.ps)
IMAGES_PNG := $(IMAGES:%.gif=%.png)

all: $(FIGURES_PS) $(IMAGES_PS) $(IMAGES_PNG) $(SLIDES_PDF)

%.pdf: %.tex $(TOOLS)
	$(PDFLATEX) "\input{$*.tex}"||true
	ln -sf `basename $*.tex` $*_notes.tex
	$(PDFLATEX) "\def\notes{1}" "\input{$*_notes.tex}"||true
	rm $*_notes.tex
	chmod 644 $*.pdf
	rm `ls -d $*.*|egrep -v '(tex|pdf)$$'`
	rm -rf _minted-$**

clean:
	rm -f *.nav *.out *.snm *.toc *.vrb *.aux *.log
	rm -rf _minted*

clobber: clean
	rm -f $(SLIDES_PDF) $(NOTES_PDF)


%.ps: %.fig $(TOOLS)
	fig2dev -L eps -m 1.25 $*.fig $*.ps
	fig2dev -L png -m 2 -S 4 $*.fig $*.png

%.ps: %.gif
	convert $*.gif $*.ps
	
%.png: %.gif
	convert $*.gif $*.png
