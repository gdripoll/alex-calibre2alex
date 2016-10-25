# calibre2alex

Converts files from a Calibre directory structure:

```
dir
+-- autor
    +--libro
       +-- archivo.pdf
       +-- archivo.epub
       +-- archivo.opf (no lo toma)
       +-- archivo.jpg (no lo toma)
```

to an alex structure:

```
dir
+-- autor
    +-- autor.archivo.esp.pdf
    +-- autor.archivo.esp.epub
```

