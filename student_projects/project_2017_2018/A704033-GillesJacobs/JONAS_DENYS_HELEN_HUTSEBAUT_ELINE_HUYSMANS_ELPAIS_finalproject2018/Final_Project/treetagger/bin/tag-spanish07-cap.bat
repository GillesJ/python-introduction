@echo off

set TAGDIR=C:\Users\pagoetha\Documents\SCAP\treetagger

set BIN=%TAGDIR%\bin
set CMD=%TAGDIR%\cmd
set LIB=%TAGDIR%\lib
set TAGOPT=%LIB%\SpanishPar_07.par -token -lemma -sgml -cap-heuristics

if "%2"=="" goto label1
perl %CMD%\utf8-tokenize.perl -a %LIB%\spanish-abbreviations "%~1" | %BIN%\tree-tagger %TAGOPT% > "%~2"
goto end

:label1
if "%1"=="" goto label2
perl %CMD%\utf8-tokenize.perl -a %LIB%\spanish-abbreviations "%~1" | %BIN%\tree-tagger %TAGOPT%
goto end

:label2
echo.
echo Usage: tag-spanish2 file {file}
echo.

:end
